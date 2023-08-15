"""
realizá un programa que permita que el usuario ingrese su nombre.
El programa debe emitir una salida con un mensaje de bienvenida que incluya el nombre.

"""
# por convención se usa snake case = nombre_completo
nombre_usuario=input("Ingrese su nombre: ")

def saludar(nombre_usuario):
  print("Hola", nombre_usuario)

saludar(nombre_usuario)