import re

def verif(date):
    list = [4, 6, 9, 10]
    date = [int(num) for num in re.findall(r'\d+', string=date)]
    print(date)
    if date[0] > 31:
        print("Il y a maximum de 31 jours dans un mois !")
        exit()
    if date[1] > 12:
        print("Il n'y a que 12 mois dans une année !")
        exit()
    if date[2] < 1970 or date[2] > 2050:
        print("Merci d'entrée une année entre 1970 et 2050 !") 
        exit()
    for month in list:
        if date[0] > 30:
            print("Cette date n'est pas valide !") 
            break
    if month == 2 and date[0] > 28:
        if date[2] % 4 == 0 and date[2] % 100 != 0 or date[2]%400==0:
            print(f'{date[0]}/{date[1]}/{date[2]} est valide')
            exit()
        else:
            print(f'{date[0]}/{date[1]}/{date[2]} n\'est pas valide')
            exit()
    print(f'{date[0]}/{date[1]}/{date[2]} est valide')

    

dateEntered = input("Entrez une date valide au format: jj/mm/aaaa : ")
if len(dateEntered) > 10:
    print("Date Invalide")
verif(date=dateEntered)