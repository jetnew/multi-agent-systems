from classes import *
from builders import *

game = Game(size=(300, 300))

# Glider
glider = [Agent((0,0)),
          Agent((1,1)),
          Agent((2,1)),
          Agent((0,2)),
          Agent((1,2))]
for a in glider:
    game.add_agent(a)

game.render(speed=50, frames=(600,600))