# -*- coding: utf-8 -*-
"""
Gilded Rose Refactoring - Strategy Pattern Implementation
Author: Pooja Malakappa Nuchchi
"""

from abc import ABC, abstractmethod


# ==================== ITEM CLASS (UNCHANGED) ====================
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# ==================== STRATEGY INTERFACE ====================
class UpdateStrategy(ABC):
    """Abstract Strategy: Defines interface for all update behaviors."""
    
    MAX_QUALITY = 50
    MIN_QUALITY = 0
    
    @abstractmethod
    def update(self, item: Item) -> None:
        """Update the item's sell_in and quality values."""
        pass
    
    def _decrease_quality(self, item: Item, amount: int = 1) -> None:
        """Safely decrease quality (minimum 0)."""
        item.quality = max(self.MIN_QUALITY, item.quality - amount)
    
    def _increase_quality(self, item: Item, amount: int = 1) -> None:
        """Safely increase quality (maximum 50)."""
        item.quality = min(self.MAX_QUALITY, item.quality + amount)
    
    def _is_expired(self, item: Item) -> bool:
        """Check if item is past its sell date."""
        return item.sell_in < 0


# ==================== CONCRETE STRATEGIES ====================
class NormalItemStrategy(UpdateStrategy):
    """Strategy for normal/standard items."""
    
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        degradation = 2 if self._is_expired(item) else 1
        self._decrease_quality(item, degradation)


class AgedBrieStrategy(UpdateStrategy):
    """Strategy for Aged Brie - quality INCREASES over time."""
    
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        increase = 2 if self._is_expired(item) else 1
        self._increase_quality(item, increase)


class BackstagePassStrategy(UpdateStrategy):
    """Strategy for Backstage Passes - complex quality rules."""
    
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        
        if self._is_expired(item):
            item.quality = 0
        elif item.sell_in < 5:
            self._increase_quality(item, 3)
        elif item.sell_in < 10:
            self._increase_quality(item, 2)
        else:
            self._increase_quality(item, 1)


class SulfurasStrategy(UpdateStrategy):
    """Strategy for Sulfuras (Legendary Item) - never changes."""
    
    def update(self, item: Item) -> None:
        pass  # Sulfuras never changes


# NOTE: Conjured items are NOT implemented in the original code.
# The original code treats them as normal items.
# This strategy matches the original behavior for TextTest compatibility.
class ConjuredItemStrategy(UpdateStrategy):
    """Strategy for Conjured items - currently same as normal items."""
    
    def update(self, item: Item) -> None:
        # Original code treats Conjured as normal items
        item.sell_in -= 1
        degradation = 2 if self._is_expired(item) else 1
        self._decrease_quality(item, degradation)


# ==================== MAIN CLASS ====================
class GildedRose:
    """Context: Uses strategies to update items."""
    
    STRATEGY_MAP = {
        "Aged Brie": AgedBrieStrategy(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
        "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
        # Conjured not in map - will use default (normal) strategy
    }
    
    DEFAULT_STRATEGY = NormalItemStrategy()
    
    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            strategy = self._get_strategy(item)
            strategy.update(item)
    
    def _get_strategy(self, item: Item) -> UpdateStrategy:
        """Get the appropriate strategy for an item."""
        return self.STRATEGY_MAP.get(item.name, self.DEFAULT_STRATEGY)
