# calcule el promedio de 2 notas
# nombre, condicion, curso, fecha
from datetime import datetime

now = datetime.now()
# year - month - day
# y-m-d
fecha_actual = now.strftime("%Y-%m-%d")
# hour - minute - seconds
hora_actual = now.strftime("%H:%M:%S")
print(fecha_actual)
print(hora_actual)

# Pedir 2 notas
nota_1 = int(input("Ingrese la 1era nota: "))
nota_2 = int(input("Ingrese la 2da nota: "))
nombre = input("Ingrese el nombre: ")
# si la nota >= 13 condicion = aprobado caso contraroi jalado
condicion = "JALADO!!!"

promedio = (nota_1 + nota_2) / 2

if promedio >= 13:
    condicion = "Aprobaste !!!"

nombre_archivo = nombre + str(fecha_actual) + str(hora_actual)
mi_archivo = open(nombre_archivo + ".txt", 'w')
mi_archivo.write("Nombre: " + nombre + "\n")
mi_archivo.write("Condicion: " + condicion + "\n")
mi_archivo.write("promedio: " + str(promedio) + "\n")
mi_archivo.write("Fecha: " + str(fecha_actual) + "\n")
