# Leer = Read
# Escribir = Write
# open (ruta del archivo, modo)
# modo = escritura | lectura
mi_archivo = open('nombres.txt', 'r')
print(mi_archivo)
mis_lineas = mi_archivo.readlines()
for linea in mis_lineas:
    print(linea.strip())
