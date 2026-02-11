package com.gildedrose;

final class ConjuredItemStrategy implements ItemUpdateStrategy {
    @Override
    public void update(Item item) {
        int delta = item.sellIn <= 0 ? -4 : -2;
        item.quality = Math.max(0, item.quality + delta);
        item.sellIn--;
    }
}
