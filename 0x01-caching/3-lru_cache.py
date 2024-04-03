#!/usr/bin/env python3
"""This module introduces the LRUCachecache class responsible for
storing and deleting cache based on the LRU caching policy.
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class definition"""
    def __init__(self):
        """Initiliazing the super class to access base
        properties and methods
        """
        super().__init__()

    def put(self, key, item):
        """Sets elements to a cache and deletes the least recently used
        items from the dictionary if max_items size is reached.
        """
        if key and item:
            self.cache_data[key] = item
            max_items = BaseCaching.MAX_ITEMS
            if len(self.cache_data) > max_items:
                last = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(last))
                del self.cache_data[last]

    def get(self, key):
        """Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """
        if key:
            try:
                item = self.cache_data.pop(key)
                self.cache_data[key] = item
                return item
            except KeyError:
                return
        return
