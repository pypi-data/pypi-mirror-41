from django.conf import settings
from elasticsearch_dsl import A, Q

import functools
import operator


class Facet (object):
    field = None
    label = None
    template = getattr(settings, 'SEEKER_DEFAULT_FACET_TEMPLATE', 'seeker/facets/terms.html')

    def __init__(self, field, label=None, name=None, description=None, template=None, **kwargs):
        self.field = field
        self.label = label or self.field.replace('_', ' ').replace('.raw', '').replace('.', ' ').capitalize()
        self.name = (name or self.field).replace('.raw', '').replace('.', '_')
        self.template = template or self.template
        self.description = description
        self.kwargs = kwargs

    def apply(self, search, **extra):
        return search

    def filter(self, search, values):
        return search

    def data(self, response):
        try:
            return response.aggregations[self.name].to_dict()
        except:
            return {}

    def get_key(self, bucket):
        return bucket.get('key')

    def buckets(self, response):
        for b in self.data(response).get('buckets', []):
            yield self.get_key(b), b.get('doc_count')


class TermsFacet (Facet):

    def __init__(self, field, **kwargs):
        self.filter_operator = kwargs.pop('filter_operator', 'or')
        super(TermsFacet, self).__init__(field, **kwargs)

    def _get_aggregation(self, **extra):
        params = {'field': self.field}
        params.update(self.kwargs)
        params.update(extra)
        return A('terms', **params)

    def apply(self, search, **extra):
        search.aggs[self.name] = self._get_aggregation(**extra)
        return search

    def filter(self, search, values):
        if len(values) > 1:
            if self.filter_operator.lower() == 'and':
                filters = [Q('term', **{self.field: v}) for v in values]
                return search.query(functools.reduce(operator.and_, filters))
            else:
                return search.filter('terms', **{self.field: values})
        elif len(values) == 1:
            return search.filter('term', **{self.field: values[0]})
        return search


class GlobalTermsFacet (TermsFacet):

    def apply(self, search, **extra):
        top = A('global')
        top[self.field] = self._get_aggregation(**extra)
        search.aggs[self.field] = top
        return search

    def data(self, response):
        return response.aggregations[self.field][self.field].to_dict()


class YearHistogram (Facet):
    template = 'seeker/facets/year_histogram.html'

    def apply(self, search, **extra):
        params = {
            'field': self.field,
            'interval': 'year',
            'format': 'yyyy',
            'min_doc_count': 1,
            'order': {'_key': 'desc'},
        }
        params.update(self.kwargs)
        params.update(extra)
        search.aggs[self.name] = A('date_histogram', **params)
        return search

    def filter(self, search, values):
        filters = []
        for val in values:
            kw = {
                self.field: {
                    'gte': '%s-01-01T00:00:00' % val,
                    'lte': '%s-12-31T23:59:59' % val,
                }
            }
            filters.append(Q('range', **kw))
        return search.query(functools.reduce(operator.or_, filters))

    def get_key(self, bucket):
        return bucket.get('key_as_string')


class RangeFilter (Facet):
    template = 'seeker/facets/range.html'

    def filter(self, search, values):
        if len(values) == 2:
            r = {}
            if values[0].isdigit():
                r['gte'] = values[0]
            if values[1].isdigit():
                r['lte'] = values[1]
            search = search.filter('range', **{self.field: r})
        return search
