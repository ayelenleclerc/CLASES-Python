""" 
Leer un grupo de 10 datos.
Mostrar la suma
"""

suma = 0

for n in range(10):
    numero = int(input("Ingrese un numero: "))
    suma += numero


print(f"Suma: {suma}")
