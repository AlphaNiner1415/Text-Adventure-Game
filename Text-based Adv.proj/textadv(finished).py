bottle_mrm_pup = 1
import fightscenario
from pprint import pprint
userloc = ''
import time
import random
creature1={}
creature1['hp'] = 100
creature1['att'] = 10
creature1['accuracy']= 5
creature1['damagereceived'] = 20
creature1['evade'] =4

mycharacter={}
mycharacter['inventory']=[]
mycharacter['armslot'] = ''
mycharacter['handslot']=''
mycharacter['bodyslot']=''
mycharacter['accessories']=''
mycharacter['headslot']=''
mycharacter['inventory'].extend(['confortable clothes', 'comfortable pants', 'fists'])
##Player's stats defined here##
mycharacter['xp'] = 0
mycharacter['lvl'] = 0
## Hashtable, a multi variable list,
## allowing you to add multiple elements into the list
mycharacter['att'] = 10
mycharacter['acc'] = 5
mycharacter['hitpoints'] = 100
mycharacter['evade'] = 5
loop = 1
sword_eqp = 0
forest_loc = 0
monster_death = 0

if sword_eqp == 1:

    mycharacter['armslot'] = "sword"
    mycharacter['att'] = mycharacter['att'] + 2

def addingitems(mycharacter,item):

    print ("You add the", item, "to your inventory.")
    mycharacter['inventory'].append (item)


#---------------------------------------------------------------------------------------------#
def takeinventory(mycharacter):
    print ("You currently have: \n\n ---------------------------------------\n")
    for item in mycharacter['inventory']:
        print (item)
        print ("\n ---------------------------------------\n")

Liner = "--------------------------------------------------------------------"
sword_in_lvingrm_still_there = 1
bottle_in_mainroom_still_there = 1

#Starting function, First loop
 
def start (dir2=''):
    global forest_loc
    global loop
    global Liner
    pickedup = False
    while loop == 1:
        
        userloc = "House's door"
        if pickedup == True:
            print("You are at the house's door.")
            print("Type north, south, east, or west to go the respective directions, alternatively you can type n,s,e,w instead.")
        else:
            print("You are at the house's door. There is a parchment lying on the ground.")
            print("Type north, south, east, or west to go the respective directions, alternatively you can type n,s,e,w instead. Type pickup to pickup the parchment.")
        dir2 = input("")
        if dir2 == "pickup":
            print(Liner)
            print ("\n\"Welcome to the alpha version of this text adventure game! \nyour goal in this game is to discover the temple ruins of Shinicarta. If you seek a weapon look inside the house.\"\n ")
            print("You put down the parchment.\n")
            print(Liner)
            pickedup = True
        if dir2 == "west" or dir2 == "w":
            print ("You cannot go there.")

        elif dir2 == "east" or dir2 =="e":
            print('You cannot go there.')

        elif dir2 == "north" or dir2 =="n":
            loop = 2
            print (loop)

            mainroom(bottle_in_mainroom_still_there,dir1="")
            return loop
        elif dir2 == "south" or dir2 =="s":
            forest_loc = 1
            loop = 0
        elif dir2 == "inventory":
            takeinventory(mycharacter)

#Main room function, second loop
def mainroom (bottle_in_mainroom_still_there,dir1=""):
    global loop
    print (loop)
    while loop == 2:
        userloc = "Main Hall"
        print("You are in the Main Hall of the house.")
        print("There is another parchment lying on the ground. Type \"pickup\" to pickup the parchment.")
        if bottle_in_mainroom_still_there ==1:
            print ("There is a bottle in the cupboard. Type \"take\" to pickup the bottle.")
        dir1 = input("")

        if dir1 == "west" or dir1 == "w":
            loop = 3
            bedroom(bottle_in_mainroom_still_there)
            return loop
        elif dir1 == "east" or dir1 =="e":
            loop = 4
            bathroom(bottle_in_mainroom_still_there)
            return loop
        elif dir1 == "north" or dir1 =="n":
            loop = 5
            livingroom(bottle_in_mainroom_still_there)
            return loop
        elif (dir1 == "south" or dir1 =="s"):
            loop = 1
            start()
            return loop
        elif (dir1 == "look" or dir1 == "l"):
            if bottle_in_mainroom_still_there == 1:
                print ("There is a bottle in the cupboard.")
            print("There is another parchment lying on the ground.")
        if dir1 == "pickup":
            print("You pick up the parchment.")
            print ("\nLooking for victory is you,\n"
                   "then listen for a clue,\n"
                   "where the Sun rise,\n"
                   "right of that is your prize.\n"
                   "Go you must through paths of green,\n"
                   "past the test, past the creatures in between,\n"
                   "end of green lies your prize.\n")
            print ("You put down the parchment.")

        conditions = [dir1 == "take", bottle_in_mainroom_still_there == 1]
        if all(conditions):
            addingitems(mycharacter, "bottle")
            bottle_in_mainroom_still_there = 0

        if dir1 == "inventory":
            takeinventory(mycharacter)


##Bed room function, third loop

def bedroom (bottle_in_mainroom_still_there,dir3=''):
    global loop
    while loop == 3:
        userloc = 'bedroom'
        print("You are in the bedroom of the house.")
        dir3 = input("")
        if dir3 == "west" or dir3 == "w":
            print ("You cannot go there.")

        elif dir3 == "north" or dir3 =="n":
            print('You cannot go there.')

        elif dir3 == "east" or dir3 =="e":
            loop = 2
            mainroom(bottle_in_mainroom_still_there,dir1="")
            return loop

        elif dir3 == "south" or dir3 =="s":
            print('You cannot go there.')

        elif dir3 == "inventory":
            takeinventory(mycharacter)

#Bathroom Function fourth loop.
def bathroom (bottle_in_mainroom_still_there,dir4=""):
    global loop
    while loop == 4:
        userloc = 'bathroom'
        print("You are in the bathroom of the house.")
        dir4 = input("")
        if dir4== "west" or dir4 == "w":
            loop = 2
            mainroom(bottle_in_mainroom_still_there,dir1="")
        elif dir4 == "east" or dir4 =="e":
            print ('You cannot go there. ')
        elif dir4 == "south" or dir4 =="s":
            print  ('You cannot go there. ')
        elif dir4 == "inventory":
            takeinventory(mycharacter)
        elif dir4 =="look":
            print("You are in the bathroom of the house.")


#Living room function, fifth loop.
def livingroom (dir5=""):
    global sword_eqp
    global loop
    global sword_in_lvingrm_still_there
    while loop == 5:
        userloc = 'livingroom'
        print("You are in the Living room of the house.")
        dir5 = input("")

        if dir5 == "west" or dir5 == "w":
            print ('You cannot go there. ')


        elif dir5 == "east" or dir5 =="e":
            print ('You cannot go there. ')

        elif dir5 == "north" or dir5 =="n":
            print  ('You cannot go there. ')

        elif dir5 == "south" or dir5 =="s":
            loop = 2
            mainroom(bottle_in_mainroom_still_there,dir1="")
            return loop
        elif dir5 == "inventory":
            takeinventory(mycharacter)
        conditions = [dir5 == "equip", sword_eqp == 0]
        if all(conditions):
                print ("You equip the sword.")
                mycharacter['inventory'].remove('sword')
                sword_eqp = 1


        elif dir5 == "look":
            if sword_in_lvingrm_still_there == 1:
                  print ("There is a sword lying next to the couch. Type pickup to pick up the sword.")
            else:
                  print ("There is a couch sitting in the room.")
        elif dir5 == 'pickup':
            if sword_in_lvingrm_still_there == 1:
                  addingitems(mycharacter,'sword')
                  sword_in_lvingrm_still_there = 0
            else:
                print("You have already picked up the sword.")
    return sword_eqp




userint = ''
start(userint)

#Forest Function, 6th loop:
gameover = False
while gameover == False:


    # Forest tile 1
    forest_loc =1
    while forest_loc == 1:
        print("You are surrounded by a forest, there is light coming from the north.")
        dir6 = input ('Which way do you want to go?')
        if (dir6 == "north") or (dir6 == "n"):
            print("Why not go here??")
            loop = 1
            start(userint)
            forest_loc = 0
        elif (dir6 == 'west') or (dir6 =='w'):
            ## <----This symbol will be included where there is a pending testing in code
            # I'm trying to find out whether or not I need to convert forest_loc to a string
            # first before I assign it a string value.
            print (type(forest_loc))
            forest_loc = "D"
            print (type(forest_loc))
            print (forest_loc)
            print (dir6)

        elif (dir6 == 'east') or (dir6 =='e'):
            ##
            forest_loc = 'A'

        elif (dir6 == "south") or (dir6 == "s"):
            forest_loc = 2


    #Forest tile 2
    while forest_loc == 2:
        print(forest_loc)
        print("You are surrounded by trees in every direction.")
        dir6 = input ('Which way do you want to go?')
        if dir6 == 'west' or dir6 == 'w':
            forest_loc = 'E'
        elif dir6 == 'north' or dir6 == 'n':

            forest_loc = 1
        elif dir6 == 'east' or dir6 == 'e':
            ##
            forest_loc = 'B'
        elif dir6 == 'south' or dir6 == 's':
            forest_loc = 3

    while forest_loc == 3:
        print("You are surrounded by trees, there is a clearing in the south.")
        dir6 = input("Which way do you want to go?")
        if dir6 == 'north' or dir6 == 'n':
            forest_loc = 2
        elif dir6 == 'south' or dir6 == 's':
            forest_loc = 'W'
        elif dir6 == 'west' or dir6 == 'w':
            forest_loc = 'F'
        elif dir6 == 'east' or dir6 == 'e':
            forest_loc = 'B'

    while forest_loc == 'A':
        print("You are surrounded by a forest on all sides.")
        dir6 = input("Which way do you want to go?")
        if dir6 == 'south' or dir6 =='s':
            forest_loc = 'B'
        elif dir6 == 'east' or dir6 =='e':
            print ("The forest becomes too thick for you to continue.")
            forest_loc = 'A'
        elif dir6 == 'north' or dir6 =='n':
            print ("The forest becomes too thick for you to continue.")
            forest_loc = 'A'
        elif dir6 == 'west' or dir6 =='w':
            forest_loc = 1

    while forest_loc == 'B':
        dir6 = input("Which way do you want to go?")
        if dir6 == 'north' or dir6 =='n':
            forest_loc = 'A'
        elif dir6 == 'south' or dir6 =='s':
            forest_loc = 'C'
        elif dir6 == 'west'  or dir6 =='w':

            forest_loc = 2
        elif dir6 == 'east' or dir6 == 'e':
            print ("The forest becomes too thick for you to continue.")

    while forest_loc == 'C':
        dir6 = input("Which way do you want to go?")
        if dir6 == 'north' or dir6 == 'n':
            forest_loc = 'B'
        elif dir6 == 'west'  or dir6 == 'w':
            forest_loc = 3

    while forest_loc == "D":
        print ("You are deep inside the forest.")
        print (forest_loc)
        dir6 = input("Which way do you want to go?")
        if dir6 == 'north' or dir6 =='n':
            print ("The forest becomes too thick for you to continue.")

        elif dir6 == 'south' or dir6 =='s':
            forest_loc = 'E'
        elif dir6 == 'west'  or dir6 =='w':
            print ("The forest becomes too thick for you to continue.")
            forest_loc = 'D'
        elif dir6 == 'east'  or dir6 =='e':
            forest_loc = 1

    while forest_loc == 'E':
        print ("You are deep inside the forest, to the west the forest becomes too thick for you to continue.")
        dir6 = input("Which way do you want to go?")
        if dir6 == 'north' or dir6 =='n':
            forest_loc = 'D'
        elif dir6 == 'south' or dir6 =='s':
            forest_loc = 'F'
        elif dir6 == 'west'  or dir6 =='w':
            print ("The forest becomes too thick for you to continue.")

    while forest_loc == 'F':
        if monster_death == 0:
            fight = True
            print("A creature jumps out of nowhere.")
            fightscenario.fightfunction(mycharacter, creature1, fight)
        dir6 = input("Which way do you want to go?")
        if dir6 == 'east' or dir6 =='e':
            forest_loc = 3

        elif dir6 == 'south' or dir6 =='s':
            print ("The forest becomes too thick for you to continue.")
        elif dir6 == 'west'  or dir6 =='w':
            print ("The forest becomes too thick for you to continue.")

    while forest_loc == 'W':
        print("Congratulations! You have found the temple ruins of Shicarta!")
        print ("You recover all the loss gold from the temple and sell it to go on and become one of the richest billionaires in the world.")
        print ("That's the whole game!\n Thanks for playing!\n ----------------------------------------------------------------------")
