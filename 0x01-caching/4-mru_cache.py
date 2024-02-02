#!/usr/bin/python3
""" MRU Cache """
from collections import OrderedDict, deque


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache Class"""

    def __init__(self):
        """intialization func"""
        super().__init__()
        self.cache_data = OrderedDict()
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
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
        return None
