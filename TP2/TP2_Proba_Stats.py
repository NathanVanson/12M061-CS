def RS(J: list) -> list:
    R = []
    # Etape 1
    n = len(J)
    k = np.random.binomial(n, 1/2)
    split1 = J[:k]
    split2 = J[k:]
    
    # Etape 2
    while split1 or split2: # Jusqu'à épuisement des 2 paquets
      n1 = len(split1) # Taille de split1
      n2 = len(split2) # Taille de split2

      p1 = n1/(n1+n2) # Probabilité de choisir dans split1
      p2 = n2/(n1+n2) # Probabilité de choisir dans split2

      chosen_list = np.random.choice(['split1', 'split2'], p=[p1, p2]) # Choisi un des deux paquets selon la proba
      if chosen_list == 'split1':
        popped = split1.pop()
        R.append(popped) # Ajoute le premier element de split1 dans R
      elif chosen_list == 'split2':
        popped = split2.pop()
        R.append(popped) # Ajoute le premier element de split2 dans R
    
    return R

# ---------- TEST ---------- #
testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(RS(testList))
# -------------------------- #

def Trajectoire(J0: list, T: int) -> list:
    tab = [J0]
    for i in range(T): # Et non pas T+1 car J0 est le premier élément de la liste
        tab.append(RS(tab[i]))
    return tab

# ---------- TEST ---------- #
testList2 = [1, 2, 3, 4]
T = 8
print(Trajectoire(testList2, T))
# ---------- TEST ---------- #