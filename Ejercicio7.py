"""
Escribir una función que reciba un fragmento de texto en una cadena de caracteres 
y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir 
otra función que reciba el diccionario generado con la función anterior y devuelva 
una tupla con la palabra más repetida y su frecuencia z.
"""
def recuento(a):
    a = (a.replace(",", "").replace(".", "").replace(":", "").replace(";", "")
     .replace("!", "").replace("¡", "").replace("?", "").replace("¿", "")
     .replace(")", " ").replace("(", " ").lower().split(" "))
    dic={}
    for i in a:
        dic[i]= (a.count(i))
    return(dic)

def mayor(b):
    maxvalor=0
    indice = ""
    for i in b:
        if b[i] > maxvalor:  
            maxvalor = b[i]
            indice = i
    return((indice, maxvalor))

while True:
    print(mayor(recuento(input("sueltalo:\n"))))

#cero IIAA, puro brain, algo de apuntes online para ver que era un diccionario y como se comporta.

