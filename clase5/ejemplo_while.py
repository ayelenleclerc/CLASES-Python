""" 
Leer una lista de numeros hasta que se ingrese un cero. Mostrar la suma.

lista1 ===>1,5,4,7,8,5,4,5,8,74,5,8,7,0
lista2 ===>4,5,8,74,5,8,7,0
lista3 ==> 0
"""

# ANTES (PARA TODOS)
suma = 0

numero = int(input("Ingrese un numero: "))
while numero != 0:
    # DURANTE(PARA CADA DATO)
    numero = int(input("Ingrese un numero: "))
    suma += numero

# DESPUES(TOTALES)
print(f"La suma de todos los numeros es: {suma}")
