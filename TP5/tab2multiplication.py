MAX=10

def initTab(T:list):
    for i in range(0, MAX+1):
        T.append([]) # crée une liste/tableau dans la case i de T (la case T[i] est donc 1 liste)
        for j in range(0, MAX+1):
            T[i].append(0)

def calculTableMult(T:list):
    T[0][0] = '*'
    for i in range(1,MAX+1):
        T[0][i]=i
        T[i][0]=i
    for i in range(1, MAX+1):
        for j in range(1, MAX+1):
            T[i][j]= T[0][i] * T[j][0]

def calculTableMult2(T:list):
    T[0][0] = '*'
    for i in range(1,MAX+1):
        T[0][i]=i
        T[i][0]=i
    for i in range(1, MAX+1):
        for j in range(1, MAX+1//2):
            T[i][j]= T[0][i] * T[j][0]
            T[j][i]=T[i][j]

def afficherTab(t:list):
    for i in range(0,MAX+1):
        print(*t[i])

def sep(t:str):
    print("---------------------------------------------")
    print(t)
    print("---------------------------------------------")

tableau=[]
sep("Normal")
initTab(tableau)
calculTableMult(tableau)
afficherTab(tableau)
sep("Symétrie")
calculTableMult2(tableau)
afficherTab(tableau)
