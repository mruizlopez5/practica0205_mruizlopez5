"""
Escribir una función que reciba una muestra de números en 
una lista y devuelva otra lista con sus valores al cuadrado.
"""
def cuadrados_lista(a):
    new = []
    for i in a:
        new.append(pow(i, 2))
    return new


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
    print("Sus valores al cuadrdado son:",cuadrados_lista(lista))