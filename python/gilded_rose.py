# -*- coding: utf-8 -*-


"""
My notes on refactoring:
- so instead of having a single method for updating quality with multiple nested if-else conditions, 
    what i am doing is writing separate methods for each type of item and then calling the appropriate method based on the item name.
    This way, each method is responsible for handling the specific rules for that item type.
- Alos added constants for item names and quality limits to avoid hardcoding strings and numbers multiple times
"""


# Constants
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured"
MAX_QUALITY = 50
MIN_QUALITY = 0
BACKSTAGE_THRESHOLD_HIGH = 11
BACKSTAGE_THRESHOLD_LOW = 6


def update_default_item(item):
    item.sell_in -= 1
    if item.quality > MIN_QUALITY:
        item.quality -= 1
    if item.sell_in < MIN_QUALITY and item.quality > MIN_QUALITY:
        item.quality -= 1


def update_sulfuras(item):
    pass  # Sulfuras never gets updated


def update_conjured_item(item):
    item.sell_in -= 1
    if item.quality > MIN_QUALITY:
        item.quality -= 2
        if item.quality < MIN_QUALITY:
            item.quality = MIN_QUALITY
    if item.sell_in < MIN_QUALITY and item.quality > MIN_QUALITY:
        item.quality -= 2
        if item.quality < MIN_QUALITY:
            item.quality = MIN_QUALITY


def update_brie(item):
    item.sell_in -= 1
    if item.quality < MAX_QUALITY:
        item.quality += 1
    if item.sell_in < MIN_QUALITY and item.quality < MAX_QUALITY:
        item.quality += 1


def update_backstage_pass(item):
    if item.quality < MAX_QUALITY:
        item.quality += 1
        if item.sell_in < BACKSTAGE_THRESHOLD_HIGH and item.quality < MAX_QUALITY:
            item.quality += 1
        if item.sell_in < BACKSTAGE_THRESHOLD_LOW and item.quality < MAX_QUALITY:
            item.quality += 1
    item.sell_in -= 1
    if item.sell_in < MIN_QUALITY:
        item.quality = MIN_QUALITY


def get_specific_update_method(item_name):
    if item_name == SULFURAS:
        return update_sulfuras
    elif item_name == AGED_BRIE:
        return update_brie
    elif item_name == BACKSTAGE_PASSES:
        return update_backstage_pass
    elif item_name.startswith(CONJURED):
        return update_conjured_item
    else:
        return update_default_item


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_method = get_specific_update_method(item.name)
            update_method(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
