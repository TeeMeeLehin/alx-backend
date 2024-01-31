#!/usr/bin/python3
""" LRU Cache """
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache Class"""

    def __init__(self):
        """intialization func"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ put func """
        if key is not None and item is not None:
            self.cache_data[key] = item
            max = super().MAX_ITEMS
            if len(self.cache_data) > max:
                key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {key}")

    def get(self, key):
        """ get func """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
