# -*- coding: utf-8 -*-
from strategies.base import ItemUpdateStrategy


class Sulfuras(ItemUpdateStrategy):
    """This strategy is used for updating Sulfuras items.
    
    Sulfuras items are legendary items that:
    - Never have to be sold (the sell_in doesn't change)
    - Never decrease in quality
    - The quality is always 80
    """
    
    def update(self, item):
        """This method is used to update the quality and sell_in of a Sulfuras item."""
        pass
