package com.gildedrose;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class GildedRoseTest {

    // --- Normal items ---

    @Test
    void normalItemLosesQualityAndSellIn() {
        Item[] items = new Item[] { new Item("+5 Dexterity Vest", 10, 20) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(9, items[0].sellIn);
        assertEquals(19, items[0].quality);
    }

    @Test
    void normalItemDegradesTwiceAsFastAfterSellBy() {
        Item[] items = new Item[] { new Item("Elixir", 0, 10) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(-1, items[0].sellIn);
        assertEquals(8, items[0].quality);
    }

    @Test
    void qualityNeverGoesNegative() {
        Item[] items = new Item[] { new Item("Elixir", 5, 0) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(0, items[0].quality);
    }

    @Test
    void qualityNeverGoesNegativeAfterSellBy() {
        Item[] items = new Item[] { new Item("Elixir", 0, 1) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(0, items[0].quality);
    }

    // --- Aged Brie ---

    @Test
    void agedBrieIncreasesInQuality() {
        Item[] items = new Item[] { new Item("Aged Brie", 5, 10) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(4, items[0].sellIn);
        assertEquals(11, items[0].quality);
    }

    @Test
    void agedBrieIncreasesTwiceAfterSellBy() {
        Item[] items = new Item[] { new Item("Aged Brie", 0, 10) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(-1, items[0].sellIn);
        assertEquals(12, items[0].quality);
    }

    @Test
    void agedBrieNeverExceeds50() {
        Item[] items = new Item[] { new Item("Aged Brie", 5, 50) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(50, items[0].quality);
    }

    // --- Sulfuras ---

    @Test
    void sulfurasNeverChanges() {
        Item[] items = new Item[] { new Item("Sulfuras, Hand of Ragnaros", 0, 80) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(0, items[0].sellIn);
        assertEquals(80, items[0].quality);
    }

    @Test
    void sulfurasNeverChangesNegativeSellIn() {
        Item[] items = new Item[] { new Item("Sulfuras, Hand of Ragnaros", -1, 80) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(-1, items[0].sellIn);
        assertEquals(80, items[0].quality);
    }

    // --- Backstage passes ---

    @Test
    void backstagePassIncreasesBy1WhenMoreThan10Days() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert", 15, 20) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(14, items[0].sellIn);
        assertEquals(21, items[0].quality);
    }

    @Test
    void backstagePassIncreasesBy2At10Days() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert", 10, 20) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(9, items[0].sellIn);
        assertEquals(22, items[0].quality);
    }

    @Test
    void backstagePassIncreasesBy3At5Days() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert", 5, 20) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(4, items[0].sellIn);
        assertEquals(23, items[0].quality);
    }

    @Test
    void backstagePassDropsToZeroAfterConcert() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert", 0, 50) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(-1, items[0].sellIn);
        assertEquals(0, items[0].quality);
    }

    @Test
    void backstagePassNeverExceeds50() {
        Item[] items = new Item[] { new Item("Backstage passes to a TAFKAL80ETC concert", 5, 49) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(50, items[0].quality);
    }

    // --- Conjured items ---

    @Test
    void conjuredDegradesTwiceAsFast() {
        Item[] items = new Item[] { new Item("Conjured Mana Cake", 3, 6) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(2, items[0].sellIn);
        assertEquals(4, items[0].quality);
    }

    @Test
    void conjuredDegradesFourTimesAfterSellBy() {
        Item[] items = new Item[] { new Item("Conjured Mana Cake", 0, 6) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(-1, items[0].sellIn);
        assertEquals(2, items[0].quality);
    }

    @Test
    void conjuredNeverGoesNegative() {
        Item[] items = new Item[] { new Item("Conjured Mana Cake", 0, 1) };
        GildedRose app = new GildedRose(items);
        app.updateQuality();
        assertEquals(0, items[0].quality);
    }
}
