def afficher_table_ascii():
    print("Caractère | Code ASCII")
    print("------------------------")
    
    # Boucle pour parcourir les caractères ASCII
    for i in range(128):
        caractere = chr(i)  # Convertir le code ASCII en caractère
        code_ascii = ord(caractere)  # Obtenir le code ASCII du caractère
        
        # Afficher le caractère et son code ASCII
        print(f"{caractere:^9} | {code_ascii:^10}")

# Appeler la fonction pour afficher la table ASCII
afficher_table_ascii()