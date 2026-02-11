package com.gildedrose;

final class NormalItemStrategy implements ItemUpdateStrategy {
    @Override
    public void update(Item item) {
        int delta = item.sellIn <= 0 ? -2 : -1;
        item.quality = Math.max(0, item.quality + delta);
        item.sellIn--;
    }
}
