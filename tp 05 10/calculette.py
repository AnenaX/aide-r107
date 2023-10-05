def calculette(a : int, op : str, b : int) -> float:
    if op == "+":
        c = a + b
    if op == "-":
        c = a - b
    if op == "*" or op == "x":
        c = a * b
    if op == "/" or op == ":" :
        c = a / b
    if op == "%":
        c = a % b 
    return c

def verif(a : str, op : str, b : str, i):
    list = ["+","-","*","x","/",":","%"]
    while op == list[i]:
        i = i + 1
        if i == 7:
            print('Erreur: expression incorrecte')
    if a.isdigit() or b.isdigit():
        print(expr[0], expr[1], expr[2] + " = " + str(calculette(int(expr[0]), expr[1], int(expr[2]))))


ch=input("Expression à calculer ? ")
expr=ch.split()
verif(str(expr[0]), str(expr[1]), str(expr[2]), 0)





