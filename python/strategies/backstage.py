# -*- coding: utf-8 -*-
from strategies.base import ItemUpdateStrategy


class Backstage(ItemUpdateStrategy):
    """This strategy is used for updating Backstage passes items.
    
    Backstage passes items increase in quality as the concert approaches:
    - The quality increases by 1 when the sell_in is greater than 10
    - The quality increases by 2 when the sell_in is between 5 and 10
    - The quality increases by 3 when the sell_in is between 0 and 5
    - The quality drops to 0 after the concert (when the sell_in is less than 0)
    """
    
    def update(self, item):
        """This method is used to update the quality and sell_in of a Backstage passes item."""
        if item.sell_in > 10:
            item.quality += 1
        elif item.sell_in > 5:
            item.quality += 2
        elif item.sell_in > 0:
            item.quality += 3
        
        self._decrease_sell_in(item)
        
        if item.sell_in < 0:
            item.quality = 0
        else:
            item.quality = self._clamp_quality(item.quality)