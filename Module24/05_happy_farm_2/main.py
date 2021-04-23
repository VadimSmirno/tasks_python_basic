from garden import PotetoGarden

my_garden = PotetoGarden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_al()
    my_garden.are_all_ripe()