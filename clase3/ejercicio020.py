"""
Ejercicio 020
Escribir un programa que permita ingresar dos cadenas de cadenas de caracteres e indicar si son iguales o distintas
"""

cadena1 = input("Ingrese una cadena: ")
cadena2 = input("Ingrese una cadena: ")

if cadena1 == cadena2:
    print(f"{cadena1} == {cadena2}")
    print("Las cadenas son iguales")
else:
    print(f"{cadena1} != {cadena2}")
    print("Las cadenas son distintas")

if cadena1 > cadena2:
    print(f"{cadena1} < {cadena2}")
else:
    print(f"{cadena1} >= {cadena2}")

if cadena1 <= cadena2:
    print(f"{cadena1} <= {cadena2}")
else:
    print(f"{cadena1} > {cadena2}")
