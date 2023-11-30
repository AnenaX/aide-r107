def hamming(mot1, mot2):
    # Vérifier si les deux mots ont la même longueur
    if len(mot1) != len(mot2):
        return -1
    
    # Initialiser la distance de Hamming à 0
    distance = 0
    
    # Parcourir les deux mots et comparer les caractères
    for i in range(len(mot1)):
        if mot1[i] != mot2[i]:
            distance += 1
    
    return distance

# Exemples d'utilisation
print(hamming("bonjour", "bonsoir"))  # Retourne 2
print(hamming("facteur", "facture"))  # Retourne 3
print(hamming("python", "php"))        # Retourne -1
print(hamming("1011101", "1001001"))   # Retourne 2

