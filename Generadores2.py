def lista_ciudades(*ciudades):
    for elemento in ciudades:
        for Subelemento in elemento:
            yield from Subelemento
## Este objeto  responde a la funcion linea 1 
ciuades_devueltas = lista_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciuades_devueltas))
print(next(ciuades_devueltas))
print(next(ciuades_devueltas))
print(next(ciuades_devueltas))
print(next(ciuades_devueltas))
print(next(ciuades_devueltas))
print(next(ciuades_devueltas))
print(next(ciuades_devueltas))