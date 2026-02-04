# -*- coding: utf-8 -*-

# Base strategy interface for updating items
class UpdateStrategy:
    # Default update method to be overridden by subclasses
    def update(self, item):
        pass


# Strategy for normal items that degrade in quality over time
class NormalStrategy(UpdateStrategy):
    # Decreases quality by 1, or by 2 after sell date
    def update(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality = item.quality - 1


# Strategy for Aged Brie which increases in quality over time
class AgedBrieStrategy(UpdateStrategy):
    # Increases quality by 1, or by 2 after sell date
    def update(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality = item.quality + 1


# Strategy for Backstage passes with tiered quality increases
class BackstageStrategy(UpdateStrategy):
    # Quality increases faster as concert approaches, drops to 0 after
    def update(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality = item.quality + 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0


# Strategy for Sulfuras legendary item that never changes
class SulfurasStrategy(UpdateStrategy):
    # Does nothing as Sulfuras never degrades or needs to be sold
    def update(self, item):
        pass


# Strategy for Conjured items that degrade twice as fast
class ConjuredStrategy(UpdateStrategy):
    # Decreases quality by 2, or by 4 after sell date
    def update(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality = item.quality - 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality = item.quality - 1


# Main class that manages inventory and applies update strategies
class GildedRose(object):
    # Initializes with items list and maps item types to strategies
    def __init__(self, items):
        self.items = items
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstageStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Conjured": ConjuredStrategy()
        }

    # Updates quality for all items using their respective strategies
    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item)
            strategy.update(item)

    # Returns the appropriate strategy based on item name
    def get_strategy(self, item):
        if item.name in self.strategies:
            return self.strategies[item.name]
        if item.name.startswith("Conjured"):
            return self.strategies["Conjured"]
        return NormalStrategy()


# Represents an item with name, sell_in days, and quality value
class Item:
    # Initializes item with name, sell_in, and quality attributes
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    # Returns string representation of the item
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
