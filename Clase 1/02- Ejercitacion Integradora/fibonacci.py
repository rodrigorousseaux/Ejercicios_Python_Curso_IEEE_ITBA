x = 0
y = 1
z = 1

numero = int(input("Ingrese un numero: "))

print("0, 1", end=", ")

for i in range(1, numero, 1):

    z = x + y
    print(z, end=", ")

    x = y
    y = z