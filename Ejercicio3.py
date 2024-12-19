"""
Escribir una función que calcule el área de un círculo y 
otra que calcule el volumen de un cilindro usando la primera función.
"""

def Acirc(a):
    A = pow((3.1416*a), 2)
    return A

def Vcilin(a, b):
    V = Acirc(a)*b
    return V

Radio = float(input("Introduce radio: "))
Altura = float(input("Introduce altura: "))

print("El area del ciruclo es:", round(Acirc(Radio), 2),"u")
print("El volumen del iclindro es:", round(Vcilin(Radio, Altura), 2), "u")

