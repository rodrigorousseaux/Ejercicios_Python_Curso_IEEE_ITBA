numero = int(input())
contador = 0

while numero != 1:

    if numero % 2 == 0:
        numero /= 2
    else:
        numero = (numero * 3) + 1

    contador += 1

print(contador)