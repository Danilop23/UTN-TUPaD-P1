# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
# Bucle FOR para recorrer los números del 0 al 100
for numero in range(0, 101):
    print(numero)  # Imprime el número actual

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 
# Solicita al usuario un número entero
numero = input("Ingresa un número entero: ")

# Verifica si el número es negativo y lo convierte a positivo (los dígitos negativos no se cuentan)
if numero.startswith("-"):
    numero = numero[1:]  # Elimina el signo negativo

# Muestra la cantidad de dígitos del número
print("El número tiene", len(numero), "dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
# Solicita al usuario dos números enteros
inicio = int(input("Ingresa el primer número entero: "))
fin = int(input("Ingresa el segundo número entero: "))

# Asegura que el primer número sea menor que el segundo
if inicio > fin:
    inicio, fin = fin, inicio  # Intercambia los valores si están en orden inverso

suma = 0  # Inicializa la suma

# Bucle que recorre los números entre 'inicio' y 'fin', excluyéndolos
for numero in range(inicio + 1, fin):
    suma += numero  # Acumula la suma

# Muestra el resultado
print("La suma de los números entre", inicio, "y", fin, "es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 
suma_total = 0  # Inicializa la suma

while True:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    
    if numero == 0:
        break  # Sale del bucle si el número es 0
    
    suma_total += numero  # Suma el número ingresado

# Muestra la suma total
print("La suma total de los números ingresados es:", suma_total)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random  # Importa la librería para generar números aleatorios

# Genera un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

intentos = 0  # Contador de intentos

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1  # Suma un intento

    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número en", intentos, "intento(s).")
        break
    else:
        print("Incorrecto. Intenta nuevamente.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
# Recorre desde 100 hasta 0, bajando de 2 en 2
for numero in range(100, -1, -2):
    print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
# Solicita al usuario un número entero positivo
limite = int(input("Ingresa un número entero positivo: "))

# Verifica que el número sea positivo
if limite < 0:
    print("El número debe ser positivo.")
else:
    suma = 0  # Inicializa la suma

    for numero in range(0, limite + 1):  # Incluye el número ingresado en la suma
        suma += numero

    print("La suma de los números desde 0 hasta", limite, "es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
CANTIDAD = 100  # Puedes cambiar este valor a menos para hacer pruebas más rápidas

# Inicializa contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Bucle para ingresar los números
for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el número {i + 1} de {CANTIDAD}: "))

    # Verifica par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Verifica positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    # Los ceros no se cuentan como positivos ni negativos

# Muestra los resultados
print("\nResultados:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
CANTIDAD = 100  # Puedes cambiar este valor para pruebas (por ejemplo, a 5 o 10)

suma_total = 0  # Acumulador para la suma

# Bucle para ingresar los números
for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el número {i + 1} de {CANTIDAD}: "))
    suma_total += numero

# Cálculo de la media
media = suma_total / CANTIDAD

# Muestra el resultado
print("\nLa media de los", CANTIDAD, "números ingresados es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Ingresa un número entero: "))

# Convierte el número a string, lo invierte con slicing y lo vuelve a convertir a entero
numero_invertido = int(str(abs(numero))[::-1])

# Mantiene el signo si el número era negativo
if numero < 0:
    numero_invertido = -numero_invertido

print("El número invertido es:", numero_invertido)