# -*- coding: utf-8 -*-

"""
Gilded Rose Inventory Management System refactored using Strategy Design Pattern

"""

from abc import ABC, abstractmethod


class Item:
    """An item in the inventory"""
    def __init__(self, name, sell_in, quality, units="Kg", price_per_unit=1.0):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.units = units  # Optional: for future extensibility
        self.price_per_unit = price_per_unit  # Optional: for future extensibility

    def __repr__(self):
        # Return only the core fields to match expected test output  
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class UpdateStrategy(ABC):
    """Abstract base class for item update strategies"""
    
    @abstractmethod
    def update(self, item):
        """Update the item's quality and sell_in values"""
        pass
    
    def _clamp_quality(self, quality):
        """Ensure quality stays within valid bounds [0, 50]"""
        return max(0, min(50, quality))


class NormalItemStrategy(UpdateStrategy):
    """
    Strategy for normal items

    Rules:
    - Quality decreases by 1 each day
    - Quality decreases by 2 after sell_in date (when sell_in < 0)
    - Quality is never negative
    - sell_in decreases by 1 each day
    """
    
    def update(self, item):
        # Decrease sell_in by 1
        item.sell_in -= 1
        
        # Decrease quality by 1 (or 2 if past sell date)
        if item.sell_in < 0:
            item.quality -= 2  # Quality degrades twice as fast after sell date
        else:
            item.quality -= 1
        
        # Ensure quality doesn't go below 0
        item.quality = self._clamp_quality(item.quality)


class AgedBrieStrategy(UpdateStrategy):
    """
    Strategy for Aged Brie

    Rules:
    - Quality increases by 1 each day
    - Quality increases by 2 after sell_in date (when sell_in < 0)
    - Quality never exceeds 50
    - sell_in decreases by 1 each day
    """
    
    def update(self, item):
        # Decrease sell_in by 1
        item.sell_in -= 1
        
        # Increase quality by 1 (or 2 if past sell date)
        if item.sell_in < 0:
            item.quality += 2  # Quality increases twice as fast after sell date
        else:
            item.quality += 1
        
        # Ensure quality doesn't exceed 50
        item.quality = self._clamp_quality(item.quality)


class SulfurasStrategy(UpdateStrategy):
    """
    Strategy for Sulfuras, things that dont go bad

    Rules:
    - Quality never changes (stays at 80)
    - sell_in never changes (legendary items don't expire)
    """
    
    def update(self, item):
        # Legendary items don't change
        pass


class BackstagePassStrategy(UpdateStrategy):
    """
    Strategy for Backstage passes to a TAFKAL80ETC concert

    Rules:
    - Quality increases by 1 when sell_in > 10
    - Quality increases by 2 when 5 < sell_in <= 10
    - Quality increases by 3 when 0 < sell_in <= 5
    - Quality drops to 0 after the concert (sell_in < 0)
    - Quality never exceeds 50
    - sell_in decreases by 1 each day
    """
    
    def update(self, item):
        # Decrease sell_in by 1
        item.sell_in -= 1
        
        # Update quality based on days remaining
        if item.sell_in < 0:
            # Concert has passed, pass is worthless
            item.quality = 0
        elif item.sell_in < 5:
            # 5 days or less: quality increases by 3
            item.quality += 3
        elif item.sell_in < 10:
            # 10 days or less: quality increases by 2
            item.quality += 2
        else:
            # More than 10 days: quality increases by 1
            item.quality += 1
        
        # Ensure quality doesn't exceed 50
        item.quality = self._clamp_quality(item.quality)


class GildedRose(object):
    """
    Main inventory management class
    Uses the Strategy pattern to delegate item updates to specific strategies
    """
    
    def __init__(self, items):
        self.items = items
        # Map item names to their corresponding update strategies
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
        }
        # Default strategy for items not in the map
        self.default_strategy = NormalItemStrategy()

    def update_quality(self):
        """Update quality and sell_in for all items in inventory"""
        for item in self.items:
            # Get the appropriate strategy for this item
            strategy = self.strategies.get(item.name, self.default_strategy)
            # Delegate the update to the strategy
            strategy.update(item)
