#!/usr/bin/python3
import itertools
BOSS_HP = 58
BOSS_DMG = 9
PLAYER_HP = 50
PLAYER_MANA = 500

class Spell(object):
    cost = 0
    damage = 0
    heal = 0
    armor = 0
    addmana = 0
    turns = -1
    def __init__(self, cost=0, damage=0, heal=0, armor=0, addmana=0, turns=-1):
        self.cost = cost
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.addmana = addmana
        self.turns = turns

SPELLS = [
    Spell(cost=53, damage=4),
    Spell(cost=73, damage=2, heal=2),
    Spell(cost=113, armor=7, turns=6),
    Spell(cost=173, damage=3, turns=6),
    Spell(cost=229, addmana=101, turns=5),
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

# Find the cheapest/most expensive option for each combination.
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
LOST = []  # formerly known as WON
for stats, price in valprice.items():
    #if fight(*stats):
    #    WON.append(price)
    if not fight(*stats):
        LOST.append(price)
#print(min(WON))
print(max(LOST))
