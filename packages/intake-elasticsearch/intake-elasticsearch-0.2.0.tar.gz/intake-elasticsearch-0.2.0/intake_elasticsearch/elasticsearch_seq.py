from intake.source import base
import json
from . import __version__
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


class ElasticSearchSeqSource(base.DataSource):
    """
    Data source which executes arbitrary queries on ElasticSearch

    This is the sequential reader: will return a list of dictionaries.

    Parameters
    ----------
    query: str
       Query to execute. Can either be in Lucene single-line format, or a
       JSON structured query (presented as text)
    npartitions: int
        Split query into this many sections. If one, will not split.
    qargs: dict
        Further parameters to pass to the query, such as set of indexes to
        consider, filtering, ordering. See
        http://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.search
    es_kwargs: dict
        Settings for the ES connection, e.g., a simple local connection may be
        ``{'host': 'localhost', 'port': 9200}``.
        Other keywords to the Plugin that end up here and are material:

        scroll: str
            how long the query is live for, default ``'100m'``
        size: int
            the paging size when downloading, default 1000.
    metadata: dict
        Extra information for this source.
    """
    name = 'elasticsearch_seq'
    container = 'python'
    version = __version__
    partition_access = False

    def __init__(self, query, npartitions=1, qargs={}, metadata={},
                 **es_kwargs):
        from elasticsearch import Elasticsearch
        self._query = query
        self._qargs = qargs
        self._scroll = es_kwargs.pop('scroll', '100m')
        self._size = es_kwargs.pop('size', 1000)  # default page size
        self._es_kwargs = es_kwargs
        self._dataframe = None
        self.es = Elasticsearch([es_kwargs])  # maybe should be (more) global?

        super(ElasticSearchSeqSource, self).__init__(metadata=metadata)
        self.npartitions = npartitions

    def _run_query(self, size=None, end=None, slice_id=None, slice_max=None):
        """Execute query on ES

        Parameters
        ----------
        size: int
            Number of objects per page
        end: int
            Cut query down to this number of results, useful for getting a
            sample
        slice_id, slice_max: int
            If given, this is one of slice_max partitions.
        """
        if size is None:
            size = self._size
        if end is not None:
            size = min(end, size)

        slice_dict = None
        if slice_id is not None:
            slice_dict = {'slice': {'id': slice_id, 'max': slice_max}}
        try:
            q = json.loads(self._query)
            if 'query' not in q:
                q = {'query': q}

            if slice_dict:
                q.update(slice_dict)
            s = self.es.search(body=q, size=size, scroll=self._scroll,
                               **self._qargs)
        except (JSONDecodeError, TypeError):
            s = self.es.search(body=slice_dict, q=self._query,
                               size=size, scroll=self._scroll,
                               **self._qargs)
        sid = s['_scroll_id']
        scroll_size = s['hits']['total']
        while scroll_size > len(s['hits']['hits']):
            page = self.es.scroll(scroll_id=sid, scroll=self._scroll)
            sid = page['_scroll_id']
            s['hits']['hits'].extend(page['hits']['hits'])
            if end is not None and len(s['hits']['hits']) > end:
                break
        self.es.clear_scroll(scroll_id=sid)
        return s

    def read(self):
        """Read all data in one go"""
        return self._get_partition()

    def to_dask(self):
        """Form partitions into a dask.bag"""
        import dask.bag as db
        from dask import delayed
        self.discover()
        parts = []
        if self.npartitions == 1:
            part = delayed(self._get_partition)()
            return db.from_delayed([part])

        for slice_id in range(self.npartitions):
            parts.append(
                delayed(self._get_partition)(slice_id))
        return db.from_delayed(parts)

    def _get_schema(self, retry=2):
        return base.Schema(datashape=None,
                           dtype=None,
                           shape=None,
                           npartitions=self.npartitions,
                           extra_metadata={})

    def _get_partition(self, partition=None):
        """
        Downloads all data or get specific partion slice of the query

        Parameters
        ----------
        partition: int or None
            If None, get all data; otherwise, get specific partition
        """
        slice_id = partition
        results = self._run_query(slice_id=slice_id, slice_max=self.npartitions)
        return [r['_source'] for r in results['hits']['hits']]
