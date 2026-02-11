# -*- coding: utf-8 -*-
"""
Unit Tests for Gilded Rose
"""

import unittest
from gilded_rose import Item, GildedRose


class TestNormalItem(unittest.TestCase):
    """Tests for normal items."""
    
    def test_quality_decreases_by_1(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)
    
    def test_sell_in_decreases_by_1(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
    
    def test_quality_never_negative(self):
        items = [Item("Normal Item", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)


class TestAgedBrie(unittest.TestCase):
    """Tests for Aged Brie."""
    
    def test_quality_increases(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)


class TestSulfuras(unittest.TestCase):
    """Tests for Sulfuras."""
    
    def test_quality_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)


if __name__ == '__main__':
    unittest.main()