# -*- coding: utf-8 -*-

class UpdateStrategy(object):
    def update(self, item):
        raise NotImplementedError()

class StandardStrategy(UpdateStrategy):
    def update(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
        
        item.sell_in = item.sell_in - 1
        
        if item.sell_in < 0:
            if item.quality > 0:
                item.quality = item.quality - 1

class AgedBrieStrategy(UpdateStrategy):
    def update(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        
        item.sell_in = item.sell_in - 1
        
        if item.sell_in < 0:
            if item.quality < 50:
                item.quality = item.quality + 1

class BackstagePassStrategy(UpdateStrategy):
    def update(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality = item.quality + 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality = item.quality + 1
        
        item.sell_in = item.sell_in - 1
        
        if item.sell_in < 0:
            item.quality = 0

class SulfurasStrategy(UpdateStrategy):
    def update(self, item):
        pass

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
        }
        
        default_strategy = StandardStrategy()

        for item in self.items:
            strategy = strategies.get(item.name, default_strategy)
            strategy.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


#The original code relied on a monolithic update_quality method with deeply nested conditional logic
#I implemented the Strategy Pattern, decomposing the complex conditional logic into separate classes
#Created a new strategy class rather than risking regression bugs by modifying the existing, messy if/else block.