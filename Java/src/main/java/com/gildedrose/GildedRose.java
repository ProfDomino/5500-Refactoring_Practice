package com.gildedrose;

class GildedRose {
    Item[] items;

    public GildedRose(Item[] items) {
        this.items = items;
    }

    public void updateQuality() {
        for (Item item : items) {
            ItemUpdateStrategy strategy = ItemStrategyFactory.forItem(item);
            strategy.update(item);
        }
    }
}
