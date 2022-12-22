### Nathan VANSON, Léonie Dezempte, Mohammad Massi Rashidi UNIGE ###

### Rolling the dice ###
### License : GNU Public License (GPL)
### Course : Probability and Statistics (TP1)

# ========== LIBRAIRES ========== #

import random
import numpy as np

# ========== FUNCTIONS ========== #

def roll_dice(num_dice: int) -> list:
  """
  Returns a list of size 'num_dice' of random numbers between 1 and 6

  Parameters
  ----------
      num_dice : int
        Numbers of dice to roll

  Returns
  ----------
      list[int]
        Integer list of size 'num_dice'.
  """
  return [random.randint(1, 6) for _ in range(num_dice)]

def question1(roll_res: list) -> bool:
  """
  Return true if all the elements of the list are identical
  
  Parameters
  ----------
      roll_res : list[int]
        Throwing results 

  Returns
  ----------
      bool 
        True if all the elements of the list are identical, false otherwise
  """
  return all(el == roll_res[0] for el in roll_res)

def question2(roll_res: list, n=3) -> bool:
  """
  Returns true if at least one of the elements is equal to 3
  
  Parameters
  ----------
      roll_res : list[int]
        Throwing results

      n : int (optional)
        Defaults to 3
  
  Returns
  ----------
      bool
        True if at least one of the elements is equal to 3, false otherwise
  """
  return any(el == n for el in roll_res)

def question3(roll_res: list, n=4) -> bool:
  """
  Return true if the sum of the elements of the list is equal to 4
  
  Parameters
  ----------
      roll_res : list[int]
        Throwing results

      n : int (optional)
        Defaults to 4 

  Returns
  ----------
      bool
        True if the sum of the elements of the list is equal to 4, false otherwise
  """
  return n == np.sum(roll_res)

def question4(roll_res: list) -> bool:
  """
  Return true if one of the 3 events occurs or not

  Parameters
  ----------
      roll_res : list[int]
        Throwing results

  Returns
  ----------
      bool
        True if one of the 3 events occurs, false otherwise
  """
  return (question1(roll_res) or question2(roll_res) or question3(roll_res))

def question5(n: int) -> float:
  """
    Returns the probability of the question4 function after 'n' trials

    Parameters
    ----------
        n : int
            Number probability test
            
    Returns
    ----------
        float 
            Probability
    """
  c = 0
  for _ in range(n):
    res = question4(roll_dice(3))
    if res :
        c += 1
  return c/n  

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
    