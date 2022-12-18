import random
def Alea():
    num = random.randint(1, 10)
    return num

def primo():
    num = Alea()
    if (num < 8):
        print("El numero generado es pequenio {}")
    else:
        print("El numero generado es grande")
    
primo()