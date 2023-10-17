def factorielle(n : int):
    print(f'{n}! = ',end='', sep="")
    fact = 1
    for i in range(1, n+1):
        fact = i * fact
        if i == 7:
            print(i, end='', sep="")
        else:
            print(i, '*', end='', sep="")
    print(" = ", fact, end='', sep="")

n = int(input("Entrez un nombre ? "))
factorielle(n=n)