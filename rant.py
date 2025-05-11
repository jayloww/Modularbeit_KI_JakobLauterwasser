from ant import Ant
import random

class RandomAnt(Ant):
    def __init__(self, x, y, team, simulation):
        super().__init__(x, y, team, simulation)

    def act(self):
        self.direction = random.choice(self.directions)
        if(self.hasFood):
            if(self.atOwnNest()):
                self.dropFood()
        elif(self.senseFood()[0]):
            self.takeFood()