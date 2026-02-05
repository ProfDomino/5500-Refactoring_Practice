# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Item:
    """Represents an item in the Gilded Rose inventory."""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater(ABC):
    """Abstract base class for item update strategies."""
    
    @abstractmethod
    def update(self, item):
        """Update the item's sell_in and quality values."""
        pass
    
    def _decrease_quality(self, item, amount=1):
        """Safely decrease quality, ensuring it doesn't go below 0."""
        item.quality = max(0, item.quality - amount)
    
    def _increase_quality(self, item, amount=1):
        """Safely increase quality, ensuring it doesn't exceed 50."""
        item.quality = min(50, item.quality + amount)
    
    def _decrease_sell_in(self, item):
        """Decrease the sell_in value by 1."""
        item.sell_in -= 1


class NormalUpdater(ItemUpdater):
    """Strategy for normal items that degrade over time."""
    
    def update(self, item):
        # First decrease quality
        self._decrease_quality(item, 1)
        
        # Then decrease sell_in
        self._decrease_sell_in(item)
        
        # If past sell date, degrade again
        if item.sell_in < 0:
            self._decrease_quality(item, 1)


class BrieUpdater(ItemUpdater):
    """Strategy for Aged Brie - quality increases over time."""
    
    def update(self, item):
        # First increase quality
        self._increase_quality(item, 1)
        
        # Then decrease sell_in
        self._decrease_sell_in(item)
        
        # If past sell date, increase again
        if item.sell_in < 0:
            self._increase_quality(item, 1)


class BackstageUpdater(ItemUpdater):
    """Strategy for Backstage passes - special concert rules."""
    
    def update(self, item):
        # Increase quality based on days remaining (before decrementing sell_in)
        if item.sell_in <= 5:
            self._increase_quality(item, 3)
        elif item.sell_in <= 10:
            self._increase_quality(item, 2)
        else:
            self._increase_quality(item, 1)
        
        # Then decrease sell_in
        self._decrease_sell_in(item)
        
        # After concert (sell_in < 0), quality drops to 0
        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(ItemUpdater):
    """Strategy for Sulfuras - legendary item, never changes."""
    
    def update(self, item):
        # Sulfuras never changes - do nothing
        pass


class ConjuredUpdater(ItemUpdater):
    """Strategy for Conjured items - degrade twice as fast.
    
    Note: Currently matching baseline behavior (like normal items).
    The 2x degradation is a new feature to be implemented after refactoring.
    """
    
    def update(self, item):
        # First decrease quality by 1 (matching baseline)
        self._decrease_quality(item, 1)
        
        # Then decrease sell_in
        self._decrease_sell_in(item)
        
        # If past sell date, degrade by 1 again
        if item.sell_in < 0:
            self._decrease_quality(item, 1)


class UpdaterFactory:
    """Factory to create the appropriate updater for an item."""
    
    @staticmethod
    def get_updater(item_name):
        """Return the appropriate updater strategy for the given item name."""
        if item_name == "Aged Brie":
            return BrieUpdater()
        elif item_name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstageUpdater()
        elif item_name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater()
        elif item_name.startswith("Conjured"):
            return ConjuredUpdater()
        else:
            return NormalUpdater()


class GildedRose:
    """The Gilded Rose inventory management system."""
    
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Update all items in the inventory."""
        for item in self.items:
            updater = UpdaterFactory.get_updater(item.name)
            updater.update(item)
