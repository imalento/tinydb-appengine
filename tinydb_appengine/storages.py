# -*- coding: utf-8 -*-
import codecs

from tinydb.storages import JSONStorage


class EphemeralJSONStorage(JSONStorage):
    """
    Use JSON file readonly.
    """

    def __init__(self, path, encoding=None, **kwargs):
        """
        Create a new instance.

        :param path: Where to store the JSON data.
        :type path: str
        """
        self.kwargs = kwargs
        self._handle = codecs.open(path, 'r', encoding=encoding)
        self.memory = None

    def read(self):
        if self.memory is not None:
            return self.memory
        self.memory = super(EphemeralJSONStorage, self).read()
        return self.memory

    def write(self, data):
        self.memory = data
