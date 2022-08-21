from .dragon import Dragon
from .scuba_thrower import ScubaThrower
from utils import terminators_win


class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    implemented = True  # Change to True to view in the GUI
    damage = 1 
    food_cost = 7
    instantiated = False
    buffed_dragon = []
    # END 4.3


    def __init__(self, armor=1):
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        ScubaThrower.__init__(self,armor)
        self.isKing = False

        if not DragonKing.instantiated :
            DragonKing.instantiated  = True
            self.isKing = True
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if  self.isKing == False:
            self.reduce_armor(self.armor)
        else:
            super().action(colony)
            curPlace = self.place
            curPlace = curPlace.exit
            while curPlace is not None:
                if curPlace.dragon != None:
                    if curPlace.dragon.is_container:
                        if curPlace.dragon is not None:
                            if curPlace.dragon not in self.buffed_dragon:
                                curPlace.dragon.damage *= 2
                                self.buffed_dragon.append(curPlace.dragon)
                            if curPlace.dragon.contained_dragon is not None:    
                                if curPlace.dragon.contained_dragon not in self.buffed_dragon:
                                    curPlace.dragon.contained_dragon.damage *= 2
                                    self.buffed_dragon.append(curPlace.dragon.contained_dragon)
                    else:
                        if curPlace.dragon not in self.buffed_dragon:
                            curPlace.dragon.damage *= 2
                            self.buffed_dragon.append(curPlace.dragon)

                curPlace = curPlace.exit



        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        if self.armor - amount <= 0 and self.isKing:
            terminators_win()

        super().reduce_armor(amount)

        


        "*** YOUR CODE HERE ***"
