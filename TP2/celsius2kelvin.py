def celsius2kelvin(Tc):
    return Tc+273.15

Tc = float(input("Choissiez une température en °C :"))
print(f"{Tc}°C équivaut à {round(celsius2kelvin(Tc=Tc), 2)}°K")
