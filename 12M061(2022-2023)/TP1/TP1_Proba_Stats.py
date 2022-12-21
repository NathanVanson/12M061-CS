### Nathan VANSON, Léonie Dezempte, Mohammad Massi Rashidi UNIGE ###

### Rolling the dice ###
### Course : Probability and Statistics (TP1)

# ========== LIBRAIRES ========== #

import random
import numpy as np

# ========== FUNCTIONS ========== #

def roll_dice(num_dice):
    """Returns a list of size `num_dice` of random numbers between 1 and 6

    Args:
        num_dice (_Any_): Numbers of dice to roll

    Returns:
        list[int]: Integer list of size 'num_dice'.
    """
    return [random.randint(1,6) for _ in range(num_dice)]

def question1(roll_res):
    """Return true if all the elements of the list are identical

    Args:
        roll_res (_Any_): Throwing results

    Returns:
        _bool_: True if all the elements of the list are identical, false otherwise
    """
    return all(el == roll_res[0] for el in roll_res)

def question2(roll_res, n=3):
    """Returns true if at least one of the elements is equal to 3

    Args:
        roll_res (_Any_): Throwing results
        n (int, optional): _NONE_. Defaults to 3.

    Returns:
        _bool_: True if at least one of the elements is equal to 3, false otherwise
    """
    return any(el == n for el in roll_res)   

def question3(roll_res, n=4):
    """Return true if the sum of the elements of the list is equal to 4

    Args:
        roll_res (_Any_): Throwing results
        n (int, optional): _NONE_. Defaults to 4.

    Returns:
        _bool_: True if the sum of the elements of the list is equal to 4, false otherwise
    """
    return n == np.sum(roll_res)

def question4(roll_res):
    """Return true if one of the 3 events occurs or not

    Args:
        roll_res (_Any_): Throwing results

    Returns:
        _bool_: True if one of the 3 events occurs, false otherwise
    """
    return (question1(roll_res) or question2(roll_res) or question3(roll_res))

def question5(n):
    """Returns the probability of the question4 function after 'n' trials

    Args:
        n (_Any_): _NONE_

    Returns:
        _Any_: Probability
    """
    c = 0
    for _ in range(n):
        res = question4(roll_dice(3))
        if res : 
            c += 1
    return c / n

# ========== MAIN / TEST ========== #

if __name__ == "__main__":
    roll = roll_dice(3)
    print(roll)
    
    # Question 1 :
    print(question1(roll))
    
    # Question 2 :
    print(question2(roll))
    
    # Question 3 :
    print(question3(roll))
    
    # Question 4 :
    print(question4(roll_dice(3)))
    
    # Question 5 (example with n = 1000) : 
    print(question5(1000))
    