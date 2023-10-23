import random

MAX=5

def initTab(T:list):
    for i in range(0, MAX):
        T.append([]) # crée une liste/tableau dans la case i de T (la case T[i] est donc 1 liste)
        for j in range(0, MAX):
            T[i].append(0) # crée 1 élément contenant 0 dans T[i]

def afficherTab(t:list):
    res = 0
    nbr = int(input("Quelle nombre souhaitez-vous compter dans le tableau : "))
    for i in range(0,MAX):
        print(*t[i])
    for i in range(0, MAX):
        for j in range(0, MAX):
            if t[i][j] == nbr:
                res = res + 1
    print(f'Il y a {res} de fois {nbr} dans {t}')

def tableauV1(T:list):
    n = len(T)
    for i in range(0, MAX):
        T[i][n//2]=1
        T[n//2][i]=1

def reinitTab(T:list):
    for i in range(0, MAX):
        for j in range(0, MAX):
            T[i][j]=0 # crée 1 élément contenant 0 dans T[i]

def tableauV2(T:list):
    for i in range(0, MAX):
        for j in range(0, MAX):
            if j == i:
                T[i][j]=1
        T[i][MAX - 1 - i] = 1

def tableauV3(T:list):
    for i in range(0, MAX):
        for j in range(0, MAX):
            if j%2 == 0 :
                T[i][j]=1

def tableauV4(T:list):
    n = len(T)
    for i in range(0, MAX):
        T[i][n//2]=1
        T[n//2][i]=1
    for i in range(0, MAX):
        for j in range(0, MAX):
            if j == i:
                T[i][j]=1
        T[i][MAX - 1 - i] = 1

def tableauV5(T:list):
    for i in range(0, MAX):
        for j in range(0, MAX):
            T[i][j]=random.randint(0,99)

def sep():
    print("---------------------------------------------")

monTableau=[]
initTab(monTableau)
afficherTab(monTableau)
reinitTab(monTableau)
sep()
tableauV1(monTableau)
afficherTab(monTableau)
reinitTab(monTableau)
sep()
tableauV2(monTableau)
afficherTab(monTableau)
reinitTab(monTableau)
sep()
tableauV3(monTableau)
afficherTab(monTableau)
reinitTab(monTableau)
sep()
tableauV4(monTableau)
afficherTab(monTableau)
reinitTab(monTableau)
sep()
tableauV5(monTableau)
afficherTab(monTableau)
reinitTab(monTableau)
sep()