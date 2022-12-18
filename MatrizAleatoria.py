import random
def Alea():
    num = random.randint(13, 50)
    return num

print("Ingrese Numero de Filas")
Filas = int(input())
print("Ingrese Numero de Columnas")
Columna = int(input())
matriz = []
for i in range(Filas):
    matriz.append([])
    for j in range(Columna):
        Valor = Alea()
        matriz[i].append(Valor)

print()
for Filas in matriz:
    print("[", end=" ")
    for c in Filas:
       print("{}".format(c), end=" ")
    print("]",end=" ")
    