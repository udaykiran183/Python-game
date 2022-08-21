from .thrower_dragon import ThrowerDragon
from utils import apply_effect, make_scare, make_slow



class ScaryThrower(ThrowerDragon):
    """ThrowerDragon that intimidates Terminators, making them back away instead of advancing."""

    name = 'Scary'
    # BEGIN 4.4
    implemented = True # Change to True to view in the GUI
    food_cost = 6
    def action(self, colony):
        super().action(colony)

    # END 4.4

    def throw_at(self, target):
        # BEGIN 4.4
        "*** YOUR CODE HERE ***"
        if target and target.already_scared is False:
            apply_effect(make_scare, target, 2)
        # END 4.4
