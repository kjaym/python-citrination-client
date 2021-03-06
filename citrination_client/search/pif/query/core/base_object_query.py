from pypif.util.serializable import Serializable
from citrination_client.search.pif.query.core.field_operation import FieldOperation


class BaseObjectQuery(Serializable):
    """
    Base class for all PIF object queries.
    """

    def __init__(self, logic=None, extract_as=None, extract_all=None, tags=None, length=None, offset=None):
        """
        Constructor.

        :param logic: Logic for this filter. Must be equal to one of "MUST", "MUST_NOT", "SHOULD", or "OPTIONAL".
        :param extract_as: String with the alias to save this field under.
        :param extract_all: Boolean setting whether all values in an array should be extracted.
        :param tags: One or more :class:`FieldOperation` operations against the tags field.
        :param length: One or more :class:`FieldOperation` operations against the length field.
        :param offset: One or more :class:`FieldOperation` operations against the offset field.
        """
        self._logic = None
        self.logic = logic
        self._extract_as = None
        self.extract_as = extract_as
        self._extract_all = None
        self.extract_all = extract_all
        self._tags = None
        self.tags = tags
        self._length = None
        self.length = length
        self._offset = None
        self.offset = offset

    @property
    def logic(self):
        return self._logic

    @logic.setter
    def logic(self, logic):
        self._logic = logic

    @logic.deleter
    def logic(self):
        self._logic = None

    @property
    def extract_as(self):
        return self._extract_as

    @extract_as.setter
    def extract_as(self, extract_as):
        self._extract_as = extract_as

    @extract_as.deleter
    def extract_as(self):
        self._extract_as = None

    @property
    def extract_all(self):
        return self._extract_all

    @extract_all.setter
    def extract_all(self, extract_all):
        self._extract_all = extract_all

    @extract_all.deleter
    def extract_all(self):
        self._extract_all = None

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = self._get_object(FieldOperation, tags)

    @tags.deleter
    def tags(self):
        self._tags = None

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = self._get_object(FieldOperation, length)

    @length.deleter
    def length(self):
        self._length = None

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, offset):
        self._offset = self._get_object(FieldOperation, offset)

    @offset.deleter
    def offset(self):
        self._offset = None
