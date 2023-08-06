__version__ = '3.0.1'

from .facets import Facet, GlobalTermsFacet, RangeFilter, TermsFacet, YearHistogram
from .mapping import (
    DEFAULT_ANALYZER, Indexable, ModelIndex, RawMultiString, RawString, build_mapping, deep_field_factory,
    document_field, document_from_model)
from .registry import app_documents, documents, model_documents, register
from .utils import delete, index, search
from .views import Column, SeekerView


default_app_config = 'seeker.apps.SeekerConfig'
