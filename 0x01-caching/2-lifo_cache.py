#!/usr/bin/python3
""" LIFO Cache """
from collections import deque


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache Class"""

    def __init__(self):
        """intialization func"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ put func """
        if key is not None and item is not None:
            if len(self.cache_data) == super().MAX_ITEMS:
                l_key = self.queue.pop()
                self.cache_data.pop(l_key)
                print(f"DISCARD: {l_key}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ get func """
        return self.cache_data.get(key)
