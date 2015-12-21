#!/usr/bin/python3
import itertools
BOSS_HP = 109
BOSS_DMG = 8
BOSS_ARM = 2
PLAYER_HP = 100

class Item(object):
    def __init__(self, cost, damage, armor):
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return '<${0} D{1} A{2}>'.format(self.cost, self.damage, self.armor)
    def __repr__(self):
        return self.__str__()

WEAPONS = [
    Item(8, 4, 0),
    Item(10, 5, 0),
    Item(25, 6, 0),
    Item(40, 7, 0),
    Item(74, 8, 0)
]

ARMOR = [
    Item(13, 0, 1),
    Item(31, 0, 2),
    Item(53, 0, 3),
    Item(75, 0, 4),
    Item(102, 0, 5)
]

RINGS = [
    Item(25, 1, 0),
    Item(50, 2, 0),
    Item(100, 3, 0),
    Item(20, 0, 1),
    Item(40, 0, 2),
    Item(80, 0, 3)
]

COMBINATIONS = []

def fight(Pdmg, Parm):
    Bhp = BOSS_HP
    Php = PLAYER_HP
    while Bhp > 0 and Php > 0:
        if Bhp > 0 and Php > 0:
            # Player turn
            Bhp = Bhp - Pdmg + BOSS_ARM
        if Bhp > 0 and Php > 0:
            # Boss turn
            Php = Php - BOSS_DMG + Parm
    return (Php > Bhp)

# And now, let’s build all the possible combinations.
for weapon in WEAPONS:
    COMBINATIONS.append((weapon,))
    for plate in ARMOR:
        COMBINATIONS.append((weapon, plate))
# Finally, rings.  We will iterate over weapon/plate combinations and add zero,
# one and two rings.
RC = []
for ring in RINGS:
    for combination in COMBINATIONS:
        RC.append(tuple(list(combination) + [ring]))
R2C = []
for i in itertools.permutations(RINGS, 2):
    if i not in R2C and reversed(i) not in R2C:
        R2C.append(i)
for combination in COMBINATIONS:
    for rc in R2C:
        RC.append(tuple(list(combination) + list(rc)))

COMBINATIONS += RC

# Find the cheapest option.
valprice = {}

for c in COMBINATIONS:
    damage = armor = cost = 0
    for item in c:
        damage += item.damage
        armor += item.armor
        cost += item.cost
    k = (damage, armor)
    #valprice[k] = min(cost, valprice.get(k, 10000))
    valprice[k] = max(cost, valprice.get(k, 0))

print("{0} item combinations found.".format(len(valprice)))

# AND FIGHT!
LOST = []
for stats, price in valprice.items():
    #if fight(*stats):
    if not fight(*stats):
        LOST.append(price)
#print(min(LOST))
print(max(LOST))
