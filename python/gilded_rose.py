# -*- coding: utf-8 -*-
from strategies import (
    NormalItemStrategy,
    AgedBrieStrategy,
    BackstagePassStrategy,
    SulfurasStrategy,
    ConjuredItemStrategy
)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _get_strategy(self, item):
        """Pick the right strategy based on item name"""
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassStrategy()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        elif item.name.startswith("Conjured"):
            return ConjuredItemStrategy()
        else:
            return NormalItemStrategy()

    def update_quality(self):
        for item in self.items:
            strategy = self._get_strategy(item)
            strategy.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
