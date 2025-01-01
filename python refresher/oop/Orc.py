from Enemy import *

class Orc(Enemy):

    def __init__(self, type_of_enemy, health_points, attack_damage):
        super().__init__(type_of_enemy, 
                         health_points, 
                         attack_damage)

    def talk():
        print("I will drink your Blood!!!")
