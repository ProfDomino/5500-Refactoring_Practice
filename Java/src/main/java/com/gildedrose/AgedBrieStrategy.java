package com.gildedrose;

final class AgedBrieStrategy implements ItemUpdateStrategy {
    @Override
    public void update(Item item) {
        int delta = item.sellIn <= 0 ? 2 : 1;
        item.quality = Math.min(QualityRules.MAX_QUALITY, item.quality + delta);
        item.sellIn--;
    }
}
