def factorielle(n : int):
    print(f'{n}! = ',end='', sep="")
    fact = 1
    i = 1
    while i != n:
        i = i + 1
        fact = i * fact
        if i == 7:
            print(i, end='', sep="")
        else:
            print(i, '*', end='', sep="")
    print(" = ", fact, end='', sep="")

n = int(input("Entrez un nombre ? "))
factorielle(n=n)