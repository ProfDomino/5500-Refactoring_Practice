import pytest

from gilded_rose import GildedRose, Item

AGED_BRIE = "Aged Brie"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"
NORMAL = "+5 Dexterity Vest"


def run_days(items, days: int):
    gr = GildedRose(items)
    for _ in range(days):
        gr.update_quality()
    return items


# -------------------------
# Normal items
# -------------------------

def test_normal_item_degrades_by_1_before_sell_date():
    items = run_days([Item(NORMAL, sell_in=10, quality=20)], 1)
    assert items[0].sell_in == 9
    assert items[0].quality == 19


def test_normal_item_degrades_by_2_after_sell_date_passed():
    # sell_in=0 -> after update becomes -1, so it should degrade by 2
    items = run_days([Item(NORMAL, sell_in=0, quality=10)], 1)
    assert items[0].sell_in == -1
    assert items[0].quality == 8


def test_normal_item_quality_never_negative():
    items = run_days([Item(NORMAL, sell_in=0, quality=0)], 3)
    assert items[0].quality == 0


# -------------------------
# Aged Brie
# -------------------------

def test_aged_brie_increases_by_1_before_sell_date():
    items = run_days([Item(AGED_BRIE, sell_in=5, quality=10)], 1)
    assert items[0].sell_in == 4
    assert items[0].quality == 11


def test_aged_brie_increases_by_2_after_sell_date_passed():
    # sell_in=0 -> after update becomes -1; baseline behavior increases twice
    items = run_days([Item(AGED_BRIE, sell_in=0, quality=10)], 1)
    assert items[0].sell_in == -1
    assert items[0].quality == 12


def test_aged_brie_quality_capped_at_50():
    items = run_days([Item(AGED_BRIE, sell_in=0, quality=49)], 2)
    assert items[0].quality == 50


# -------------------------
# Backstage passes
# -------------------------

def test_backstage_increases_by_1_when_more_than_10_days():
    items = run_days([Item(BACKSTAGE, sell_in=15, quality=20)], 1)
    assert items[0].sell_in == 14
    assert items[0].quality == 21


def test_backstage_increases_by_2_when_10_days_or_less():
    # sell_in=10 -> after update becomes 9 (<10), so +2 total
    items = run_days([Item(BACKSTAGE, sell_in=10, quality=20)], 1)
    assert items[0].sell_in == 9
    assert items[0].quality == 22


def test_backstage_increases_by_3_when_5_days_or_less():
    # sell_in=5 -> after update becomes 4 (<5), so +3 total
    items = run_days([Item(BACKSTAGE, sell_in=5, quality=20)], 1)
    assert items[0].sell_in == 4
    assert items[0].quality == 23


def test_backstage_drops_to_0_after_concert():
    # sell_in=0 -> after update -1, quality should become 0
    items = run_days([Item(BACKSTAGE, sell_in=0, quality=40)], 1)
    assert items[0].sell_in == -1
    assert items[0].quality == 0


def test_backstage_quality_capped_at_50():
    items = run_days([Item(BACKSTAGE, sell_in=6, quality=49)], 1)
    assert items[0].quality == 50


# -------------------------
# Sulfuras
# -------------------------

def test_sulfuras_never_changes_sell_in_or_quality():
    items = run_days([Item(SULFURAS, sell_in=0, quality=80)], 10)
    assert items[0].sell_in == 0
    assert items[0].quality == 80


# -------------------------
# Conjured (matches THIS repo's implementation, not the original spec)
# -------------------------

def test_conjured_degrades_like_normal_before_sell_date():
    items = run_days([Item(CONJURED, sell_in=2, quality=5)], 1)
    assert items[0].sell_in == 1
    assert items[0].quality == 4


def test_conjured_degrades_like_normal_after_sell_date_passed():
    items = run_days([Item(CONJURED, sell_in=0, quality=5)], 1)
    assert items[0].sell_in == -1
    assert items[0].quality == 3


def test_conjured_quality_never_negative():
    items = run_days([Item(CONJURED, sell_in=0, quality=0)], 2)
    assert items[0].quality == 0
