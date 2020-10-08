"""
A pesar de que el domino tradicional se juega con fichas hasta el número 6, vamos a considerar un
juego de fichas de valor máximo n.

    Escribir una función que calcule la cantidad de fichas para un juego de dominó completo con fichas
    que contienen hasta el número n. Nota: ¡No hay fichas repetidas! 2-4 es la misma ficha que 4-2.
    ¡Observar que en el dominó hay fichas con valor 0!

   cantidadFichas(3)
       10
   cantidadFichas(4)
       15

   Escribir una función que muestre todas las fichas para un juego de dominó como el anterior, en cualquier orden.

   mostrarFichas(3)
   0-0
   0-1
   0-2
   0-3
   1-1
   1-2
   1-3
   2-2
   2-3
   3-3

   Llamar a las funciones anteriores con distintos valores para corroborar su funcionamiento

   ★★★ Challenge: Escribir una función que, dada una cantidad de fichas, calcule cuál es el n (valor máximo) de las fichas. Si el número de fichas no corresponde a la cantidad de fichas de ningún juego de dominó completo retornar -1.

   valorMaximo(10)
   3
   valorMaximo(11)
   -1
   valorMaximo(15)
   4
"""