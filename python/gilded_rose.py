# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater(ABC):
    def __init__(self, item):
        self.item = item
    
    def update(self):
        self.item.sell_in -= 1
        self.item.quality += self.quality_delta()
        if self.item.sell_in < 0:
            self.item.quality += self.expired_delta()
        self.item.quality = max(0, min(50, self.item.quality))
    
    @abstractmethod
    def quality_delta(self):
        pass
    
    def expired_delta(self):
        return 0


class NormalItemUpdater(ItemUpdater):
    def quality_delta(self):
        return -1
    
    def expired_delta(self):
        return -1


class AgedBrieUpdater(ItemUpdater):
    def quality_delta(self):
        return 1
    
    def expired_delta(self):
        return 1


class SulfurasUpdater(ItemUpdater):
    def quality_delta(self):
        return 0
    
    def update(self):
        self.item.quality = 80


class BackstagePassUpdater(ItemUpdater):
    def quality_delta(self):
        if self.item.sell_in > 10:
            return 1
        return 2 if self.item.sell_in > 5 else 3
    
    def expired_delta(self):
        return -self.item.quality


class GildedRose:
    UPDATERS = {
        "Aged Brie": AgedBrieUpdater,
        "Sulfuras, Hand of Ragnaros": SulfurasUpdater,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater
    }
    
    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            self.UPDATERS.get(item.name, NormalItemUpdater)(item).update()