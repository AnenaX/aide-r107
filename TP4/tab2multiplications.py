multiplicateur = [1,2,3,4,5,6,7,8,9,10]
tabRes = []
nbr = int(input("La table de multiplication de quel chiffre/nombre souhaitez-vous voir ? "))
print(f'Table de {nbr} :')
for i in range(0, len(multiplicateur)+1):
    res = i * nbr
    tabRes.append(res)
    print(f'{nbr} * {i} = {res}')
print(tabRes)