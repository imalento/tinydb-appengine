# -*- coding: utf-8 -*-

from tinydb import TinyDB, where

from tinydb_appengine.storages import EphemeralJSONStorage


def test_readwrite():
    """
    Test Readonly JSON
    """

    test_file = 'test/test.json'
    item1 = {'name': 'Value A'}
    ephemeral = TinyDB(test_file, storage=EphemeralJSONStorage)

    def get(s):
        return ephemeral.get(where('name') == s)

    assert get('Value A') == item1
    assert get('Value B') is None

    ephemeral.remove(where('name') == 'Value A')
    assert get('Value A') is None

    item2 = {'name': 'Value B'}
    ephemeral.insert(item2)
    assert get('Value B') == item2

    ephemeral.remove(where('name') == 'Value B')
    assert get('Value B') is None

    ephemeral.close()

    ephemeral = TinyDB(test_file, storage=EphemeralJSONStorage)
    assert get('Value A') == item1
    assert get('Value B') is None
    ephemeral.close()


def test_empty_file():
    """
    Test empty file
    """
    empty_file = 'test/empty.json'
    ephemeral = TinyDB(empty_file, storage=EphemeralJSONStorage)
    assert ephemeral.get(where('name') == 'Value A') is None
    ephemeral.close()
