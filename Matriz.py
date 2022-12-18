import random
def Alea():
    num = random.randint(13, 50)
    return num


print("Ingrese Numero de Filas")
Filas = int (input())
print("Ingrese Numero de Filas")
Columnas = int (input())  
matriz = []
### Carga la matriz con vacios ###
for i in range(Filas):
    matriz.append([])
    for j in range(Columnas):
        valor = Alea()
        matriz[i].append(valor)

print()
for Filas in matriz:
    print("[", end=" ")
    for elemento in Filas:
       print("{}".format(elemento), end=" ")
    print("]",end=" ")
    













