package com.gildedrose;

final class QualityRules {
    static final int MAX_QUALITY = 50;
    static final int SULFURAS_QUALITY = 80;

    static void clampQuality(Item item, int min, int max) {
        if (item.quality < min) item.quality = min;
        if (item.quality > max) item.quality = max;
    }

    static void clampNormalQuality(Item item) {
        clampQuality(item, 0, MAX_QUALITY);
    }

    private QualityRules() {}
}
