#!/usr/bin/python3
""" FIFO Cache """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache Class"""

    def __init__(self):
        """intialization func"""
        super().__init__()

    def put(self, key, item):
        """ put func """
        if key is not None and item is not None:
            self.cache_data[key] = item
            max = super().MAX_ITEMS
            if len(self.cache_data) > max:
                key = list(self.cache_data.keys())[0]
                self.cache_data.pop(key)
                print(f"DISCARD: {key}")

    def get(self, key):
        """ get func """
        return self.cache_data.get(key)
