# -*- coding: utf-8 -*-
"""
Text console RPG

Stats:
* health
* strength (attack power)
* agility (evasion probability)

stat_list = []

Mobs
* Level 1 -- Crab -- 1 gold 
* Level 2 -- Demon -- 2 gold
* Level 3 -- Dragon -- 4 gold

mobs_list = []

Levels -> stat upgrades
Lvl 1 exp (0/100)
    * health 100
    * gold 5
    * stren
Lvl 2 exp(100/200)
    * health x2 (== 200)
Lvl 3 exp (200/400)
    * health x2 (== 400)

Items
* gold
* health potion (lvl 1-3) -- restores 80/160/320 hp -- 1/2/4 gold
* steel sword ( +100% strength )
* wooden shield ( +50% agility )
* leather armor ( +50% health )

items_list = []
"""

print "Welcome to text console RPG!"
prompt = '> ' 

while True:
    command = raw_input(prompt)
