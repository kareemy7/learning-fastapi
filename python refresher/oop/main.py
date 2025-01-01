from Enemy import *
from Zombie import *
from Orc import *

zombie = Zombie(10, 3)
zombie.type_of_enemy = 'Zombie'
print(f'{zombie.type_of_enemy} has {zombie.health_points} health points and deals {zombie.attack_damage} damage')

zombie.talk()
zombie.walk_forward()
zombie.attack()