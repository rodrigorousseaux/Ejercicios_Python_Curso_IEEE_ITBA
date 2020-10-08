"""El número e tiene inmensa utilidad para el análisis y la estadística, es una de las super-estrellas
de la matemática, y su utilidad radica en que la función ex es igual a su derivada, por definición de e.

Gracias a las series de Taylor podemos obtener la siguiente definición del número e:

e = 1 + 1/1! + 1/2! + 1/3! + 1/4! + 1/5! +.... 1/n!

Se pide obtener una aproximación del número e calculando la suma de los primeros 20 términos de esta sucesión infinita.

Tips---> n!=1⋅2⋅3⋅ ... ⋅n.
"""
e = 0
factorial = 0

for i in range(2, 21, 1):

    factorial += i * (i-1)
    e = e + (1 / factorial)

e += 2

print()
print(e)