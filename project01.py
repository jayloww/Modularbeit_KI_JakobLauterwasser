from simulation import Simulation
from ant import Ant
from tqdm import tqdm

class SearchBasedAnt(Ant):
    def __init__(self, x, y, team, simulation):
        super().__init__(x, y, team, simulation)
        self.nestPosition = (5,1)
        self.foodPosition = (7,25)

    def act(self):
        pass


if __name__ == "__main__":
    simulation = Simulation(SearchBasedAnt, SearchBasedAnt, logfile="project01.rec")   
  
    simulation.loadArena("single01.txt")

    for t in tqdm(range(100)):
        simulation.tick()
    
    print(simulation.foodCount)

    simulation.shutdown()