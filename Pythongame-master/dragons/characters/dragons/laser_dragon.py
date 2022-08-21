from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.5
    implemented = True  # Change to True to view in the GUI
    damage = 2
    food_cost = 10
    
    # END 4.5

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
        # BEGIN 4.5
        Dict = {}
        currplace = self.place
        dis = 0
        while currplace.entrance is not None:
            if currplace is not skynet:
                l = [ i for i in currplace.terminators]

                #b = [ j for j in currplace.dragon]
                l.append(currplace.dragon)
                for i in l:
                    if i is not self:
                        Dict[i] = dis
            dis = dis + 1
            currplace  = currplace.entrance
        return Dict


            
        
        #return {}
        # END 4.5

    def calculate_damage(self, distance):
        # BEGIN 4.5

        return self.damage - 0.2*distance - 0.05*self.fighters_shot
        # END 4.5

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            if fighter is not None:

    
    
                fighter.reduce_armor(damage)
                if damage:
                    
                    self.fighters_shot += 1
             
