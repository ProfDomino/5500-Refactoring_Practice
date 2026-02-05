# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
class UpdateStrategy(ABC):
    """
    Base class for item update strategies.
Each item type has its own strategy for updating quality and sell_in. 
    """
    @abstractmethod
    def update(self, item):
        """Update the item's quality and sell_in values."""
        pass
    
    def _decrease_quality(self, item, amount=1):
        """Helper method to decrease quality, ensuring it does not fall below 0."""
        item.quality = max(0, item.quality - amount)
    
    def _increase_quality(self, item, amount=1):
        """Helper method to increase quality, ensuring it does not exceed 50."""
        item.quality = min(50, item.quality + amount)
    
    def _decrease_sell_in(self, item):
        """Helper method to decrease sell_in by 1."""
        item.sell_in -= 1


class NormalItemStrategy(UpdateStrategy):
    """
    Normal items Strategy:
    - Quality decreases by 1 each day
    - Quality decreases by 2 after sell_in date
    - Sell_in decreases by 1 each day
    """
    def update(self, item):
        self._decrease_sell_in(item)
        if item.sell_in < 0:
            self._decrease_quality(item, amount=2)
        else:
            self._decrease_quality(item, amount=1)


class AgedBrieStrategy(UpdateStrategy):
    """
    Aged Brie Strategy:
    - Quality increases by 1 each day
    - Quality increases by 2 after sell_in date
    - Sell_in decreases by 1 each day
    """
    def update(self, item):
        self._decrease_sell_in(item) 
        if item.sell_in < 0:
            self._increase_quality(item, amount=2)
        else:
            self._increase_quality(item, amount=1)


class BackstagePassStrategy(UpdateStrategy):
    """
    Backstage passes Strategy:
    - Sell_in decreases by 1 each day (happens first)
    - Quality increases by 1 when sell_in >= 10 (after decrement)
    - Quality increases by 2 when 5 <= sell_in < 10 (after decrement)
    - Quality increases by 3 when 0 <= sell_in < 5 (after decrement)
    - Quality drops to 0 after the concert (sell_in < 0)
    """
    
    def update(self, item):
        self._decrease_sell_in(item)
        
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            self._increase_quality(item, amount=3)
        elif item.sell_in < 10:
            self._increase_quality(item, amount=2)
        else:
            self._increase_quality(item, amount=1)


class SulfurasStrategy(UpdateStrategy):
    """
    Strategy for Sulfuras (Legendary item):
    Quality never changes (always 80)
    Sell_in never changes
    """
    
    def update(self, item):
        # Legendary items never change
        pass


class ConjuredStrategy(UpdateStrategy):
    """
    Conjured items Strategy:
    NOTE: Preserves original behavior (which was buggy - treated like normal items)
    - Quality decreases by 1 each day (original behavior, not the 2x requirement)
    - Quality decreases by 2 after sell_in date
    - Sell_in decreases by 1 each day
    """
    
    def update(self, item):
        self._decrease_sell_in(item)
        
        # Matching original buggy behavior to preserve existing functionality
        if item.sell_in < 0:
            self._decrease_quality(item, amount=2)
        else:
            self._decrease_quality(item, amount=1)


class StrategyFactory:
    """Factory class to map item names to their appropriate update strategies."""
    @staticmethod
    def get_strategy(item_name):
        """
        Returns the appropriate strategy based on item name.
        
        Args:
            item_name: The name of the item  
        Returns:
            UpdateStrategy: The appropriate strategy for the item
        """
        strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Conjured Mana Cake": ConjuredStrategy(),
        }
        # Check for conjured items (items starting with "Conjured")
        if item_name.startswith("Conjured"):
            return ConjuredStrategy()
        
        # Return specific strategy or default to normal item strategy
        return strategies.get(item_name, NormalItemStrategy())


class GildedRose(object):
    """
    Inventory management system for the Gilded Rose inn.
    Uses Strategy Pattern to handle different item types.
    """
    
    def __init__(self, items):
        self.items = items
        self.strategy_factory = StrategyFactory()

    def update_quality(self):
        """
        Updates the quality and sell_in values for all items.
        Delegates to appropriate strategy for each item type.
        """
        for item in self.items:
            strategy = self.strategy_factory.get_strategy(item.name)
            strategy.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
