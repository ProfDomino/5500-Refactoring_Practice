# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class ItemUpdateStrategy(ABC):
    """This is an abstract base class for item update strategies."""
    
    @abstractmethod
    def update(self, item):
        """This method is used to update the quality and sell_in of an item.
        
        Args:
            item: The item to update
        """
        pass
    
    def _clamp_quality(self, quality):
        """This method is used to ensure that the quality of an item stays within valid bounds (0-50).
        
        Args:
            quality: The quality value to clamp (the value to be clamped)
            
        Returns:
            The clamped quality value between 0 and 50
        """
        return max(0, min(50, quality))
    
    def _decrease_sell_in(self, item):
        """This method is used to decrease the sell_in of an item by 1.
        
        Args:
            item: The item to update (the item to decrease the sell_in of)
        """
        item.sell_in -= 1
