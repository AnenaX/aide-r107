def hms(sec):
    m = sec / 60
    s = sec % 60
    h = m / 60
    minutes = m % 60
    return s, round(minutes), round(h)

sec = int(input("Entrer un nombre de secondes : "))
a, b, c = hms(sec=sec)
print(f"{c}h{b}min{a}sec")

