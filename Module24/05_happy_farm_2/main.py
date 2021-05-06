from garden import PotetoGarden
from garden import Garden

# TODO, должна быть только 1 грядка за которой ухаживает садовник. my_garden - лишняя =)
# my_garden = PotetoGarden(5)
# my_garden.are_all_ripe()


garden = Garden('Остин', 5)
garden.look_after()

for _ in range(3):
    # my_garden.grow_al()
    # my_garden.are_all_ripe()
    garden.look_after()


# зачёт!







