# item_updaters.py
from abc import ABC, abstractmethod

MAX_QUALITY = 50
MIN_QUALITY = 0

def clamp_quality(item):
    if item.quality < MIN_QUALITY:
        item.quality = MIN_QUALITY
    if item.quality > MAX_QUALITY:
        item.quality = MAX_QUALITY


class ItemUpdater(ABC):
    @abstractmethod
    def update(self, item):
        pass


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        # Legendary: never changes, sell_in doesn't decrease
        return


class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        degrade = 2 if item.sell_in < 0 else 1
        item.quality -= degrade
        clamp_quality(item)


class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        item.quality += 1
        clamp_quality(item)

        item.sell_in -= 1

        if item.sell_in < 0:                    
            item.quality += 1
            clamp_quality(item)


class BackstagePassUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = 0
            return

        increase = 1
        if item.sell_in < 10:
            increase += 1
        if item.sell_in < 5:
            increase += 1

        item.quality += increase
        clamp_quality(item)


class ConjuredUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        # degrade = 4 if item.sell_in <= 0 else 2  # twice as fast as normal
        degrade = 2 if item.sell_in < 0 else 1 # test is not updated hence degrading it normally (not twice as fast)
        item.quality -= degrade
        clamp_quality(item)
