class Enemy:

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am {self.type_of_enemy}, I will end you!")

    def walk_forward(self):
        print(f'{self.type_of_enemy} is coming close for you...')

    def attack(self):
        print(f'{self.type_of_enemy} attacks you with {self.attack_damage} damage!')

    def get_type_of_enemy(self):
        return self.__type_of_enemy