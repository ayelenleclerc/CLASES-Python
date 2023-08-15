"""
Ejercicio 021
Escribir un programa que permita ingreasr dos numeros enteros e indicar si el primero es mayor, menor o igual que el segundo.
"""

num1 = 10
num2 = 21

# primer alternativa
if num1 > num2:
    print(f"{num1} > {num2}")
else:
    if num1 < num2:
        print(f"{num1} < {num2}")
    else:
        print(f"{num1} == {num2}")

# segunda alternativa
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} es menor que {num2}")
else:
    print(f"{num1} es igual que {num2}")
