def bissextile (y):
    if y % 4 == 0 or y % 400 == 0:
        bi = True
        return bi
    
years = int(input("Entrer une année : "))
bi = bissextile(y=years)
if bi == True:
    print(f"L'année {years} est bissextile !")
else:
    print(f"L'année {years} n'est pas bissextile")
