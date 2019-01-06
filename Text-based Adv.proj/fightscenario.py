import Statsmodtest
import monster
from time import sleep

##Player's stats defined here##

## Hashtable, a multi variable list,
## allowing you to add multiple elements into the list

fight = False

turnentity = 0

creatureattack = 0
def fightfunction(mycharacter, creature1,fight):
    while fight:
        sleep(0.5)

        #Creature's Turn:
        monster.creature(mycharacter, creature1)
        
        if mycharacter['hitpoints']<= 0:
            print ("----- \n\n\nYou lose!!!!")
            fight = False
        
        #Player's turn:    
        Statsmodtest.playerattack(mycharacter,creature1)
        
        if creature1['hp'] <= 0:
            print ("----- \n\n\nYou win!!!!")
            fight = False
            monster_death = 1
            return monster_death
        
    
    
    
