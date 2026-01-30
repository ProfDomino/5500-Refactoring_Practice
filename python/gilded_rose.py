class GildedRose(object):

    def __init__(self, items):
        self.items = items
        # Create one factory we can reuse
        self._updater_factory = ItemUpdaterFactory()

    def update_quality(self):
        for item in self.items:
            # Ask the factory for the updater for this item
            updater = self._updater_factory.get_updater(item)

            updater.update(item)

def limit_quality(item):
    if item.quality < 0:
        item.quality = 0

    if item.quality > 50:
        item.quality = 50


class ItemUpdater:
    def update(self, item):
        # For most items: update quality before days_left and decrease days_left (usually); 
        # If expired, apply extra quality update; limit quality to valid range,
        self.update_quality_before_sell_date(item)

        self.decrease_days_left(item)

        if item.days_left < 0:
            self.update_quality_after_sell_date(item)

        self.limit(item)

    def update_quality_before_sell_date(self, item):
        if item.quality > 0:
            item.quality -= 1

    def update_quality_after_sell_date(self, item):
        if item.quality > 0:
            item.quality -= 1

    def decrease_days_left(self, item):
        item.days_left -= 1

    def limit(self, item):
        limit_quality(item)



# UPDATERS
class AgedBrieUpdater(ItemUpdater):
    # Aged Brie: quality increases as it ages; after sell date, increases faster
    def update_quality_before_sell_date(self, item):
        item.quality += 1

    def update_quality_after_sell_date(self, item):
        item.quality += 1


class BackstagePassUpdater(ItemUpdater):
    # Backstage passes: quality increases as it approaches; after concert, quality is 0
    def update_quality_before_sell_date(self, item):
        item.quality += 1

        if item.days_left < 11:
            item.quality += 1

        if item.days_left < 6:
            item.quality += 1

    def update_quality_after_sell_date(self, item):
        item.quality = 0


class SulfurasUpdater(ItemUpdater):
    # Sulfuras is special;
    def update(self, item):
        return

    def limit(self, item):
        return


class NormalItemUpdater(ItemUpdater):
    pass


class ItemUpdaterFactory:
    # Factory returns the correct updater based on item.name.
    def __init__(self):
        # Create and reuse updater instances (no need to recreate them each time)
        self._updaters_by_name = {
            "Aged Brie": AgedBrieUpdater(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater(),
            "Sulfuras, Hand of Ragnaros": SulfurasUpdater(),
        }

        # Default updater for any item name not in the dictionary
        self._default_updater = NormalItemUpdater()

    def get_updater(self, item):
        #Return the updater. If uddater name not recognized, return default updater.
        return self._updaters_by_name.get(item.name, self._default_updater)
    

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @property
    def days_left(self):
        # Alias for sell_in.
        return self.sell_in

    @days_left.setter
    def days_left(self, value):
        #Alias setter for sell_in. Assignments to days_left get stored in sell_in.
        self.sell_in = value

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    