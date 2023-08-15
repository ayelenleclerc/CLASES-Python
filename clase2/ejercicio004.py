""" Realizá un programa que permita ingresar 3 notas pertenecientes a tres trimestres distintos pra cierto aumno de nivel secundario.
Debe calcularse y mostrar la nota promedio"""

# n1=int(input("Ingrese la primera nota: "))
# n2=int(input("Ingrese la segunda nota: "))
# n3=int(input("Ingrese la tercera nota: "))
# promedio=(n1+n2+n3)/3
# print("El promedio es: ", promedio)

n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))
n3=int(input("Numero 3: "))

promedio=(n1+n2+n3)/3

print("Notas:", n1, n2, n3, "Promedio:", promedio)

cadena_formato = f"Notas:[{n1}, {n2}, {n3}]==> Promedio: {promedio}"
print(cadena_formato)