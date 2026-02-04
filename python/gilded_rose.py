# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Strategy Pattern Implementation
class UpdateStrategy:
    def update(self, item):
        pass
    
    def clamp_quality(self, item, min_val=0, max_val=50):
        item.quality = max(min_val, min(max_val, item.quality))


class NormalItemStrategy(UpdateStrategy):
    def update(self, item):
        if item.sell_in <= 0:
            item.quality -= 2
        else:
            item.quality -= 1
        item.sell_in -= 1
        self.clamp_quality(item)


class AgedBrieStrategy(UpdateStrategy):
    def update(self, item):
        if item.sell_in <= 0:
            item.quality += 2
        else:
            item.quality += 1
        item.sell_in -= 1
        self.clamp_quality(item)


class SulfurasStrategy(UpdateStrategy):
    def update(self, item):
        # Legendary item never changes
        pass


class BackstagePassStrategy(UpdateStrategy):
    def update(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        else:
            if item.sell_in <= 5:
                item.quality += 3
            elif item.sell_in <= 10:
                item.quality += 2
            else:
                item.quality += 1
        item.sell_in -= 1
        self.clamp_quality(item)


class ConjuredItemStrategy(UpdateStrategy):
    def update(self, item):
        if item.sell_in <= 0:
            item.quality -= 4
        else:
            item.quality -= 2
        item.sell_in -= 1
        self.clamp_quality(item)


# Factory Pattern
class StrategyFactory:
    @staticmethod
    def get_strategy(item):
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif "Sulfuras" in item.name:
            return SulfurasStrategy()
        elif "Backstage passes" in item.name:
            return BackstagePassStrategy()
        elif "Conjured" in item.name:
            return ConjuredItemStrategy()
        else:
            return NormalItemStrategy()


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = StrategyFactory.get_strategy(item)
            strategy.update(item)