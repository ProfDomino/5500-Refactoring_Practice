# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class UpdateStrategy(ABC):
    
    @abstractmethod
    def update(self, item):
        pass


class NormalItemStrategy(UpdateStrategy):
    
    def update(self, item):
        # decrease sell_in
        item.sell_in -= 1
        
        # decrease quality
        if item.quality > 0:
            item.quality -= 1
        
        # after sell date, quality degrades twice as fast
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieStrategy(UpdateStrategy):
    
    def update(self, item):
        item.sell_in -= 1
        
        # increases in quality
        if item.quality < 50:
            item.quality += 1
        
        # after sell date, increases even faster
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class BackstagePassStrategy(UpdateStrategy):
    
    def update(self, item):
        item.sell_in -= 1
        
        if item.sell_in < 0:
            # concert is over, worthless
            item.quality = 0
        elif item.sell_in < 5:
            # 5 days or less, +3 quality
            if item.quality < 50:
                item.quality += 3
                if item.quality > 50:
                    item.quality = 50
        elif item.sell_in < 10:
            # 10 days or less, +2 quality
            if item.quality < 50:
                item.quality += 2
                if item.quality > 50:
                    item.quality = 50
        else:
            # more than 10 days, +1 quality
            if item.quality < 50:
                item.quality += 1


class SulfurasStrategy(UpdateStrategy):
    
    def update(self, item):
        # sulfuras never changes
        pass


class ConjuredItemStrategy(UpdateStrategy):
    
    def update(self, item):
        item.sell_in -= 1
        
        # degrades twice as fast as normal
        if item.quality > 0:
            item.quality -= 2
            if item.quality < 0:
                item.quality = 0
        
        # after sell date, degrades even faster
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2
            if item.quality < 0:
                item.quality = 0
