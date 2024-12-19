"""
Escribir una función que convierta un número decimal en 
binario y otra que convierta un número binario en decimal.
"""
def decTObin(a):
    binar = []
    if a == 0:
        binar.append(a)
    else:
        while a != 1 or 0:
            binar.append(a%2)
            a = (a//2)
        binar.append(a)
        binar.reverse()
    return(binar)


while True:
    print(decTObin(int(input("Introduce entero: "))))
