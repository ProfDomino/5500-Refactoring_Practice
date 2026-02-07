# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Strategy Interface
class UpdateStrategy:
    """Base strategy interface for item updates"""
    
    def update(self, item):
        """Update both quality and sell_in for an item"""
        raise NotImplementedError("Subclasses must implement update method")


# Concrete Strategies
class NormalItemStrategy(UpdateStrategy):
    """Strategy for normal items that degrade in quality"""
    
    def update(self, item):
        # Decrease quality by 1
        if item.quality > 0:
            item.quality -= 1
        
        # Decrease sell_in
        item.sell_in -= 1
        
        # After sell date, degrade twice as fast
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieStrategy(UpdateStrategy):
    """Strategy for Aged Brie that increases in quality over time"""
    
    def update(self, item):
        # Increase quality by 1 (max 50)
        if item.quality < 50:
            item.quality += 1
        
        # Decrease sell_in
        item.sell_in -= 1
        
        # After sell date, increase quality twice as fast
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class SulfurasStrategy(UpdateStrategy):
    """Strategy for Sulfuras (legendary item) - never changes"""
    
    def update(self, item):
        # Sulfuras never decreases in quality or sell_in
        pass


class BackstagePassStrategy(UpdateStrategy):
    """Strategy for Backstage passes that increase in value as concert approaches"""
    
    def update(self, item):
        # Increase quality based on days until concert
        if item.quality < 50:
            item.quality += 1
            
            # 10 days or less: +1 additional quality
            if item.sell_in <= 10 and item.quality < 50:
                item.quality += 1
            
            # 5 days or less: +1 more additional quality
            if item.sell_in <= 5 and item.quality < 50:
                item.quality += 1
        
        # Decrease sell_in
        item.sell_in -= 1
        
        # After concert, quality drops to 0
        if item.sell_in < 0:
            item.quality = 0


class ConjuredItemStrategy(UpdateStrategy):
    """Strategy for Conjured items that degrade twice as fast as normal items"""
    
    def update(self, item):
        # Decrease quality by 2
        if item.quality > 0:
            item.quality -= 2
            if item.quality < 0:
                item.quality = 0
        
        # Decrease sell_in
        item.sell_in -= 1
        
        # After sell date, degrade twice as fast (4 total per day)
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2
            if item.quality < 0:
                item.quality = 0


class GildedRose:
    """Main class that manages items and applies update strategies"""
    
    def __init__(self, items):
        self.items = items
        # Dictionary mapping item names to their strategies
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Conjured Mana Cake": ConjuredItemStrategy(),
        }
    
    def get_strategy(self, item_name):
        """Get the appropriate strategy for an item"""
        # Check if item name starts with "Conjured"
        if item_name.startswith("Conjured"):
            return ConjuredItemStrategy()
        
        # Return specific strategy or default to NormalItemStrategy
        return self.strategies.get(item_name, NormalItemStrategy())
    
    def update_quality(self):
        """Update quality for all items using their respective strategies"""
        for item in self.items:
            strategy = self.get_strategy(item.name)
            strategy.update(item)