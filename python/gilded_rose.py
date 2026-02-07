# -*- coding: utf-8 -*-

"""
My notes on refactoring:
- The original implementation handled all item rules inside a single update_quality() method,
  which resulted in deeply nested if/else statements that were difficult to read and modify.
- To improve this, I applied the State pattern by creating a separate state class for each item type
  (Normal, Aged Brie, Backstage Pass, and Sulfuras), where each class is responsible for its own update logic.
- The Item object now delegates the update behavior to its associated state instead of containing
  conditional logic itself.
- A factory is used to determine the correct state based on the item name, keeping name-based checks
  in one place rather than scattered throughout the code.
- This refactor improves readability, testability, and makes it easier to extend the system with new
  item types without modifying existing logic, though it introduces additional classes.
"""


class GildedRose(object):
    def __init__(self, items, factory=None):
        self.items = items
        self.factory = factory or ItemStateFactory()

    def update_quality(self):
        for item in self.items:
            state = self.factory.get_state(item)
            state.update(item)


class ItemStateFactory:
    """
    Maps item names to behavior (State objects).
    Keeps name-based branching in one place.
    """
    def __init__(self):
        self.registry = {
            "Aged Brie": AgedBrieState(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassState(),
            "Sulfuras, Hand of Ragnaros": SulfurasState(),
        }
        self.defaultState = NormalItemState()

    def get_state(self, item):
        return self.registry.get(item.name, self.defaultState)


class BaseItemState:
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def update(self, item):
        raise NotImplementedError

    def inc_quality(self, item, amount=1):
        item.quality = min(self.MAX_QUALITY, item.quality + amount)

    def dec_quality(self, item, amount=1):
        item.quality = max(self.MIN_QUALITY, item.quality - amount)

    def dec_sell_in(self, item, amount=1):
        item.sell_in -= amount


class NormalItemState(BaseItemState):
    def update(self, item):
        # Before sell date: quality -1 per day
        self.dec_quality(item, 1)
        self.dec_sell_in(item, 1)

        # After sell date: quality degrades twice as fast (-2 total)
        if item.sell_in < 0:
            self.dec_quality(item, 1)


class AgedBrieState(BaseItemState):
    def update(self, item):
        # Before sell date: quality +1 per day
        self.inc_quality(item, 1)
        self.dec_sell_in(item, 1)

        # After sell date: quality increases twice as fast (+2 total)
        if item.sell_in < 0:
            self.inc_quality(item, 1)


class BackstagePassState(BaseItemState):
    def update(self, item):
        # Increase as concert approaches
        self.inc_quality(item, 1)
        if item.sell_in < 11:
            self.inc_quality(item, 1)
        if item.sell_in < 6:
            self.inc_quality(item, 1)

        self.dec_sell_in(item, 1)

        # After concert: quality drops to 0
        if item.sell_in < 0:
            item.quality = 0


class SulfurasState(BaseItemState):
    def update(self, item):
        # Legendary item: never changes
        pass


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)