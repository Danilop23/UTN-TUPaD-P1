# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    """
    Esta función imprime un mensaje de saludo en pantalla.
    """
    print("Hola Mundo!")

# Programa principal
if __name__ == "__main__":
    imprimir_hola_mundo()  # Llamada a la función

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de volver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    """
    Recibe un nombre como parámetro y devuelve un saludo personalizado.
    """
    return f"Hola {nombre}!"

# Programa principal
if __name__ == "__main__":
    nombre_usuario = input("Ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    """
    Imprime la información personal del usuario.
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu lugar de residencia: ")

    informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math  # Importamos la librería para usar el valor de π

# Función para calcular el área del círculo
def calcular_area_circulo(radio):
    """
    Calcula y devuelve el área de un círculo dado su radio.
    """
    return math.pi * radio ** 2

# Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    """
    Calcula y devuelve el perímetro de un círculo dado su radio.
    """
    return 2 * math.pi * radio

# Programa principal
if __name__ == "__main__":
    radio_input = input("Ingresa el radio del círculo: ")

    try:
        radio = float(radio_input)  # Convertimos a número decimal
        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)

        print(f"El área del círculo es: {area:.2f}")
        print(f"El perímetro del círculo es: {perimetro:.2f}")
    except ValueError:
        print("Por favor, ingresa un número válido para el radio.")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    """
    Convierte una cantidad de segundos a horas.
    """
    return segundos / 3600

# Programa principal
if __name__ == "__main__":
    segundos_input = input("Ingresa la cantidad de segundos: ")

    try:
        segundos = int(segundos_input)
        horas = segundos_a_horas(segundos)
        print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
    except ValueError:
        print("Por favor, ingresa un número válido de segundos.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar del número dado, del 1 al 10.
    """
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
if __name__ == "__main__":
    numero_input = input("Ingresa un número para ver su tabla de multiplicar: ")

    try:
        numero = int(numero_input)
        tabla_multiplicar(numero)
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    """
    Devuelve una tupla con la suma, resta, multiplicación y división de a y b.
    Maneja el caso en que b sea 0 para evitar división por cero.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    
    return (suma, resta, multiplicacion, division)

# Programa principal
if __name__ == "__main__":
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        
        suma, resta, mult, div = operaciones_basicas(a, b)

        print("\nResultados de las operaciones:")
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {mult}")
        print(f"División: {div}")
    
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    """
    Calcula y devuelve el Índice de Masa Corporal (IMC).
    """
    if altura <= 0:
        return "Altura inválida"
    return peso / (altura ** 2)

# Programa principal
if __name__ == "__main__":
    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))
        
        imc = calcular_imc(peso, altura)
        
        if isinstance(imc, str):
            print(f"Error: {imc}")
        else:
            print(f"Tu IMC es: {imc:.2f}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Pedir al usuario la temperatura en Celsius
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir a Fahrenheit usando la función
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

# Mostrar el resultado
print(f"{temp_celsius} grados Celsius equivalen a {temp_fahrenheit} grados Fahrenheit.")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Solicitar los números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular el promedio usando la función
promedio = calcular_promedio(num1, num2, num3)

# Mostrar el resultado
print(f"El promedio de los números ingresados es: {promedio}")