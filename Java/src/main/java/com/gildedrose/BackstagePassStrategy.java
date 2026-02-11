package com.gildedrose;

final class BackstagePassStrategy implements ItemUpdateStrategy {
    @Override
    public void update(Item item) {
        if (item.sellIn <= 0) {
            item.quality = 0;
        } else {
            int delta = 1;
            if (item.sellIn <= 10) delta++;
            if (item.sellIn <= 5) delta++;
            item.quality = Math.min(QualityRules.MAX_QUALITY, item.quality + delta);
        }
        item.sellIn--;
    }
}
