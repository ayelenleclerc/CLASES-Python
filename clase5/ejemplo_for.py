""" 
Leer un grupo de 10 datos.
Mostrar la suma
"""
desde = 0
cant = 10
salto = 2

print(range(desde, cant, salto))
print(len(range(desde, cant, salto)))
print(list(range(desde, cant, salto)))


for n in range(desde, cant, salto):
    print(n, end=" ", sep="-")
