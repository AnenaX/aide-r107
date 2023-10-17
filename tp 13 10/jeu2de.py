from random import *

joueur1 = 0
joueur2 = 0

def lancer2Des(joueur):
    n = randint(1, 6)
    m = randint(1, 6)
    print(f"Dé 1 : {n} - Dé 2 : {m}")
    if n == m :
        if n == 1 or n == 2 or n == 4  or n == 5:
            joueur = joueur + 5
            print(f"Le score du Joueur est maintenant de {joueur} suite à un gain de 5 points")
        elif n == 6:
            joueur = joueur + 25
            print(f"Le score du Joueur est maintenant de {joueur} suite à un gain de 25 points")
        elif n == 3:
            joueur = 0
            print(f"Le score du joueur a été remis à zéro suite à un double 3")
        else:
            return

def fin2Partie(point1, point2):
    print("---- Fin de Partie ----")
    print(f"Joueur 1 : {point1}")
    print(f"Joueur 2 : {point2}")
    if point1 == 50:
        print("Le Joueur 1 est gagnant !")
    else:
        print("Le Joueur 2 est gagnant !")

while joueur1 != 50 or joueur2 != 50:
    print("Joueur 1")
    lancer2Des(joueur1)
    print("Joueur 2")
    lancer2Des(joueur2)      

fin2Partie(joueur1, joueur2)
