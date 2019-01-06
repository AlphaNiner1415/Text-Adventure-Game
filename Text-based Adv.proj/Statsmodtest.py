import random
from signal import pause


def playerattack(mycharacter,creature1):
   
        
    print ('---- \n\n It is now your turn!')
    playerhitmiss = random.randint(1,10)
    choice = input("What do you want to do?")

    #Player chooses to attack
    if choice == "attack":
        print (playerhitmiss,mycharacter['acc'])

        ##Hit
        if playerhitmiss <= mycharacter['acc']:
            print ('You attack!')
            damage2(mycharacter,creature1)
        ##Miss
        else:
            print('You miss!')
            
    #Player choose to run, the system compares the player's evade skills
    # with the monster
    
    conditions= [choice == "run", mycharacter['evade'] >= creature1['evade']]
    if all(conditions):
        print ("you successfully run away!")
        fight = False
        pause()
    elif choice == "item":
        print ("This is not yet implemented into the game yet.")
        pause()

#Computes the damage done to the creature if the attack was hit by subtracting the creature's
# hitpoints witht the player's attack.

def damage2(mycharacter,creature1):
    creature1['hp'] = creature1['hp']- mycharacter['att']
    print ("The creature now has ",creature1['hp'],' hitpoints left.')        



    

 
    
