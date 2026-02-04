# -*- coding: utf-8 -*-

from item_updaters import(
    ItemUpdater,
    SulfurasUpdater,
    NormalItemUpdater,
    AgedBrieUpdater,
    BackstagePassUpdater,
    ConjuredUpdater,
)

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self._default_updater = NormalItemUpdater()
        self._updaters = {
            AGED_BRIE: AgedBrieUpdater(),
            BACKSTAGE_PASSES: BackstagePassUpdater(),
            SULFURAS: SulfurasUpdater(),
        }
        self._conjured_updater = ConjuredUpdater()

    def update_quality(self):
        for item in self.items:
            updater = self._get_updater(item)
            updater.update(item)

    def _get_updater(self, item) -> ItemUpdater:
        if item.name in self._updaters:
            return self._updaters[item.name]
        if item.name.startswith("Conjured"):
            return self._conjured_updater
        return self._default_updater


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
