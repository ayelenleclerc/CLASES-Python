"""
  Ejercicio 018
  Escribir un programa que permita al usuario ingresar un numero entero y luego muestre un mensaje indicando si el numero es par o impar.
  Pensando los pasos para resolver el problema:
     
  1- Pedir al usuario que ingrese un numero entero
  2- Almacenar ese numero en una variable
  3- verificar si el numero es par o impar
  
  Si el número es par, mostrar un mensaje indicando que es par.
  si el número es impar, mostrar un mensaje indicando que es impar.
  
  (Para verificar si un numero es par o impar, se puede utilizar el operador modulo %).
  Si el resto de la division del numero por 2 es 0, el numero es par.
  Si el resto de la division del numero por 2 es 1, el numero es impar.
"""

variable = int(input("Numero: "))
es_par = (variable % 2) == 0
es_impar = (variable % 2) != 0

if es_par:
    print("Es par")
else:
    print("Es impar")

# print(variable, type(variable))
# print(es_par, type(es_par))
