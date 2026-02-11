# Gilded Rose Refactoring – Design Notes

## Writeup

**Major issues:** The original updateQuality() was really hard to follow—tons of nested ifs and the same name checks over and over (Aged Brie, Sulfuras, Backstage passes). Adding Conjured would’ve meant more conditionals in there. Also we couldn’t change the Item class so everything had to work with the existing fields.

**Design choices:** I used the strategy pattern so each item type has its own class that knows how to update. GildedRose just loops and calls the right strategy. A factory looks at the item name (and the "Conjured " prefix) and returns which strategy to use. That way adding a new type is just a new class + putting it in the factory, no giant if/else.

**Drawbacks:** More files to maintain. Strategy selection is still based on the name string so if someone typos a name it’ll silently act like a normal item. Would’ve been nicer to have a type field on Item but we couldn’t touch that.

---

## Class diagram reference (for UML / Lucidchart)

- **Item** (unchanged): `name`, `sellIn`, `quality`; constructor, `toString()`
- **GildedRose**: `items: Item[]`; constructor, `updateQuality()` — loops, gets strategy from factory, calls update on it
- **ItemUpdateStrategy** (interface): `update(Item item)`
- **Concrete strategies** (implement the interface): NormalItemStrategy, AgedBrieStrategy, SulfurasStrategy, BackstagePassStrategy, ConjuredItemStrategy
- **ItemStrategyFactory**: `forItem(Item): ItemUpdateStrategy` — gets strategy by item name / "Conjured " prefix
- **QualityRules**: MAX_QUALITY, SULFURAS_QUALITY; clamp methods (strategies do bounds themselves so these are barely used)

GildedRose has the items array, calls the factory to get a strategy, then strategy.update(item). All the strategy classes implement the interface. Factory picks which one by name.
