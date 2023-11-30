from random import randint

de1 = [0, 0, 0]
de2 = [0, 0, 0]
de3 = [0, 0, 0]

def lancerDe() -> int:
        n = randint(1,6)
        return n

def tri3Nombres(tab) -> int:
    x = tab[0]
    y = tab[1]
    z = tab[2]
    if x > y and x > z :
        if z > y:
            tab = [x, z, y]
        else:
            tab = [x, y, z]
    if x < y and x > z :
        if z > y:
            tab = [z, x, y]
        else:
            tab = [y, x, z]
    if x < y and x < z :
        if z > y:
            tab = [z, y, x]
        else:
            tab = [y, z, x]
    print(tab)


de1[0] = lancerDe()
de1[1] = lancerDe()
de1[2] = lancerDe()

de2[0] = lancerDe()
de2[1] = lancerDe()
de2[2] = lancerDe()

de3[0] = lancerDe()
de3[1] = lancerDe()
de3[2] = lancerDe()

tri3Nombres(de1)
tri3Nombres(de2)
tri3Nombres(de3)