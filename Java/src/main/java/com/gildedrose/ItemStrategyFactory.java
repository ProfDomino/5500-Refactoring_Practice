package com.gildedrose;

import java.util.HashMap;
import java.util.Map;

final class ItemStrategyFactory {
    private static final String AGED_BRIE = "Aged Brie";
    private static final String BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert";
    private static final String SULFURAS = "Sulfuras, Hand of Ragnaros";
    private static final String CONJURED_PREFIX = "Conjured ";

    private static final Map<String, ItemUpdateStrategy> STRATEGIES = new HashMap<>();

    static {
        STRATEGIES.put(AGED_BRIE, new AgedBrieStrategy());
        STRATEGIES.put(BACKSTAGE_PASS, new BackstagePassStrategy());
        STRATEGIES.put(SULFURAS, new SulfurasStrategy());
    }

    static ItemUpdateStrategy forItem(Item item) {
        if (STRATEGIES.containsKey(item.name)) {
            return STRATEGIES.get(item.name);
        }
        if (item.name.startsWith(CONJURED_PREFIX)) {
            return new ConjuredItemStrategy();
        }
        return new NormalItemStrategy();
    }

    private ItemStrategyFactory() {}
}
