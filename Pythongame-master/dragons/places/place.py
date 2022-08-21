from typing import Container

from characters.fighter import Fighter
#from .dragon_colony i


class Place(object):
    """A Place holds fighters and has an exit to another Place."""

    def __init__(self, name, exit=None):
        """Create a Place with the given NAME and EXIT.

        name -- A string; the name of this Place.
        exit -- The Place reached by exiting this Place (may be None).
        """
        self.name = name
        self.exit = exit
        self.terminators = []  # A list of Terminators
        self.dragon = None  # A Dragon
        self.entrance = None  # A Place
        # Phase 1: Add an entrance to the exit
        # BEGIN 1.2
        "*** YOUR CODE HERE ***"
        if self.exit!=None:
            self.exit.entrance=self
        # END 1.2

    def add_fighter(self, fighter):
        """Add a Fighter to this Place.

        There can be at most one Dragon in a Place, unless exactly one of them is
        a container dragon , in which case there can be two. If add_fighter
        tries to add more Dragons than is allowed, an assertion error is raised.

        There can be any number of Terminators in a Place.
        """
        if fighter.is_dragon:
            if self.dragon is None:
                self.dragon = fighter
            else:
                # BEGIN 3.2
                if fighter.is_container and not self.dragon.is_container:
                    if not self.dragon.is_container:              
                        
                        if fighter.contain_dragon(self.dragon) is False:
                            assert self.dragon is None, 'Two dragons in {0}'.format(self)
                        
                        fighter.contain_dragon(self.dragon)
                        #self.dragon.place = fighter.place
                        #self.place.dragon = fighter
                        self.dragon = fighter                        
                elif not fighter.is_container and self.dragon.is_container:
                    if  self.dragon.is_container :
                        #Place.dragon = self.dragon
                        
                        if self.dragon.contain_dragon(fighter) is False:
                            assert self.dragon is None, 'Two dragons in {0}'.format(self)

                        self.dragon.contain_dragon(fighter)

                        #fighter.place = self                        
                else:
                    assert self.dragon is None, 'Two dragons in {0}'.format(self)
                # END 3.2
        else:
            self.terminators.append(fighter)
        fighter.place = self

    def remove_fighter(self, fighter):
        """Remove a FIGHTER from this Place.

        A target Dragon may either be directly in the Place, or be contained by a
        container Dragon at this place. The true DragonKing may not be removed. If
        remove_fighter tries to remove a Dragon that is not anywhere in this
        Place, an AssertionError is raised.

        A Terminator is just removed from the list of Terminators.
        """
        if fighter.is_dragon:
            # Special handling for DragonKing
            # BEGIN 4.3
            "*** YOUR CODE HERE ***"
            if fighter.name == 'King' and fighter.isKing :
                if not fighter.isKing:
                      self.dragon = None
                      fighter.place = None
                elif fighter.isKing:
                      self.dragon = fighter
                      fighter.place = self
                return   

            # END 4.3

            # Special handling for container dragons
            if self.dragon is fighter:
                # Bodyguard was removed. Contained dragon should remain in the game
                if hasattr(self.dragon, 'is_container') and self.dragon.is_container:
                    self.dragon = self.dragon.contained_dragon
                else:
                    self.dragon = None
            else:
                # Contained dragon was removed. Bodyguard should remain
                if hasattr(self.dragon, 'is_container') and self.dragon.is_container \
                        and self.dragon.contained_dragon is fighter:
                    self.dragon.contained_dragon = None
                else:
                    assert False, '{0} is not in {1}'.format(fighter, self)
        else:
            self.terminators.remove(fighter)

        fighter.place = None

    def __str__(self):
        return self.name
