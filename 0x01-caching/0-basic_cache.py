#!/usr/bin/python3
""" Basic Cache """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache Class"""

    def __init__(self):
        """intialization func"""
        super().__init__()

    def put(self, key, item):
        """ put func """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get func """
        return self.cache_data.get(key)
