# 1) Dado el diccionario precios_frutas 
# Diccionario inicial
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Agregar nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el diccionario actualizado
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario actualizado
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
# Obtener solo las frutas (claves del diccionario)
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista de frutas
print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# Crear un diccionario vacío
contactos = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de teléfono de {nombre}: ")
    contactos[nombre] = numero

# Consultar un nombre
consulta = input("¿Qué contacto querés consultar?: ")

# Verificar si existe y mostrar el número
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("El contacto no existe.")

# 5) Solicita al usuario una frase e imprime:
# Solicitar una frase al usuario
frase = input("Ingresá una frase: ")

# Separar en palabras
palabras = frase.split()

# Obtener palabras únicas con un set
palabras_unicas = set(palabras)

# Contar la cantidad de veces que aparece cada palabra
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Crear un diccionario vacío para almacenar los alumnos y sus notas
alumnos = {}

# Cargar 3 alumnos con sus notas
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    print(f"Ingresá 3 notas para {nombre}:")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
parcial1 = {"Ana", "Luis", "Sofía", "Carlos"}
parcial2 = {"Sofía", "Carlos", "María", "Pedro"}
# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2

# Estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2

# Estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Diccionario de ejemplo con productos y su stock
stock_productos = {
    "ladrillo": 100,
    "cemento": 50,
    "cal": 80
}

# Pedir producto al usuario
producto = input("Ingresá el nombre del producto: ").lower()

# Verificar si el producto existe en el stock
if producto in stock_productos:
    print(f"Stock actual de '{producto}': {stock_productos[producto]}")
    
    # Preguntar si desea agregar unidades
    agregar = input("¿Querés agregar unidades a este producto? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de '{producto}': {stock_productos[producto]}")
else:
    print(f"El producto '{producto}' no existe en el stock.")
    agregar_nuevo = input("¿Querés agregar este producto al stock? (s/n): ").lower()
    if agregar_nuevo == "s":
        cantidad = int(input("¿Cuántas unidades querés ingresar para este nuevo producto?: "))
        stock_productos[producto] = cantidad
        print(f"Producto '{producto}' agregado con stock de {cantidad} unidades.")

# Mostrar stock actualizado
print("\nStock actual:")
for prod, cant in stock_productos.items():
    print(f"{prod}: {cant}")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Agenda con tuplas (día, hora) como claves
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Gimnasio"
}

# Solicitar al usuario día y hora
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato hh:mm): ")

# Consultar la actividad
clave = (dia, hora)

if clave in agenda:
    print(f"A esa hora tenés: {agenda[clave]}")
else:
    print("No hay ninguna actividad programada en ese día y hora.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: 
# Diccionario original
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Invertir claves y valores
invertido = {capital: pais for pais, capital in original.items()}

# Mostrar el nuevo diccionario
print("Diccionario invertido:", invertido)