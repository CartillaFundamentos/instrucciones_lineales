# Ejercicio No. 5: Grados Celsius a Fahrenheit y Kelvin.

# input
c = float(input("Grados Celsius: "))

# processing
f = (c * (9/5)) + 32
k = c + 273.15

# output
print("Grados Fahrenheit:" + str(f))
print("Grados Kelvin:" + str(k))