"""Realizá un programa que permita ingresar el monto total de las ventas realizadas por un
vendedor durante el mes, de quien se sabe que gana un sueldo fijo de 44000 pesos más el 16
por ciento del monto total vendido. Con tales datos debes calcular y mostrar el importe a
cobrar por el vendedor.
"""
# venta_total_mensual=float(input("Total:"))
# sueldo_fijo=44000
# comision= venta_total_mensual*0.16
# total= sueldo_fijo+comision

# print("Importe a cobrar por el vendedor: ", total)

SUELDO_FIJO = 44000
COMISION = 0.16
total_ventas = float(input("Total de ventas: "))

comision_ventas = total_ventas * COMISION

total_cobro = float(SUELDO_FIJO + comision_ventas)

print(f"Importe a cobrar por el vendedor:, ${(total_cobro):15,.2f} ")

# :15,.2f  --> para darle formato a la cantidad ej 44,000.00
