def demandeTemps():
    x=int(input("Nombre de jours"))
    if x > 365:
        return("Error")
    else:
        y=int(input("Nombre d'heures"))
        if y > 60:
            return("Error")
        else:
            z=int(input("Nombre de minutes"))
            if z > 60:
                return("Error")
            else :
                a=int(input("Nombre de secondes"))
                if a > 60:
                    return("Error")
afficheTemps(demandeTemps())

def afficheTemps(temps):
    x=temps[0]
    if x > 1:
        print(x, "jours")
    elif x != 0:
        print(x, "jour")
    else :
        pass
    y=temps[1]
    if y > 1:
        print(x, "heures")
    elif y != 0:
        print(x, "heure")
    else :
        pass
    z=temps[2]
    if z > 1:
        print(z, "minutes")
    elif z != 0:
        print(z, "minute")
    else :
        pass
    a=temps[3]
    if a > 1:
        print(a, "secondes")
    elif a != 0:
        print(a, "seconde")
    else :
        pass
afficheTemps(1,0,14,23)

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
array([[1, 2, 3],[4, 5, 6]])