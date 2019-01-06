from time import sleep
from signal import pause
import random
monster = {}
monster['hp']=100
monster['att']=10
monster['acc']=5
monster['evade'] = 2 #A number out of 10 so 2 means 20% chance to evade

player = {}
player['max.hp'] = 100
player['hp']= 0
player['att'] = 100
player['acc'] = 4
player['evade'] = 4
player['skillpoints'] = 10
player['xp']= 0
player['lvl']=0

#Function Defining Section
def skillassign(player):
    while player['skillpoints'] > 0:
        print ("You have ", player['skillpoints'], " skillpoints left,")
        player_decision = input("what do you want to spend it on? \n plausible choices are hp, att, acc, and evade. ")
        if player_decision == "hp":
            player['skillpoints'] = player['skillpoints']-1
            player['max.hp'] = player['max.hp']+ 25
            
        if player_decision == "att":
            player['skillpoints'] = player['skillpoints']-1
            player['att'] = player['att']+ 10
            
        if player_decision == "acc":
            player['skillpoints'] = player['skillpoints']-1
            player['acc'] = player['acc']+ 0.5
            
        if player_decision == "evade":
            player['skillpoints'] = player['skillpoints']-1
            player['evade'] = player['evade']+ 0.25

        print ("=======================\n","Your current stats are: \n\n",player['max.hp'], ' hitpoints \n\n',player['att'],' attack \n\n', player['acc'], ' accuracy \n\n', player ['evade'],'/10 evasion \n\n')
    print ("That is all your skillpoints, we will now proceed to your first fight")
player['hp']= player['max.hp']
    
def damage(monster,player):
    player['hp']= player['hp']- monster['att']
    print ("You now have " ,player['hp'], " hitpoints left.")

def monster1(monster, player):        
   
    print ("======\n\n It is the monster's turn.")
    print()
    hitmissrat= random.randint(1,10)
    print(hitmissrat, " ", monster['acc'])
    print()
    ##Hit
    if hitmissrat <= monster['acc']:
        print ("The monster's attack hits!")
        damage(monster, player)
            
    ##Miss
    else:
        print ("The monster's attack misses!")

def damage2(player,monster):
    monster['hp'] = monster['hp']- player['att']
    print ("The creature now has ",monster['hp'],' hitpoints left.')
    
def playerattack(player,monster):
   
        
    print ('---- \n\n It is now your turn!')
    playerhitmiss = random.randint(1,10)
    choice = input("What do you want to do?")
    if choice == "attack":
        print (playerhitmiss,player['acc'])

        ##Hit
        if playerhitmiss <= player['acc']:
            print ('You attack!')
            damage2(player,monster)
        ##Miss
        else:
            print('You miss!')
    conditions= [choice == "run", player['evade'] >= monster ['evade']]
    if all(conditions):
        print ("you successfully run away!")
        fight = False
        pause()
    elif choice == "item":
        print ("This is not yet implemented into the game yet.")
        pause()
    

            
def damage2(player,monster):
    monster['hp'] = monster['hp']- player['att']
    print ("The creature now has ",monster['hp'],' hitpoints left.')        



    

 
    

    


#Start of things that will actually run.



fight = True
while fight:
    sleep (0.5)
    monster1(monster,player)
    if player['hp']<= 0:
        print ("========== \n\n\nYou lose!!!!")
        fight = False
    playerattack(player,monster)
    if monster['hp']<= 0:
        print ('================\n\n\n You win!!!!!!!!!!!')
        player['xp'] = player ['xp']+50
        fight = False
        monster={
            'hp' : 150,
            'att': 15,
            'evade': 3,
            'acc': 6}
        print (monster)
        

while True:
    if player['xp'] == 50 and player['lvl'] == 0:
        print ("Level up! you are now level 1!")
        player['lvl'] =1
        player['xp']= 0
        player['skillpoints'] = 5
        skillassign(player)
        fight = True
    
        
