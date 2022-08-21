from .dragon import Dragon
class EarthDragon(Dragon):
    # ADD/OVERRIDE
    # CLASS ATTRIBUTES HERE
    name = 'Earth'
    #damage = 4
    # OVERRIDE CLASS ATTRIBUTES HERE
    
    implemented = True # Change to True to view in the GUI
    food_cost = 4 
    def __init__(self, armor = 4 ):
        self.armor = 4
    pass
