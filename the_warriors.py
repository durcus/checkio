"""
создать класс Warrior, у экземпляров которого будет 2 параметра - здоровье (равное 50) и атака (равная 5), а также свойство is_alive, которое может быть True (если здоровье воина > 0) или False (в ином случае). Кроме этого вам необходимо создать класс для второго типа солдат - Knight, который будет наследником Warrior, но с увеличенной атакой - 7. Также вам необходимо будет создать функцию fight(), которая будет проводить дуэли между 2 воинами и определять сильнейшего из них. Бои происходят по следующему принципу:
каждый ход первый воин наносит второму урон в размере своей атаки, в следствие чего здоровье второго воина уменьшается, после чего аналогично поступает и второй воин по отношению к первому.
Если в конце очередного хода у первого воина здоровье > 0, а у другого - нет, выживший объявляется победителем и функция возвращает True, или False в ином случае.
"""


class Warrior():
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    def _getalive(self):
        if self.health > 0:
            return True
        else:
            return False

    is_alive = property(_getalive)


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)


def fight(chel1, chel2):
    while chel1.health > 0 and chel2.health > 0:
        chel2.health -= chel1.attack
        if chel2.health > 0:
            chel1.health -= chel2.attack
    if chel1.health > 0:
        return True
    else:
        return False


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

print(fight(chuck, bruce) == True)
print(fight(dave, carl) == False)
print(chuck.is_alive == True)
print(bruce.is_alive == False)
print(carl.is_alive == True)
print(dave.is_alive == False)
print(fight(carl, mark) == False)
print(carl.is_alive == False)
