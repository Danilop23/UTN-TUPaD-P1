# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.  
# Funcion principal del programa
def verificar_mayoria_edad():
    # Solicita al usuario que ingrese su edad
    edad = int(input("Por favor, ingresa tu edad: "))

    # Verifica si la edad es mayor a 18
    if edad > 18:
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")

# Llamada a la función principal
verificar_mayoria_edad()

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 
# Función principal del programa
def evaluar_nota():
    # Solicita al usuario que ingrese su nota
    nota = int(input("Por favor, ingresa tu nota: "))

    # Verifica si la nota es mayor o igual a 6
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

# Llamada a la función principal
evaluar_nota()

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
# Función principal del programa
def ingresar_numero_par():
    # Solicita al usuario que ingrese un número
    numero = int(input("Por favor, ingresa un número: "))

    # Verifica si el número es par usando el operador módulo (%)
    if numero % 2 == 0:
        print("Ha ingresado un número par.")
    else:
        print("Por favor, ingrese un número par.")

# Llamada a la función principal
ingresar_numero_par()

# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.
# Función principal del programa
def clasificar_por_edad():
    # Solicita al usuario que ingrese su edad
    edad = int(input("Por favor, ingresa tu edad: "))

    # Clasificación por edad según las categorías dadas
    if edad < 12:
        print("Niño/a")
    elif edad >= 12 and edad < 18:
        print("Adolescente")
    elif edad >= 18 and edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

# Llamada a la función principal
clasificar_por_edad()

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
# Función principal del programa
def verificar_contraseña():
    # Solicita al usuario que ingrese una contraseña
    contraseña = input("Por favor, ingresa tu contraseña: ")

    # Verifica si la longitud de la contraseña está entre 8 y 14 caracteres
    if len(contraseña) >= 8 and len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta.")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Llamada a la función principal
verificar_contraseña()
import random
from statistics import mode, median, mean

# Generamos la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprimimos los resultados de la moda, mediana y media
print("Lista de números aleatorios:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)

# Comparamos para determinar el sesgo
if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

    # 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
    # Función principal del programa
def verificar_terminacion_vocal():
    # Solicita al usuario que ingrese una frase o palabra
    frase = input("Por favor, ingresa una frase o palabra: ")

    # Comprobamos si la última letra es una vocal
    if frase[-1].lower() in 'aeiou':
        frase += '!'  # Añadimos un signo de exclamación al final
        print(frase)
    else:
        print(frase)

# Llamada a la función principal
verificar_terminacion_vocal()

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# Función principal del programa
def transformar_nombre():
    # Solicita al usuario que ingrese su nombre
    nombre = input("Por favor, ingresa tu nombre: ")

    # Solicita al usuario que elija una opción
    print("Elige una opción para transformar tu nombre:")
    print("1. Mayúsculas")
    print("2. Minúsculas")
    print("3. Primera letra mayúscula")
    opcion = input("Escribe 1, 2 o 3: ")

    # Realiza la transformación según la opción elegida
    if opcion == '1':
        print(nombre.upper())  # Convierte a mayúsculas
    elif opcion == '2':
        print(nombre.lower())  # Convierte a minúsculas
    elif opcion == '3':
        print(nombre.title())  # Convierte la primera letra a mayúscula
    else:
        print("Opción no válida. Elige 1, 2 o 3.")

# Llamada a la función principal
transformar_nombre()

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: ● Menor que 3: "Muy leve" (imperceptible). ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
# Función principal del programa
def clasificar_terremoto():
    # Solicita al usuario la magnitud del terremoto
    magnitud = float(input("Por favor, ingresa la magnitud del terremoto en la escala de Richter: "))

    # Clasificación de la magnitud según la escala de Richter
    if magnitud < 3:
        print("Muy leve (imperceptible).")
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible).")
    elif 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños).")
    elif 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles).")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos).")
    else:
        print("Extremo (puede causar graves daños a gran escala).")

# Llamada a la función principal
clasificar_terremoto()

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año. Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
def obtener_estacion(hemisferio, mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Invierno" if hemisferio == "N" else "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Primavera" if hemisferio == "N" else "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Verano" if hemisferio == "N" else "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        return "Otoño" if hemisferio == "N" else "Primavera"
    else:
        return "Fecha inválida"

# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingresa el número del mes (1-12): "))
dia = int(input("Ingresa el día del mes: "))

# Validar hemisferio
if hemisferio not in ["N", "S"]:
    print("Hemisferio inválido. Debe ser 'N' o 'S'.")
else:
    estacion = obtener_estacion(hemisferio, mes, dia)
    print(f"La estación del año es: {estacion}")
    