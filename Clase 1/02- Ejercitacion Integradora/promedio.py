"""
Cálcular la nota de un alumno es una tarea cotidiana de un profesor. Esta tarea suele realizarse a mano o en excel
muchas veces. En esta ocasión la haremos en python.

    Escribir una función que calcule el promedio de 3 notas y entrege ese valor usando return.
    Reescribir la función anterior modificandola para asignar una importancia
    al primer examen de 20%,
    al segundo de 50% y
    al tercero de 30%.
    Llamar a cada función anterior 3 veces con distintas notas y verificar, mediante la instrucción if, si el alumno
    aprobó en cada caso (suponga que 4 es la nota de aprobación).
"""

def promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

def importanciaExamen(nota1, nota2, nota3):
    nota1 *= 0.2
    nota2 *= 0.5
    nota3 *= 0.3

    suma = nota1 + nota2 + nota3
    return suma

for i in range(0, 3, 1):
    print()
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    resultado = promedio(nota1, nota2, nota3)

    if resultado >= 4:
        print()
        print("Promedio 1: " + str(resultado) + ". [Aprobado]")
    else:
        print()
        print("Promedio 1: " + str(resultado) + ". [Desaprobado]")

    resultado2 = importanciaExamen(nota1, nota2, nota3)

    if resultado2 >= 4:
        print()
        print("Promedio 2: " + str(resultado2) + ". [Aprobado]")
    else:
        print()
        print("Promedio 2: " + str(resultado2) + ". [Desaprobado]")