# -*- coding: utf-8 -*-

from strategies import NormalItem, AgedBrie, Backstage, Sulfuras, Conjured


class StrategyFactory:
    """This is a factory class that creates the appropriate update strategy for an item."""
    
    # to avoid hardcoded strings
    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    CONJURED_PREFIX = "Conjured"
    
    def create_strategy(self, item):
        """This method is used to create and return the appropriate strategy for the given item.
        
        Args:
            item: The item to create a strategy for
            
        Returns:
            An instance of ItemUpdateStrategy appropriate for the item
        """
        if item.name == self.AGED_BRIE:
            return AgedBrie()
        elif item.name == self.SULFURAS:
            return Sulfuras()
        elif item.name == self.BACKSTAGE_PASSES:
            return Backstage()
        elif item.name.startswith(self.CONJURED_PREFIX):
            return Conjured()
        else:
            return NormalItem()
