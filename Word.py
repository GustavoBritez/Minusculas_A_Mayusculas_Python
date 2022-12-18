palabra = input("")
val = 0
indice = 0
mayuscula = 0
    ## 0          Posicion 1
for mayuscula in palabra:
    if(mayuscula.islower() == True):
        indice = indice +1
    else:
        val = val+1

if(indice >= val):
    print(palabra.lower()) 
else:
    print(palabra.upper())     

