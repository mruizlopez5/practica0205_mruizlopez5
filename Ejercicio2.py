"""
Escribir una función que reciba un número entero positivo y 
devuelva su factorial. Realiza el ejercicio mediante bucles 
interactivos y mediante una función recursiva.
"""

def factotrial(a):
    val = 1
    for i in range(a):
        val = val*(i+1)
    return val

print(factotrial(int(input("introduce entero positivo: "))))