#!/usr/bin/env python3
"""This module contains a BasicCache which inherits
from BaseCaching class and is a caching system.
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class definition"""

    def __init__(self):
        """Initiliazing access to the super class"""
        super().__init__()

    def put(self, key, item):
        """Sets a key and value pair to the cache data property"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key."""
        if key:
            try:
                return self.cache_data[key]
            except KeyError:
                return
        return
