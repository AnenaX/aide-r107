def celsius2fahrenheit(Tc : float):
    return 9*Tc/5+32

def celsius2kelvin(Tc : float):
    return Tc+273.15

choice = int(input("[1] -> °C to °F\n[2] -> °C to °K \nEntrer 1 ou 2:"))

if choice == 1:
    Tc = float(input("Choissiez une température en °C :"))
    print(f"{Tc}°C équivaut à {round(celsius2fahrenheit(Tc=Tc), 2)}°F")
elif choice == 2 :
    Tc = float(input("Choissiez une température en °C :"))
    print(f"{Tc}°C équivaut à {round(celsius2kelvin(Tc=Tc), 2)}°K")
else:
    print("Error : wrong value")