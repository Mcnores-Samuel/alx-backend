#!/usr/bin/env python3
"""This module introduces the LIFOcache class responsible for
storing and deleting cache based on the LIFO caching policy.
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """FIFOcache class definition"""
    def __init__(self):
        """Initiliazing the super class to access base
        properties and methods
        """
        super().__init__()

    def put(self, key, item):
        """Sets elements to a cache and deletes the last in items from
        from the dictionary if max_items size is reached.
        """
        if key and item:
            self.cache_data[key] = item
            max_items = BaseCaching.MAX_ITEMS
            if len(self.cache_data) > max_items:
                last = list(self.cache_data.keys())[-2]
                print('DISCARD: {}'.format(last))
                del self.cache_data[last]

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


my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
