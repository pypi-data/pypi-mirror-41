
"""
Jack Treanor

Blotto entry computational framework.

"""

import numpy as np
import random
import scipy






def random_entry(soldiers,castles):
    
    """ 
    Creates a randomly generated entry consisting of a specified number of soldiers accross a specified number of castles.

    Args:

        soldiers(int): Number of soldiers
        castles(int): Number of castles

    Returns:

        entry(list): A blotto entry with "soldiers" amount of soldiers accross "castles" number of castles.

    """
    
    a = soldiers                         # temporary variable
    entry = []                           # empty entry
    
    for i in range(castles-1):
        
        b = random.randint(0,a)          # populate each castle with a random amount of soldiers between 0 and a
        entry.append(b)                  # add this to the entry
        a -= b                           # reduce a by this number
        
    entry.append(a)                      # add any remaining reserves as the last variable
    random.shuffle(entry)                # shuffle the entry vector
    
    return entry





def repeat_re(n,soldiers,castles):
    
    """ 
    Function that repeats the random_entry function n times to generate n random entries (to be used for testing). Default 100 soldiers, 10 castles 
    
    Args:

        n(int): Number of entries desired
        soldiers(int): Number of soldiers
        castles(int): Number of castles

    Returns:

        entry(list): A blotto entry with "soldiers" amount of soldiers accross "castles" number of castles.
    """

    for i in range(0,n):                            # loop n times
    
        print(random_entry(soldiers,castles))       # returns list of random entries with specified number of soldiers and castles
    
        i += 1                                      # increment i by 1
        
        
        
        

def var(entry):

    """ 
    Calculates the variance of input entry.

    Args:

        a(list): The entry you wish to calculate the varience of.

    Returns:

        b(float): The varience of entry a.

    """
    
    b = np.var(a)                         # computes the numpy variance function
    
    return b





def battle(x,y):
    
    """ 
    Simulates a game of Blotto with entry x vs entry y and displays the score of y. 


    Args:

        x(list): The entry x.
        y(list): The entry y.

    Returns:

        battle_result2(int): The score of entry y.
    """
    
    castles = [1,2,3,4,5,6,7,8,9,10]      # assigns points per castle
    i = [0,0,0,0,0,0,0,0,0,0]             # creates a string of length 10 used to test if scores are > 0 per castle


    result2 = np.subtract(y,x)            # computes y - x to determine which castles y has won

    p2 = scipy.greater(result2,i)*1       # tests to see if the score per castle is greater than 0, multiplied by 1 to convert the TRUE/FALSE output to 0 and 1 format

    battle2 = castles*p2                  # calculates the score on each castle for y

    battle_result2 = sum(battle2)         # calculates the overall score for y
    

    return battle_result2                 # displays the result




    
                              

    
def repeat_battle(y,n):
    
    """ 
    Simulates n games of Blotto of y vs n randomly generated entries, and returns the average score of y accross the games. 


    Args:

        y(list): The entry x.
        n(int): The number of games to be played.

    Returns:

        avg_score: The average of y's scores accross n matches.
    """
    
    result = []                           # empty list
    
    x = random_entry(100,10)              # generates a random opponent x
    
    for i in range(n):                    # for loop n times
        
        result.append(battle(x,y))        # adds the result of the battle between x and y to the empty string
    
        i += 1                            # increment loop by 1
        x = random_entry(100,10)          # regenerate entry x for next battle
         
    avg_score = sum(result)/n             # the average score of y accross n matches
    return avg_score                      # return the average score of y
        
    
    
    

def battle_learn(x,y):
    
    """ 
    Modified Battle Function: Plays Blotto entry x vs entry y and outputs 0 or 1 for use of the learning_alg function. 

    Note: Entries must have 10 castles each.


    Args:

        x(list): The entry x.
        y(list): The entry y.

    Returns:

        1, battle_result1(int): 1, and the overall score for entry x.
        0, battle_result2(int): 0, and the overall score for entry y.
    """
    
    castles = [1,2,3,4,5,6,7,8,9,10]      # assigns points per castle
    i = [0,0,0,0,0,0,0,0,0,0]             # creates a string of length 10 used to test if scores are > 0 per castle

    
    result1 = np.subtract(x,y)            # computes x - y to determine which castles x has won
    result2 = np.subtract(y,x)            # computes y - x to determine which castles y has won

    #print(result1,result2)

    p1 = scipy.greater(result1,i)*1       # tests to see if entry x's score per castle is greater than 0, multiplied by 1 to convert the TRUE/FALSE outout to 0 and 1 format
    p2 = scipy.greater(result2,i)*1       # tests to see if entry y's score per castle is greater than 0, multiplied by 1 to convert the TRUE/FALSE outout to 0 and 1 format

    #print(p1,p2)

    battle1 = castles*p1                  # calculates the score on each castle for x  
    battle2 = castles*p2                  # calculates the score on each castle for y

    battle_result1 = sum(battle1)         # calculates the overall score for x
    battle_result2 = sum(battle2)         # calculates the overall score for y
    

    if battle_result1 > battle_result2:   # if statement to determin winner
        return 1 and battle_result1       # return 1 if x wins
    else: return 0 and battle_result2     # return 0 if y wins
    
    






def learning_alg(n,tolerance):
    
    """ 
    An iterative function which randomly generates 2 entries then plays a match between them and the winner "stays on" and plays against a new randomly generated opponent. 
    If a winning entry is defeated,  another randomly generated entry replaces it and this is repeated n times.
    
    Entries which win "tolerance" amount of matches in a row are saved as "good" entries and are output along with their winning streak.

 Args:

        n(int): The amount of matches to be simulated.
        tolerance(n): The minimum requirement for games to be won for an entry to be considered "good.

    Returns:

       saved(list): A list containing entries which survived at least "tolerance" amount of matches, along with the respective winning streak.
    """
    
    saved = []                            # empty list
    
    j = random_entry(100,10)              # generate a random entry j
    k = random_entry(100,10)              # generate a random entry k
    
    h = 0                                 # set h = 0 (h records the number of matches won in a row per randomly generated entry)
    
    
    for i in range(n):                    # for loop n times
    
        
        c = battle_learn(j,k)             # play entry j against entry k
    
        if c > 0 :                        # if j wins
                k = random_entry(100,10)  # generate a new opponent k
                h = h+1                   # increase the recorded number of wins h by 1
                if h == tolerance:        # when h has met the desired tolerance, save this entry to the string "saved"
                                saved.append(j) 
                                
        else:                             # if k wins
            j = k                         # set k into j's place for the next round
            k = random_entry(100,10)      # generate a new opponent k
            if h > tolerance:             # if h has met the desired tolerance, save the number of matches won in a row h to the string "saved"
                                saved.append(h+tolerance)
            h = 0                         # reset h = 0 for the new entries
        
    
        #print("J =", j)                  # outputs "J =" and the entry values j
        #print("K =", k)                  # outputs "K=" and the entry values k
        
        i += 1                            # increment the loop by 1
        
    return saved








def learning_alg90(n,tolerance):
    
    """
    The learning_alg function for the case with 100 soldiers vs 90 soldiers.

    "An iterative function which randomly generates 2 entries then plays a match between them and the winner "stays on" and plays against a new randomly generated opponent. 
    If a winning entry is defeated,  another randomly generated entry replaces it and this is repeated n times.
    
    Entries which win "tolerance" amount of matches in a row are saved as "good" entries and are output along with their winning streak.""

   Args:

        n(int): The amount of matches to be simulated.
        tolerance(n): The minimum requirement for games to be won for an entry to be considered "good.

    Returns:

       savy(list): A list containing entries which survived at least "tolerance" amount of matches, along with the respective winning streak.
    """
    
    savy = []
    
    j = random_entry(100,10)             # generate a random entry j
    k = random_entry(90,10)              # generate a random entry k
    
    h = 0                                # set h = 0 (h records the number of matches won in a row per randomly generated entry)
    
    
    for i in range(n):                   # for loop n times
    
        
        c = battle_learn(j,k)            # play entry j against entry k
    
        if c > 0 :                       # if j wins                      
                k = random_entry(90,10)  # generate new opponent k
                h = h+1                  # increase the recorded number of wins h by 1
                if h == tolerance:       # if h has met the desired tolerance, save this entry k to the string "savy"
                                savy.append(k)
                                
        else:                            # if k wins
            j = random_entry(100,10)     # generate new opponent j
            if h > tolerance:            # if h has met the desired tolerance, save the number of matches won in a row h to the string "savy"
                                savy.append(h+tolerance)
            h = 0                        # reset h = 0 for the new entries
        
    
        #print("J =", j)                 # outputs "J =" and the entry values j
        #print("K =", k)                 # outputs "K=" and the entry values k
        
        i += 1                           # increment the loop by 1
        
    return savy

   
def learning_alg_n(n,tolerance,soldiers,enemy_soldiers,castles):
    
    """
    The learning_alg function for generating matches playing "soldiers" soldiers against "enemy_soldiers" soldiers accross "castles" castles.
    
    "An iterative function which randomly generates 2 entries then plays a match between them and the winner "stays on" and plays against a new randomly generated opponent. 
    If a winning entry is defeated,  another randomly generated entry replaces it and this is repeated n times.
    
    Entries which win "tolerance" amount of matches in a row are saved as "good" entries and are output along with their winning streak.""

    Args:

        n(int): The amount of matches to be simulated.
        tolerance(n): The minimum requirement for games to be won for an entry to be considered "good.
        soldiers(int): The number of soldiers on your team.
        enemy_soldiers(int): The number of soldiers your randomly generated opponent has.
        castles(int): The number of castles that Blotto will be played accross.

    Returns:

       entries(list): A list containing entries which survived at least "tolerance" amount of matches, along with the respective winning streak.




    """
    
    entries = []
    
    j = random_entry(enemy_soldiers,castles)        # generate a random entry j corresponding to "enemy_soldiers" soldiers and "castles" castles
    k = random_entry(soldiers,castles)              # generate a random entry k
    
    h = 0                                           # set h = 0 (h records the number of matches won in a row per randomly generated entry)
    
    
    for i in range(n):                              # for loop n times
    
        
        c = battle_learn(j,k)                       # play entry j against entry k
    
        if c > 0 :                                  # if j wins                      
                k = random_entry(90,10)              # generate new opponent k
                h = h+1                             # increase the recorded number of wins h by 1
                if h == tolerance:                  # if h has met the desired tolerance, save this entry k to the string "savy"
                                entries.append(k)
                                
        else:                                       # if k wins
            j = random_entry(100,10)                 # generate new opponent j
            if h > tolerance:                       # if h has met the desired tolerance, save the number of matches won in a row h to the string "savy"
                                entries.append(h+tolerance)
            h = 0                                   # reset h = 0 for the new entries
        
    
        #print("J =", j)                            # outputs "J =" and the entry values j
        #print("K =", k)                            # outputs "K=" and the entry values k
        
        i += 1                                      # increment the loop by 1
        
    return entries


def bln(x,y):
    
    """ 
    Modified Battle Function: Plays Blotto entry x vs entry y and outputs 0 or 1 for use of the learning_alg function.

    Note: Blotto entries must be of the same size (have the same number of castles). 


    Args:

        x(list): The entry x.
        y(list): The entry y.

    Returns:

        1, battle_result1(int): 1, and the overall score for entry x.
        0, battle_result2(int): 0, and the overall score for entry y.
    """
     
    a = len(x)
    b=len(y)
    
    if a == b:
        castles = np.linspace(1,a,num=a)
        i = np.zeros(a)
    
        # Castles = [1,2,3,4,5,6,7,8,9,10]      # assigns points per castle
        #i = [0,0,0,0,0,0,0,0,0,0]             # creates a string of length 10 used to test if scores are > 0 per castle

    
        result1 = np.subtract(x,y)           # computes x - y to determine which castles x has won
        result2 = np.subtract(y,x)           # computes y - x to determine which castles y has won

        #print(result1,result2)

        p1 = scipy.greater(result1,i)*1      # tests to see if entry x's score per castle is greater than 0, multiplied by 1 to convert the TRUE/FALSE outout to 0 and 1 format
        p2 = scipy.greater(result2,i)*1      # tests to see if entry y's score per castle is greater than 0, multiplied by 1 to convert the TRUE/FALSE outout to 0 and 1 format

        #print(p1,p2)

        battle1 = Castles*p1                # calculates the score on each castle for x  
        battle2 = Castles*p2                # calculates the score on each castle for y

        battle_result1 = sum(battle1)        # calculates the overall score for x
        battle_result2 = sum(battle2)        # calculates the overall score for y
    

        if battle_result1 > battle_result2:   # if statement to determin winner
            return 1 and battle_result1      # return 1 if x wins
        else: return 0 and battle_result2    # return 0 if y wins
    
    else:
        return "Entries x and y do not have the same number of castles"
        






