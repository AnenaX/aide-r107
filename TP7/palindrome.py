def estPalindrome(ch):
    # Supprimer les espaces et mettre en minuscules
    ch = ch.replace(" ", "").lower()
    
    # Comparer la chaîne avec sa version inversée
    return ch == ch[::-1]

# Programme principal pour tester la fonction
if __name__ == "__main__":
    exemples = ["bob", "radar", "11h11", "Rions noir", "Esope reste ici et se repose",
                "un art luxueux ultra nu", "No lemon no melon", "Was it a car or a cat i saw"]

    for exemple in exemples:
        resultat = estPalindrome(exemple)
        print(f"{exemple} est un palindrome : {resultat}")