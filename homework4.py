from random import randint, choice

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(value, 0)

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'

class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self, heroes_list):
        random_hero = choice(heroes_list)
        self.__defence = random_hero.ability

    def attack(self, heroes_list):
        for hero in heroes_list:
            if hero.health > 0:
                if isinstance(hero, Berserk) and self.__defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'

class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes_list):
        pass

    def attack(self, boss):
        boss.health -= self.damage

class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes_list):
        coeff = randint(2, 5)
        boss.health -= coeff * self.damage
        print(f'Warrior {self.name} hits critically {coeff * self.damage}.')

class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')
        self.attack_increase = 5  # Amount to increase each round

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0:
                hero.damage += self.attack_increase

class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE')
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes_list):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damage to boss.')

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points

class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'REVIVE')

    def apply_super_power(self, boss, heroes_list):
        if any(hero.health == 0 for hero in heroes_list):
            for hero in heroes_list:
                if hero.health == 0:
                    hero.health = 100  # Revive with 100 health
                    self.health = 0  # Witcher sacrifices himself
                    print(f'Witcher {self.name} revives {hero.name}.')

class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'STEAL_HEALTH')

    def apply_super_power(self, boss, heroes_list):
        stolen_health = randint(10, 30)
        boss.health -= stolen_health
        target_hero = choice(heroes_list)
        target_hero.health += stolen_health
        print(f'Hacker {self.name} steals {stolen_health} health from boss and gives it to {target_hero.name}.')

class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health + 100, damage - 5, 'TAKE_DAMAGE')

    def apply_super_power(self, boss, heroes_list):
        damage_taken = self.damage // 5
        for hero in heroes_list:
            if hero.health > 0:
                hero.health -= damage_taken
        print(f'Golem {self.name} absorbs damage for allies.')

# Additional heroes can be implemented similarly...

round_number = 0

def is_game_over(boss, heroes_list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    if all(hero.health <= 0 for hero in heroes_list):
        print('Boss won!!!')
        return True
    return False

def show_statistics(boss, heroes_list):
    print(f' ------------- ROUND {round_number} -------------')
    print(boss)
    for hero in heroes_list:
        print(hero)

def play_round(boss, heroes_list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes_list)
    boss.attack(heroes_list)
    for hero in heroes_list:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes_list)
    show_statistics(boss, heroes_list)

def start_game():
    boss = Boss(name='Minotavr', health=1000, damage=50)

    warrior_1 = Warrior(name='Asterix', health=290, damage=10)
    warrior_2 = Warrior(name='Obelix', health=280, damage=5)
    magic = Magic(name='Alice', health=270, damage=10)
    berserk = Berserk(name='Guts', health=230, damage=5)
    medic = Medic(name='Doc', health=150, damage=5, heal_points=20)
    hacker = Hacker(name='Hacker', health=250, damage=20)
    witcher = Witcher(name='Geralt', health=300, damage=15)
    golem = Golem(name='Rocky', health=300, damage=5)
    

    heroes_list = [warrior_1, medic, warrior_2, magic, berserk, hacker, witcher, golem]
    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)

start_game()
