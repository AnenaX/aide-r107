import random

MAX=5
def initTab(T:list):
    for i in range(0, MAX):
        T.append([]) # crée une liste/tableau dans la case i de T (la case T[i] est donc 1 liste)
        for j in range(0, MAX):
            T[i].append(0) # crée 1 élément contenant 0 dans T[i]

def afficherTab(t):
# ---------------------------------------------------
monTableau=[]
initTab(monTableau)
print(monTableau)