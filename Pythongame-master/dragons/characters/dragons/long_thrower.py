from .thrower_dragon import ThrowerDragon


class LongThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at least 5 places away."""

    name = 'Long'
    food_cost = 2
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.1
    implemented = True
    min_range = 5
    max_range = float('inf')
    #a = dimension[2]
    damage = 1

    # Change to True to view in the GUI
    # END 2.1
