# Gilded Rose Refactor Notes (Java)

When I first read `updateQuality()` it was basically a wall of nested ifs. It works, but it’s hard to reason about and adding “Conjured” would make it even worse. Also we weren’t allowed to touch the `Item` class, so I had to keep everything compatible with `name/sellIn/quality`.

I refactored using the Strategy pattern: each item type has its own updater class, and `GildedRose.updateQuality()` just loops through items and delegates the update. I used a small factory to choose the strategy based on the item name (and the `"Conjured "` prefix). This kept the main update method short and made Conjured easy to add.

Downsides: it adds more files/classes, and strategy selection still depends on the item name string (so a typo would fall back to Normal behavior). If we were allowed to change `Item`, I’d prefer an enum/type field instead of relying on strings.
