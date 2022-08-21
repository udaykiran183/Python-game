from .dragon import Dragon
from utils import random_or_none


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1

    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3
    min_range = 0
    max_range = 100000

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        # REPLACE THIS LINE


        
        temp = self.place
        a = self.min_range
        b = self.max_range
        """
       

        """
        if a is not None:
            for i in range(a):
                temp=temp.entrance

        i = a  
        while(i <= b and temp is not None):
            i = i + 1
            if temp == 'skynet':
                temp=temp.entrance
                return None
            else:
                if len(temp.terminators)!= 0:
                    return random_or_none(temp.terminators)
                else:
        
                    temp=temp.entrance
        
        # END 1.3 and 2.1
        
    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))
