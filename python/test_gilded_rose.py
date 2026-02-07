# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """Comprehensive test suite for Gilded Rose refactoring"""
    
    # ===== Normal Item Tests =====
    
    def test_normal_item_decreases_quality(self):
        """Normal items decrease in quality by 1 each day"""
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
    
    def test_normal_item_decreases_sell_in(self):
        """Normal items decrease sell_in by 1 each day"""
        items = [Item("Normal Item", 5, 10)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(4, items[0].sell_in)
    
    def test_normal_item_degrades_twice_as_fast_after_sell_date(self):
        """Once sell_in passes, quality degrades twice as fast"""
        items = [Item("Normal Item", 0, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(18, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    def test_quality_never_negative(self):
        """Quality can never be negative"""
        items = [Item("Normal Item", 10, 0)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].quality)
    
    def test_quality_never_negative_after_sell_date(self):
        """Quality never goes below 0 even with double degradation"""
        items = [Item("Normal Item", -1, 1)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].quality)
    
    # ===== Aged Brie Tests =====
    
    def test_aged_brie_increases_quality(self):
        """Aged Brie increases in quality over time"""
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(21, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
    
    def test_aged_brie_increases_twice_as_fast_after_sell_date(self):
        """Aged Brie increases quality twice as fast after sell date"""
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(22, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    def test_aged_brie_quality_max_50(self):
        """Quality never exceeds 50"""
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(50, items[0].quality)
    
    def test_aged_brie_quality_max_50_after_sell_date(self):
        """Quality never exceeds 50 even after sell date"""
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(50, items[0].quality)
    
    # ===== Sulfuras Tests =====
    
    def test_sulfuras_never_decreases_quality(self):
        """Legendary items never decrease in quality"""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(80, items[0].quality)
    
    def test_sulfuras_never_decreases_sell_in(self):
        """Legendary items never decrease in sell_in"""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(10, items[0].sell_in)
    
    def test_sulfuras_never_changes_after_sell_date(self):
        """Sulfuras doesn't change even after sell date"""
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(80, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    # ===== Backstage Pass Tests =====
    
    def test_backstage_pass_increases_quality(self):
        """Backstage passes increase in quality as concert approaches"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)
    
    def test_backstage_pass_increases_by_2_when_10_days_or_less(self):
        """Quality increases by 2 when 10 days or less"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(22, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
    
    def test_backstage_pass_increases_by_3_when_5_days_or_less(self):
        """Quality increases by 3 when 5 days or less"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(23, items[0].quality)
        self.assertEqual(4, items[0].sell_in)
    
    def test_backstage_pass_quality_drops_to_zero_after_concert(self):
        """Quality drops to 0 after the concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    def test_backstage_pass_quality_max_50(self):
        """Backstage pass quality never exceeds 50"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(50, items[0].quality)
    
    def test_backstage_pass_at_exactly_11_days(self):
        """At 11 days, quality increases by 1 (not yet 10 days or less)"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(21, items[0].quality)
    
    def test_backstage_pass_at_exactly_6_days(self):
        """At 6 days, quality increases by 2 (not yet 5 days or less)"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(22, items[0].quality)
    
    # ===== Conjured Item Tests =====
    
    def test_conjured_items_degrade_twice_as_fast(self):
        """Conjured items degrade twice as fast as normal items"""
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(18, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
    
    def test_conjured_items_degrade_four_times_as_fast_after_sell_date(self):
        """Conjured items degrade at 4x speed after sell date"""
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(16, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    def test_conjured_quality_never_negative(self):
        """Conjured item quality never goes below 0"""
        items = [Item("Conjured Mana Cake", 10, 1)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].quality)
    
    def test_conjured_with_prefix(self):
        """Any item starting with 'Conjured' uses conjured strategy"""
        items = [Item("Conjured Magic Sword", 10, 20)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(18, items[0].quality)
    
    # ===== Multiple Items Tests =====
    
    def test_multiple_items_updated_correctly(self):
        """Multiple items are all updated correctly in one pass"""
        items = [
            Item("Normal Item", 10, 20),
            Item("Aged Brie", 10, 20),
            Item("Sulfuras, Hand of Ragnaros", 10, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Conjured Mana Cake", 10, 20)
        ]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(19, items[0].quality)
        self.assertEqual(21, items[1].quality)
        self.assertEqual(80, items[2].quality)
        self.assertEqual(21, items[3].quality)
        self.assertEqual(18, items[4].quality)
    
    def test_multiple_days_simulation(self):
        """Simulate multiple days of updates"""
        items = [Item("Normal Item", 3, 10)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)
        self.assertEqual(2, items[0].sell_in)
        
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(1, items[0].sell_in)
        
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)
        self.assertEqual(0, items[0].sell_in)
        
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
    
    # ===== Edge Cases =====
    
    def test_item_with_zero_quality_and_zero_sell_in(self):
        """Item with both zero quality and sell_in stays at zero quality"""
        items = [Item("Normal Item", 0, 0)]
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        
        self.assertEqual(0, items[0].quality)
    
    def test_backstage_pass_progression_complete(self):
        """Complete progression of backstage pass from 15 days to after concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)
        
        for i in range(5):
            gilded_rose.update_quality()
        self.assertEqual(15, items[0].quality)
        self.assertEqual(10, items[0].sell_in)
        
        for i in range(5):
            gilded_rose.update_quality()
        self.assertEqual(25, items[0].quality)
        self.assertEqual(5, items[0].sell_in)
        
        for i in range(5):
            gilded_rose.update_quality()
        self.assertEqual(40, items[0].quality)
        self.assertEqual(0, items[0].sell_in)
        
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()