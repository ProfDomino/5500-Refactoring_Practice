# -*- coding: utf-8 -*-
from strategies.base import ItemUpdateStrategy


class Conjured(ItemUpdateStrategy):
    """This strategy is used for updating Conjured items.
    
    Conjured items degrade in quality twice as fast as normal items:
    - The quality decreases by 2 before the sell date
    - The quality decreases by 4 after the sell date
    """
    
    def update(self, item):
        """This method is used to update the quality and sell_in of a Conjured item."""
        item.quality -= 2
        
        self._decrease_sell_in(item)
        
        if item.sell_in < 0:
            item.quality -= 2
        
        item.quality = self._clamp_quality(item.quality)
