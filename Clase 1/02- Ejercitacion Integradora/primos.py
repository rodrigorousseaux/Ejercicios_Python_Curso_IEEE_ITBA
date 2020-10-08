def calcularPrimos(num):

    if num == 1:
        return False
    """El numero primo se divide entre 1 y si mismo SOLAMENTE.
    En este for lo divido desde 2 hasta su antecesor, verificando asi
    si tiene algun otro multiplo"""
    for i in range(2, num, 1):

        if num % i == 0:
            return False

    return True


for i in range(1, 21, 1):

    esPrimo = calcularPrimos(i)

    if esPrimo:
        print("El numero " + str(i) + " es primo")
    else:
        print("El numero " + str(i) + " no es primo")
