# -*- coding: utf-8 -*-

from item import Item
from strategy_factory import StrategyFactory


class GildedRose(object):
    """This is the main class for managing Gilded Rose inventory."""

    def __init__(self, items):
        """This method is used to initialize the GildedRose with a list of items.
        
        Args:
            items: List of Item objects to manage
        """
        self.items = items
        self.strategy_factory = StrategyFactory()

    def update_quality(self):
        """This method is used to update the quality and sell_in for all items in the inventory.
        
        It uses the Strategy Pattern to delegate the update logic to
        item-specific strategy classes.
        """
        for item in self.items:
            strategy = self.strategy_factory.create_strategy(item)
            strategy.update(item)
