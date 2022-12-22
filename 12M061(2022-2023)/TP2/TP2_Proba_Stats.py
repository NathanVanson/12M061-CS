### Nathan VANSON UNIGE ###

### Card shuffling by the riffle shuffle ###
### License : GNU Public License (GPL)
### Course : Probability and Statistics (TP2)

# ========== LIBRAIRES ========== #

import random
import numpy as np
import matplotlib.pyplot as plt

# ========== FUNCTIONS ========== #

def RS(J: list) -> list:
    """
    Apply a Riffle Shuffle to a list to produce a new list
    
    Parameters
    ----------
      J : list
        List on which we apply the Riffle Shuffle

    Returns
    ----------
      R : list
        Riffle Shuffle result applied on J
    """
    J = list(J)
    R = []
    # Step 1
    n = len(J)
    k = np.random.binomial(n, 1/2)
    split1 = J[:k] 
    split2 = J[k:]
    
    # Step 2
    while split1 or split2: # Until the 2 packs are sold out
      n1 = len(split1)
      n2 = len(split2)

      p1 = n1/(n1+n2) # Probability of choosing in split1
      p2 = n2/(n1+n2) # Probability of choosing in split2

      chosen_list = np.random.choice(['split1', 'split2'], p=[p1, p2]) # Choose one of the two packages according to the probability
      if chosen_list == 'split1':
        popped = split1.pop()
        R.append(popped) # Add the first element of split1 in R
      elif chosen_list == 'split2':
        popped = split2.pop()
        R.append(popped) # Add the first element of split2 in R
    
    return R

def Trajectoire(J0: list, T: int, shuffle=RS) -> np.ndarray:
    """
    Application of a trajectory on a list leaving a list whose first element is this 
    one and whose following elements are deduced successively by application of RS

    Parameters
    ----------
        J0 : list
            List in which we apply the trajectory (it also corresponds to the first element of the output list)

        T : int
            Range of the trajectory
            
        shuffle : function
            Function used to shuffle the list (default is RS)

    Returns
    ----------
        Tab : np.ndarray
            The final np array after applying the trajectory (numpy)
    """
    J0 = list(J0)
    Tab = [J0]
    #print(Tab)
    for i in range(T): # And not T+1 because J0 is the first element of the list
        Tab.append(shuffle(Tab[i]))
    return np.asarray(Tab)

# ========== MAIN / TEST ========== #

if __name__ == "__main__":

  # Question 1 :
  testList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(RS(testList1))

  # Question 2 :
  testList2 = [1, 2, 3, 4]
  T = 8
  print(Trajectoire(testList2, T))

  # Question 3 / 4 :
  n = 52
  J0 = range(n)
  Ju = np.arange(n)
  T = 10
  Tk = 1000
  J = Trajectoire(J0, T)
  
  I_Values = []
  for Jt in J:
      Jt = Trajectoire(Jt, Tk)
      P = np.asarray([np.bincount(Jt[:, k], minlength=n)/Tk for k in range(n)])
      Pu = np.asarray([np.bincount(Ju, minlength=n)/n for k in range(n)])
      I_Values.append(np.max(np.abs(n * P - 1)))
      
      np.random.shuffle(Ju) # Uniform random permutations

  t = np.where(I_Values[np.argmin(I_Values)] < 1, np.argmin(I_Values), None) # Minimal t
  print("Valeur de t minimum pour I(Jt) < 1 : ", t)

  I_u = np.max(np.abs(n * Pu - 1))
  
  plt.plot(I_Values, label = 'I(Jt)')
  plt.axvline(t, color = 'r', label = 't Minmimal pour I(Jt) < 1')
  plt.axhline(I_u, color = 'g', label = 'J Uniforme')
  plt.xlabel("t")
  plt.ylabel("I(Jt)")
  plt.legend() 
  plt.show()
  