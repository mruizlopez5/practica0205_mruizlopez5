"""
Escribir una función que reciba una muestra 
de números en una lista y devuelva su media.
"""

def media(a):
    sum = 0
    for i in a:
        sum = sum + i
    sum = sum/(len(a))
    return sum

while True:
    lista=[]
    i = True
    while i != False:
        a = input("Intorduce numero (dale a enter vacio para terminar): ")
        if a != "":
            lista.append(int(a))
        else:
            i = False
    print("Los valores introducidos son:",lista)
    print("La media de los valores es:",round(media(lista),2))

