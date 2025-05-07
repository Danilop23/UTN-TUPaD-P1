# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 
multiplos_de_4 = list(range(4, 101, 4))

# Mostrar la lista
print(multiplos_de_4)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
cosas_que_me_gustan = ["pizza", "montañas", "videojuegos", "gatos", "música"]

# Mostrar el penúltimo elemento
print("El penúltimo elemento es:", cosas_que_me_gustan[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = [] 
lista_vacia = []

# Agregar tres palabras usando append
lista_vacia.append("sol")
lista_vacia.append("libro")
lista_vacia.append("playa")

# Imprimir la lista resultante
print("Lista con palabras agregadas:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"] 
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo (índice 1) con "loro"
animales[1] = "loro"

# Reemplazar el último (índice -1) con "oso"
animales[-1] = "oso"

# Imprimir la lista modificada
print("Lista modificada:", animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# 1. Crea una lista llamada numeros con los valores: [8, 15, 3, 22, 7].
# 2. Busca el valor máximo de la lista usando max(numeros), que en este caso es 22.
# 3. Elimina ese valor máximo (22) de la lista con remove().
# 4. Imprime la lista resultante. Este programa elimina el número más grande de una lista y luego muestra la lista sin ese valor.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
numeros = list(range(10, 31, 5))

# Mostrar los dos primeros elementos
print("Los dos primeros elementos son:", numeros[0], "y", numeros[1])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"]
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los valores en los índices 1 y 2
autos[1] = "fiat"
autos[2] = "toyota"

# Mostrar la lista resultante
print("Lista modificada:", autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla. 
dobles = []

# Agregar el doble de 5, 10 y 15 usando append directamente
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print("Lista de dobles:", dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# Lista original
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente (índice 1)
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente (índice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante
print("Lista de compras actualizada:", compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidada = [
    15,            # lista_anidada[0]
    True,          # lista_anidada[1]
    [25.5, 57.9, 30.6],  # lista_anidada[2][0], [2][1], [2][2]
    False          # lista_anidada[3]
]

# Imprimir la lista resultante
print("Lista anidada:", lista_anidada)