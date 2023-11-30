def encadrer(chaine:str) :
    n = len(chaine)
    splited = chaine.split(" ")
    n = n + 2
    print("+",n*"-", "+")
    for p in splited[p]:
        print("| ",splited[p], " |")
    print("+",n*"-", "+")

chaine = input("Ecrivez une phrase à encadrer : ")
encadrer(chaine=chaine)