import math

pi = math.pi

r = int(input("Entrez le rayon d'un cercle: "))
peri = 2*pi*r
surf = pi*r*r
print(f'perimètre = {round(float(peri),2)}, surface = {round(float(surf),2)}')