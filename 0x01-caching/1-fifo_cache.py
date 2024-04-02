#!/usr/bin/env python3
"""This module introduces the FIFOcache class responsible for
storing and deleting cache based on the FIFO caching policy.
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOcache class definition"""
    def __init__(self):
        """Initiliazing the super class to access base
        properties and methods
        """
        super().__init__()

    def put(self, key, item):
        """Sets elements to a cache and deletes the first in items from
        from the dictionary if max_items size is reached.
        """
        if key and item:
            self.cache_data[key] = item
            max_items = BaseCaching.MAX_ITEMS
            total_items = len(self.cache_data)
            if total_items > max_items:
                first = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(first))
                del self.cache_data[first]

    def get(self, key):
        """Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """
        if key:
            try:
                return self.cache_data[key]
            except KeyError:
                return
        return
