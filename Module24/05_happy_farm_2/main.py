from garden import PotetoGarden
from garden import Garden
from garden import Potesto

# TODO, должна быть только 1 грядка за которой ухаживает садовник. my_garden - лишняя =)
my_garden = PotetoGarden(5)
my_garden.are_all_ripe()

# TODO, сейчас назвали садовника "мой сад"? =) Возможно, стоит придумать ему другое название.
my_garden2 = Garden('Остин', 5)
my_garden2.look_after()
print(my_garden2.ridge.potetoes)
for _ in range(3):
    my_garden.grow_al()
    my_garden.are_all_ripe()
    my_garden2.look_after()
print(my_garden2.ridge.potetoes)

# зачёт!







