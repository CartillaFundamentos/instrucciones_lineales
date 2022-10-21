# Ejercicio No. 4: Convertir cantidad de segundos en horas, minutos y segundos.

# input
segundos_totales = int(input("Ingrese la cantidad de segundos: "))

# Processing
horas = segundos_totales // 3600
minutos = segundos_totales // 60

minutos = minutos % 60
segundos = segundos_totales % 60

# output
print("Horas:" + str(horas))
print("Minutos:" + str(minutos))
print("Segundos:" + str(segundos))