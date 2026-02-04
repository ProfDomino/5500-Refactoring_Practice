# -*- coding: utf-8 -*-
from strategies.base import ItemUpdateStrategy


class NormalItem(ItemUpdateStrategy):
    """This strategy is used for updating normal items.
    
    Normal items decrease the quality by 1 each day.
    After the sell_in date passes, the quality degrades twice as fast.
    """
    
    def update(self, item):
        """This method is used to update the quality and sell_in of a normal item."""
        item.quality -= 1
        
        self._decrease_sell_in(item)
        
        if item.sell_in < 0:
            item.quality -= 1
        
        item.quality = self._clamp_quality(item.quality)
