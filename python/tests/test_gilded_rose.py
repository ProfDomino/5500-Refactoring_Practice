# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item


class GildedRoseTest(unittest.TestCase):
    """This is a unit test class for the Gilded Rose refactored implementation."""
    
    def test_normal_item_decreases_quality(self):
        """This test checks that normal items decrease in quality by 1 each day."""
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
    
    def test_normal_item_decreases_quality_twice_after_sell_date(self):
        """This test checks that normal items decrease in quality by 2 after sell date."""
        items = [Item("Normal Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    def test_quality_never_negative(self):
        """This test checks that the quality of items never goes below 0."""
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
    
    def test_aged_brie_increases_quality(self):
        """This test checks that Aged Brie increases in quality as it ages."""
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
    
    def test_aged_brie_increases_quality_twice_after_sell_date(self):
        """This test checks that Aged Brie increases in quality by 2 after sell date."""
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    def test_quality_never_exceeds_50(self):
        """This test checks that the quality of items never exceeds 50 (except for legendary items)."""
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
    
    def test_sulfuras_never_changes(self):
        """This test checks that Sulfuras never decreases in quality or sell_in."""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(10, items[0].sell_in)
    
    def test_backstage_passes_increase_quality(self):
        """This test checks that Backstage passes increase in quality as concert approaches."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
    
    def test_backstage_passes_increase_by_2_when_10_days_or_less(self):
        """This test checks that Backstage passes increase by 2 when 10 days or less."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
    
    def test_backstage_passes_increase_by_3_when_5_days_or_less(self):
        """This test checks that Backstage passes increase by 3 when 5 days or less."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
    
    def test_backstage_passes_drop_to_zero_after_concert(self):
        """This test checks that Backstage passes drop to 0 after the concert."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    def test_conjured_items_degrade_twice_as_fast(self):
        """This test checks that Conjured items degrade in quality twice as fast as normal items."""
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
    
    def test_conjured_items_degrade_four_times_after_sell_date(self):
        """This test checks that Conjured items degrade by 4 after sell date."""
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    def test_multiple_items(self):
        """This test checks that multiple items are updated correctly."""
        items = [
            Item("Normal Item", 10, 20),
            Item("Aged Brie", 5, 10),
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Conjured Mana Cake", 3, 6)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(19, items[0].quality)
        self.assertEqual(11, items[1].quality)
        self.assertEqual(80, items[2].quality)
        self.assertEqual(21, items[3].quality)
        self.assertEqual(4, items[4].quality)

        
if __name__ == '__main__':
    unittest.main()
