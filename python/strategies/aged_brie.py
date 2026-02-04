# -*- coding: utf-8 -*-
from strategies.base import ItemUpdateStrategy


class AgedBrie(ItemUpdateStrategy):
    """This strategy is used for updating Aged Brie items.
    
    Aged Brie items increase in quality as they age.
    After the sell_in date passes, the quality increases twice as fast.
    """
    
    def update(self, item):
        """This method is used to update the quality and sell_in of an Aged Brie item."""
        item.quality += 1

        self._decrease_sell_in(item)
        
        if item.sell_in < 0:
            item.quality += 1

        item.quality = self._clamp_quality(item.quality)
