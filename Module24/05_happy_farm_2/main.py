from garden import PotetoGarden
from garden import Garden
from garden import Potesto


my_garden = PotetoGarden(5)
my_garden.are_all_ripe()
my_garden2 = Garden('Остин', 5)
my_garden2.look_after()
for _ in range(3):
    my_garden.grow_al()
    my_garden.are_all_ripe()
    my_garden2.look_after()






