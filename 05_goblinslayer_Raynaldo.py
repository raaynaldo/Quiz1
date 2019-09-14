boy_hp = 200
goblin1_hp = 165
goblin2_hp = 165
goblin3_hp = 165
boy_atk = 10
goblin1_atk = 3
goblin2_atk = 4
goblin3_atk = 1

def minus_hp(hp, dmg):
    hp -= dmg
    if hp < 0:
        return 0
    else:
        return hp

def goblin_getDamage(dmg):
    global goblin1_hp
    global goblin2_hp
    global goblin3_hp

    if goblin1_hp > 0:
        goblin1_hp = minus_hp(goblin1_hp, dmg)
        print("boy attacked goblin1 for {0} damage;goblin1 hp: {1}".format(dmg, goblin1_hp))
    elif goblin2_hp > 0:
        goblin2_hp = minus_hp(goblin2_hp, dmg)
        print("boy attacked goblin2 for {0} damage;goblin2 hp: {1}".format(dmg, goblin2_hp))
    elif goblin3_hp > 0:
        goblin3_hp = minus_hp(goblin3_hp, dmg)
        print("boy attacked goblin3 for {0} damage;goblin3 hp: {1}".format(dmg, goblin3_hp))

boyAtk_count = 0
def boy_doAttack():
    global boyAtk_count
    boyAtk_count += 1
    if boyAtk_count == 3:
        boyAtk_count = 0
        goblin_getDamage(20)
    else:
        goblin_getDamage(10)

def goblin_doAttack():
    global goblin1_hp
    global goblin2_hp
    global goblin3_hp
    global boy_hp
    if goblin1_hp > 0:
        boy_hp = minus_hp(boy_hp, goblin1_atk)
        print("goblin1 attacked boy for {0} damage;boy hp: {1}".format(goblin1_atk, boy_hp))
    if goblin2_hp > 0:
        boy_hp = minus_hp(boy_hp, goblin2_atk)
        print("goblin2 attacked boy for {0} damage;boy hp: {1}".format(goblin2_atk, boy_hp))
    if goblin3_hp > 0: 
        boy_hp = minus_hp(boy_hp, goblin3_atk)
        print("goblin3 attacked boy for {0} damage;boy hp: {1}".format(goblin3_atk, boy_hp))

turn = 1
while boy_hp > 0 and (goblin1_hp > 0 or goblin2_hp > 0 or goblin3_hp > 0):
    print("Turn ", turn)
    boy_doAttack()
    goblin_doAttack()
    turn += 1
    print()

print("Total turn : ", turn - 1)
print("The winner is")
if boy_hp > 0:
    print("Boy Hp : ", boy_hp)
else:
    if goblin1_hp > 0:
        print("Goblin 1 Hp : ", goblin1_hp)
    if goblin2_hp > 0:
        print("Goblin 2 Hp : ", goblin2_hp)
    if goblin3_hp > 0:
        print("Goblin 3 Hp : ", goblin3_hp)

