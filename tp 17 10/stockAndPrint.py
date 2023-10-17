from random import *

MAXT = 20

myTab = []
my2ndTab = []
my3rdTab = []

def remplirTabAlea(tab):
    for i in range(0, MAXT + 1):
        r = randint(0,10)
        tab.append(r)
    print(*tab)
    return tab

def saisirTab(tab):
    for i in range(0, MAXT + 1):
        r = input(f'Case {i} ? ')
        while r.isnumeric() == False:
            r = input(f'Case {i} ? ')
        tab.append(r)
    print(*tab)

def compteur(tab):
    nbr = int(input("Quel chiffre souhaitez-vous compter ? "))
    res = 0
    for i in range(0, len(tab)):
        if tab[i] == nbr:
            res = res + 1
    print(f'Il y a {res} de fois {nbr} dans {tab} ')

t = remplirTabAlea(myTab)
saisirTab(my2ndTab)
compteur(t)