#!/usr/bin/python3
""" LFU Cache """
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LRU Cache Class"""

    def __init__(self):
        """intialization func"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.count = {}

    def put(self, key, item):
        """ put func """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.count[key] = self.count.get(key, 0) + 1

            if len(self.cache_data) > self.MAX_ITEMS:
                min_count = min(self.count.values())
                min_keys = [k for k, v in self.count.items() if v == min_count]

                if len(min_keys) == 1:
                    key_to_remove = min_keys[0]
                else:
                    key_to_remove = min(min_keys,
                                        key=lambda k: list(
                                            self.cache_data.keys()).index(k))

                del self.cache_data[key_to_remove]
                del self.count[key_to_remove]
                print(f"DISCARD: {key_to_remove}")

    def get(self, key):
        """ get func """
        if key in self.cache_data:
            self.count[key] = self.count.get(key, 0) + 1
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
