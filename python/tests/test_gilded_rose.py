# -*- coding: utf-8 -*-
import unittest
from gilded_rose_revision import (
    GildedRose, create_item,
    NormalItem, AgedItem, BackstageItem, LegendItem, ConjuredItem
)


class GildedRoseTest(unittest.TestCase):

    # Normal Item tests
    def test_normal_item_decreases_quality(self):
        item = create_item("foo", 10, 20)
        GildedRose([item]).update_quality()
        self.assertEqual(19, item.get_quality())

    def test_normal_item_decreases_twice_after_sell_date(self):
        item = create_item("foo", 0, 20)
        GildedRose([item]).update_quality()
        self.assertEqual(18, item.get_quality())

    def test_quality_never_negative(self):
        item = create_item("foo", 5, 0)
        GildedRose([item]).update_quality()
        self.assertEqual(0, item.get_quality())

    # Aged Brie tests
    def test_aged_brie_increases_quality(self):
        item = create_item("Aged Brie", 10, 20)
        GildedRose([item]).update_quality()
        self.assertEqual(21, item.get_quality())

    def test_aged_brie_quality_max_50(self):
        item = create_item("Aged Brie", 10, 50)
        GildedRose([item]).update_quality()
        self.assertEqual(50, item.get_quality())

    # Sulfuras tests
    def test_sulfuras_never_changes(self):
        item = create_item("Sulfuras, Hand of Ragnaros", 10, 80)
        GildedRose([item]).update_quality()
        self.assertEqual(80, item.get_quality())
        self.assertEqual(10, item.get_sell_in())

    # Backstage pass tests
    def test_backstage_increases_by_1_when_more_than_10_days(self):
        item = create_item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
        GildedRose([item]).update_quality()
        self.assertEqual(21, item.get_quality())

    def test_backstage_increases_by_2_when_10_days_or_less(self):
        item = create_item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        GildedRose([item]).update_quality()
        self.assertEqual(22, item.get_quality())

    def test_backstage_increases_by_3_when_5_days_or_less(self):
        item = create_item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        GildedRose([item]).update_quality()
        self.assertEqual(23, item.get_quality())

    def test_backstage_drops_to_0_after_concert(self):
        item = create_item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        GildedRose([item]).update_quality()
        self.assertEqual(0, item.get_quality())

    # Conjured tests
    def test_conjured_decreases_twice_as_fast(self):
        item = create_item("Conjured Mana Cake", 10, 20)
        GildedRose([item]).update_quality()
        self.assertEqual(18, item.get_quality())

    def test_conjured_decreases_four_times_after_sell_date(self):
        item = create_item("Conjured Mana Cake", 0, 20)
        GildedRose([item]).update_quality()
        self.assertEqual(16, item.get_quality())


if __name__ == '__main__':
    unittest.main()