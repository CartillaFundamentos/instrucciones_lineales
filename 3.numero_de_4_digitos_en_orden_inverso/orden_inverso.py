# Ejercicio No.3: Devolver número de cuatro dígitos en orden inverso

# input
n = int(input("Ingrese un número de 4 dígitos: "))

# processing
digito1 = (n % 10000) // 1000
digito2 = (n % 1000) // 100
digito3 = (n % 100) // 10
digito4 = n % 10

# output
print(str(digito4) + str(digito3) + str(digito2) + str(digito1))