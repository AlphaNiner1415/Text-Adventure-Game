def health(healthstat):
    print ("Player health is: " + str(healthstat))
def attack(attackbase, attackbonus):
    print ("Player attack is: " + str(attackbase + attackbonus))
def level(playerlevel):
    print ('Player level is: ' + str(playerlevel))

def levelup(mycharacter):
    if (mycharacter['xp'] >= 100 and mycharacter['lvl'] == 0):
        mycharacter['lvl'] = 1
        mycharacter['xp'] = mycharacter ['xp'] - 100
        mycharacter['att'] = 10
        mycharacter['accuracy'] = 1
        
        
    elif (mycharacter['xp'] >= 200 and mycharacter['lvl'] == 1):
        mycharacter['lvl']  = 2
        mycharacter['xp'] = mycharacter ['xp']-200
        mycharacter['att'] = 20
        mycharacter['accuracy'] = 2
        
        
    elif (mycharacter['xp'] >= 300 and mycharacter['lvl']  == 2):
        mycharacter['lvl']   = 3
        mycharacter['xp'] = mycharacter ['xp'] - 300
        mycharacter['att'] = 30
        mycharacter['accuracy'] = 3
        
    else:
        print ("Player level is still: "+ str(mycharacter['lvl']))
    
