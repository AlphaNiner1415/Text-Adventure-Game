import random
def creature(mycharacter, creature1):        
   
    print ("----\n\n It is the creature's turn.")
    print()
    hitmissrat= random.randint(1,10)
    print(hitmissrat, " ", creature1['accuracy'])
    print()
    ##Hit
    if hitmissrat <= creature1['accuracy']:
        print ("The creature's attack hits!")
        damage(creature1, mycharacter)
            
    ##Miss
    else:
        print ("The creature's attack misses!")
                
        

def damage(creature1,mycharacter):
    mycharacter['hitpoints']= mycharacter['hitpoints']- creature1['att']
    print ("You now have " ,creature1['hp'], " hitpoints left.")



                
            
            
        
    
    
