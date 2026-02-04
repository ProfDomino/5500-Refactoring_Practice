# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Item:
    """Original Item class - DO NOT MODIFY (goblin will rage)"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Updateable(ABC):
    """Interface to enforce updateQuality method"""
    @abstractmethod
    def update_quality(self):
        pass


class ItemWrapper(Updateable):
    """Abstract wrapper using composition over inheritance"""
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, name, sell_in, quality):
        self._item = Item(name, sell_in, quality)

    def get_quality(self):
        return self._item.quality

    def get_name(self):
        return self._item.name

    def get_sell_in(self):
        return self._item.sell_in

    def get_item(self):
        return self._item

    def set_sell_in(self):
        self._item.sell_in -= 1

    def compute_quality(self, delta):
        """Check boundary and adjust quality within valid range"""
        new_quality = self._item.quality + delta
        if new_quality > self.MAX_QUALITY:
            self._item.quality = self.MAX_QUALITY
        elif new_quality < self.MIN_QUALITY:
            self._item.quality = self.MIN_QUALITY
        else:
            self._item.quality = new_quality

    @abstractmethod
    def update_quality(self):
        pass

    def __repr__(self):
        return repr(self._item)


class NormalItem(ItemWrapper):
    """Standard item - degrades by 1, or 2 after sell date"""
    def update_quality(self):
        if self.get_sell_in() > 0:
            # Before sell date, decreases quality normally
            self.compute_quality(-1)
        else:
            # After sell date, decreases quality faster
            self.compute_quality(-2)
        self.set_sell_in()


class AgedItem(ItemWrapper):
    """Like Aged Brie - increases in quality over time"""
    def update_quality(self):
        if self.get_sell_in() > 0:
            # Before sell date, increases quality normally
            self.compute_quality(1)
        else:
            # After sell date, increases quality faster
            self.compute_quality(2)
        self.set_sell_in()


class BackstageItem(ItemWrapper):
    """Like Backstage passes - increases, then drops to 0 after concert"""
    def update_quality(self):
        if self.get_sell_in() <= 0:
            # After concert, quality drops to 0
            self._item.quality = 0
        elif self.get_sell_in() <= 5:
            # Increases by 3 when 5 days or less
            self.compute_quality(3)
        elif self.get_sell_in() <= 10:
            # Increases by 2 when 10 days or less
            self.compute_quality(2)
        else:
            # Increases by 1 otherwise
            self.compute_quality(1)
        self.set_sell_in()


class LegendItem(ItemWrapper):
    """Like Sulfuras - never changes, quality always 80"""
    LEGENDARY_QUALITY = 80

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, self.LEGENDARY_QUALITY)

    def update_quality(self):
        # Legendary items never change
        pass


class ConjuredItem(ItemWrapper):
    """Conjured items - degrade twice as fast as normal"""
    def update_quality(self):
        if self.get_sell_in() > 0:
            # Before sell date, decreases quality twice as fast
            self.compute_quality(-2)
        else:
            # After sell date, decreases quality four times as fast
            self.compute_quality(-4)
        self.set_sell_in()


class GildedRose:
    """Main class that manages inventory"""
    def __init__(self, items=None):
        self._items = items if items else []

    def items(self):
        return [wrapper.get_item() for wrapper in self._items]

    def add_item(self, item: Updateable):
        self._items.append(item)

    def update_quality(self):
        for item in self._items:
            item.update_quality()

    def __repr__(self):
        return "\n".join(str(item) for item in self._items)


# Factory function to create the right wrapper based on item name
def create_item(name, sell_in, quality):
    """Factory to create appropriate item wrapper"""
    if name == "Aged Brie":
        return AgedItem(name, sell_in, quality)
    elif name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstageItem(name, sell_in, quality)
    elif name == "Sulfuras, Hand of Ragnaros":
        return LegendItem(name, sell_in, quality)
    elif name.startswith("Conjured"):
        return ConjuredItem(name, sell_in, quality)
    else:
        return NormalItem(name, sell_in, quality)