"""Realizá un programa que permita ingresar el monto total de las ventas realizadas por un
vendedor durante el mes, de quien se sabe que gana un sueldo fijo de 44000 pesos más el 16
por ciento del monto total vendido. Con tales datos debes calcular y mostrar el importe a
cobrar por el vendedor.
"""

# sueldo_fijo = 44000
SUELDO_FIJO = 44000  # EN MAYUSCULAS EN PYTHON ES DECIR QUE ES UNA CONSTANTE
porcentaje_comision = 0.16

total_ventas = float(input("Ingrese el total de ventas del mes del vendedor:"))

comision_ventas = total_ventas * porcentaje_comision

sueldo_a_cobrar = SUELDO_FIJO + comision_ventas

recibo_de_sueldo = f"""
--------------------------------------------------
Liquidación Vendedor
--------------------------------------------------
Sueldo fijo:                     ${SUELDO_FIJO:15,.2f}
Comisión por ventas:             ${round(comision_ventas,2):15,.2f} 
--------------------------------------------------
Total a cobrar:                  ${round(sueldo_a_cobrar,2):15,.2f}
"""
print(recibo_de_sueldo)

#:15,.2f --> para darle formato a la cantidad ej 44,000.00
