#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_frecuencias(cadena):
    # Eliminamos los espacios
    cadena = cadena.replace(" ", "")
    # Creamos un diccionario vacío para las frecuencias
    frecuencias = {}
    
    # Recorremos cada letra en la cadena
    for letra in cadena:
        # Si la letra ya está en el diccionario, sumamos 1
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            # Si no, la agregamos con valor 1
            frecuencias[letra] = 1
    
    return frecuencias

# Ejemplo de uso
texto = "hola mundo"
resultado = contar_frecuencias(texto)
print(resultado)




#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# Lista original
numeros = [1, 2, 3, 4, 5]

# Usamos map() para obtener el doble de cada número
dobles = list(map(lambda x: x * 2, numeros))

# Mostramos el resultado
print(dobles)




#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabras(lista_palabras, palabra_objetivo):
    # Filtramos las palabras que contienen la palabra objetivo
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

# Ejemplo de uso
palabras = ["camino", "camiseta", "cama", "auto", "camello"]
objetivo = "cam"

resultado = buscar_palabras(palabras, objetivo)
print(resultado)




#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    # Usamos map() para restar elemento a elemento
    return list(map(lambda x, y: x - y, lista1, lista2))

# Ejemplo de uso
lista_a = [10, 20, 30, 40]
lista_b = [1, 5, 10, 15]

resultado = diferencia_listas(lista_a, lista_b)
print(resultado)




#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.

def evaluar_nota(notas, nota_aprobado=5):
    # Calculamos la media de la lista
    media = sum(notas) / len(notas)
    
    # Determinamos el estado según la media
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    # Devolvemos una tupla (media, estado)
    return (media, estado)

# Ejemplo de uso
notas_alumno = [6, 7, 5, 8, 9]
resultado = evaluar_nota(notas_alumno)

print(resultado)




#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial(n - 1)
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")




#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    # Usamos map() para convertir cada tupla en un string
    return list(map(lambda t: " ".join(map(str, t)), lista_tuplas))

# Ejemplo de uso
datos = [(1, 2), ("hola", "mundo"), (3.5, 4.8)]
resultado = tuplas_a_strings(datos)
print(resultado)




#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#indicando si la división fue exitosa o no.

def dividir_numeros():
    try:
        # Pedimos los números al usuario
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        # Intentamos realizar la división
        resultado = num1 / num2

    except ValueError:
        # Captura cuando el usuario ingresa algo que no es un número
        print("Error: Debes ingresar solo valores numéricos.")
    except ZeroDivisionError:
        # Captura cuando se intenta dividir por cero
        print("Error: No se puede dividir entre cero.")
    else:
        # Se ejecuta si no hubo ningún error
        print(f"División exitosa: {num1} / {num2} = {resultado}")
    finally:
        # Este bloque siempre se ejecuta
        print("Fin del programa.")

# Ejemplo de ejecución
dividir_numeros()




#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # Usamos filter() para excluir las mascotas prohibidas
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

# Ejemplo de uso
mascotas = ["Perro", "Gato", "Tigre", "Cocodrilo", "Conejo"]
resultado = filtrar_mascotas(mascotas)
print(resultado)




#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.

# Definimos la excepción personalizada
class ListaVaciaError(Exception):
    pass

def promedio_numeros(lista):
    if not lista:
        # Lanzamos la excepción si la lista está vacía
        raise ListaVaciaError("La lista está vacía. No se puede calcular el promedio.")
    return sum(lista) / len(lista)

# Ejemplo de uso
try:
    numeros = []  # Prueba con lista vacía
    resultado = promedio_numeros(numeros)
    print(f"El promedio es: {resultado}")
except ListaVaciaError as e:
    print(f"Error: {e}")




#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
#adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        
        # Verificamos que la edad esté en un rango válido
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")

    except ValueError as e:
        # Captura tanto errores de conversión como de rango
        print(f"Error: {e}")
    else:
        print(f"Edad válida: {edad} años.")
    finally:
        print("Fin del programa.")

# Ejecutar la función
pedir_edad()




#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitudes_palabras(frase):
    # Separamos la frase en palabras
    palabras = frase.split()
    # Usamos map() para obtener la longitud de cada palabra
    return list(map(len, palabras))

# Ejemplo de uso
frase = "Hola mundo desde Python"
resultado = longitudes_palabras(frase)
print(resultado)




#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minus(conjunto):
    # Eliminamos duplicados convirtiendo a set y ordenamos para consistencia
    letras_unicas = sorted(set(conjunto))
    # Usamos map() para generar tuplas (mayúscula, minúscula)
    return list(map(lambda l: (l.upper(), l.lower()), letras_unicas))

# Ejemplo de uso
caracteres = ['a', 'b', 'A', 'c', 'b', 'C']
resultado = letras_mayus_minus(caracteres)
print(resultado)




#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
#función filter()

def palabras_por_letra(lista_palabras, letra_inicial):
    # Usamos filter() para obtener palabras que comienzan con la letra indicada
    return list(filter(lambda palabra: palabra.startswith(letra_inicial), lista_palabras))

# Ejemplo de uso
palabras = ["manzana", "mango", "pera", "melón", "banana"]
resultado = palabras_por_letra(palabras, "m")
print(resultado)



#15. Crea una función lambda que sume 3 a cada número de una lista dada.

# Lista de ejemplo
numeros = [1, 2, 3, 4, 5]

# Lambda que suma 3 a cada número usando map()
resultado = list(map(lambda x: x + 3, numeros))

print(resultado)




#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas(cadena, n):
    # Separamos la cadena en palabras
    palabras = cadena.split()
    # Filtramos las palabras que tienen longitud mayor que n
    return list(filter(lambda palabra: len(palabra) > n, palabras))

# Ejemplo de uso
texto = "Python es un lenguaje de programación muy poderoso"
resultado = palabras_mas_largas(texto, 5)
print(resultado)




#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
#corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos):
    # Usamos reduce para combinar los dígitos en un solo número
    return reduce(lambda x, y: x * 10 + y, digitos)

# Ejemplo de uso
digitos = [5, 7, 2]
resultado = lista_a_numero(digitos)
print(resultado)




#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
#90. Usa la función filter()

# Lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "Marta", "edad": 19, "calificacion": 92},
    {"nombre": "Pedro", "edad": 21, "calificacion": 85}
]

# Filtramos los estudiantes con calificación >= 90
estudiantes_destacados = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

# Mostramos el resultado
print(estudiantes_destacados)




#19. Crea una función lambda que filtre los números impares de una lista dada.

# Lista de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7]

# Lambda que filtra los números impares usando filter()
impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares)




#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
#filter()

# Lista de ejemplo con enteros y strings
elementos = [1, "hola", 3, "mundo", 5, "python"]

# Filtramos solo los elementos de tipo int
enteros = list(filter(lambda x: isinstance(x, int), elementos))

print(enteros)




#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

# Definimos la función lambda que calcula el cubo
cubo = lambda x: x ** 3

# Ejemplo de uso
numero = 4
resultado = cubo(numero)
print(f"El cubo de {numero} es {resultado}")




#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

# Ejemplo de uso
numeros = [2, 3, 4]
resultado = producto_total(numeros)
print(resultado)




#23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce

def concatenar_palabras(lista_palabras):
    return reduce(lambda x, y: x + y, lista_palabras)

# Ejemplo de uso
palabras = ["Hola", " ", "mundo", "!"]
resultado = concatenar_palabras(palabras)
print(resultado)




#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

# Ejemplo de uso
numeros = [10, 2, 3]
resultado = diferencia_total(numeros)
print(resultado)




#25. Crea una función que cuente el número de caracteres en una cadena de texto dada

def contar_caracteres(cadena):
    return len(cadena)

# Ejemplo de uso
texto = "Hola, mundo"
resultado = contar_caracteres(texto)
print(f"El número de caracteres es: {resultado}")




#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# Función lambda para calcular el resto
resto = lambda x, y: x % y

# Ejemplo de uso
a = 17
b = 5
resultado = resto(a, b)
print(f"El resto de {a} ÷ {b} es {resultado}")




#27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    if not lista:
        return 0  # O manejar como desees si la lista está vacía
    return sum(lista) / len(lista)

# Ejemplo de uso
numeros = [10, 20, 30, 40, 50]
resultado = promedio(numeros)
print(f"El promedio es: {resultado}")




#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento  # Retorna el primer duplicado encontrado
        vistos.add(elemento)
    return None  # Si no hay duplicados

# Ejemplo de uso
numeros = [2, 5, 1, 2, 3, 5]
resultado = primer_duplicado(numeros)
print(f"El primer duplicado es: {resultado}")




#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#carácter '#', excepto los últimos cuatro.

def enmascarar_variable(valor):
    # Convertimos el valor a string
    texto = str(valor)
    # Enmascaramos todos los caracteres menos los últimos cuatro
    if len(texto) <= 4:
        return texto  # Si tiene 4 o menos caracteres, no se enmascara
    return '#' * (len(texto) - 4) + texto[-4:]

# Ejemplo de uso
numero_tarjeta = 1234567890123456
resultado = enmascarar_variable(numero_tarjeta)
print(resultado)




#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    # Convertimos a minúsculas y ordenamos las letras
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Ejemplo de uso
palabra_a = "Amor"
palabra_b = "Roma"

resultado = son_anagramas(palabra_a, palabra_b)
print(f"¿Son anagramas? {resultado}")




#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.

# Definimos la excepción personalizada
class NombreNoEncontradoError(Exception):
    pass

def buscar_nombre():
    # Pedimos al usuario que ingrese nombres separados por comas
    entrada = input("Introduce una lista de nombres separados por comas: ")
    lista_nombres = [nombre.strip() for nombre in entrada.split(",")]
    
    # Pedimos el nombre a buscar
    nombre_a_buscar = input("Introduce el nombre a buscar: ").strip()
    
    try:
        if nombre_a_buscar in lista_nombres:
            print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
        else:
            # Lanzamos excepción si no se encuentra
            raise NombreNoEncontradoError(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista.")
    except NombreNoEncontradoError as e:
        print(e)

# Ejecución de la función
buscar_nombre()




#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#no trabaja aquí.

def buscar_puesto(nombre_completo, lista_empleados):
    """
    lista_empleados: lista de diccionarios con claves 'nombre' y 'puesto'
    """
    for empleado in lista_empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return f"El puesto de {nombre_completo} es: {empleado['puesto']}"
    return f"{nombre_completo} no trabaja aquí."

# Ejemplo de uso
empleados = [
    {"nombre": "Ana García", "puesto": "Gerente"},
    {"nombre": "Luis Pérez", "puesto": "Programador"},
    {"nombre": "Marta López", "puesto": "Diseñadora"}
]

resultado = buscar_puesto("Luis Pérez", empleados)
print(resultado)

resultado2 = buscar_puesto("Carlos Ruiz", empleados)
print(resultado2)




#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# Listas de ejemplo
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Lambda para sumar elementos correspondientes
suma_listas = list(map(lambda x, y: x + y, lista1, lista2))

print(suma_listas)




#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#manipular la estructura del árbol.
#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método
#info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
#mismas.
#Caso de uso:
#1. Crear un árbol.
#2. Hacer crecer el tronco del árbol una unidad.
#3. Añadir una nueva rama al árbol.
#4. Hacer crecer todas las ramas del árbol una unidad.
#5. Añadir dos nuevas ramas al árbol.
#6. Retirar la rama situada en la posición 2.
#7. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        # Inicializar tronco de longitud 1 y lista vacía de ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en 1"""
        self.tronco += 1

    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1"""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta la longitud de todas las ramas existentes en 1"""
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina la rama en la posición indicada (0-index)"""
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print(f"Posición inválida: {posicion}")

    def info_arbol(self):
        """Devuelve información sobre el tronco y las ramas"""
        info = {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
        return info


# ------------------------------
# Caso de uso
# ------------------------------

# 1. Crear un árbol
mi_arbol = Arbol()

# 2. Hacer crecer el tronco una unidad
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2 (0-index)
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
info = mi_arbol.info_arbol()
print(info)




#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
#agregar dinero al saldo.
#Código a seguir:
#1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
#poder hacerse.
#3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
#Lanzará un error en caso de no poder hacerse.
#4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#Caso de uso:
#1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#2. Agregar 20 unidades de saldo de "Bob".
#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#4. Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, usuario_origen, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if cantidad > usuario_origen.saldo:
            raise ValueError(f"{usuario_origen.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        usuario_origen.saldo -= cantidad
        self.saldo += cantidad
        print(f"{usuario_origen.nombre} ha transferido {cantidad} a {self.nombre}.")
        print(f"Saldo de {usuario_origen.nombre}: {usuario_origen.saldo}, Saldo de {self.nombre}: {self.saldo}")

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad
        print(f"{self.nombre} ha agregado {cantidad}. Saldo actual: {self.saldo}")


# Caso de uso ajustado:

# 1. Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 50 unidades de saldo a Bob (para que pueda transferir 80)
bob.agregar_dinero(50)  # Bob pasa de 50 → 100

# 3. Hacer una transferencia de 80 unidades desde Bob a Alicia
alicia.transferir_dinero(bob, 80)  # Bob: 100 → 20, Alicia: 100 → 180

# 4. Retirar 50 unidades de saldo a Alicia
alicia.retirar_dinero(50)  # Alicia: 180 → 130




#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
#reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
#de la función procesar_texto .
#Código a seguir:
#1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
#que devolver un diccionario.
#2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
#que devolver el texto con el remplazo de palabras.
#3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
#eliminada.
#4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
#número de argumentos variable según la opción indicada.
#Caso de uso:
#Comprueba el funcionamiento completo de la función procesar_texto

# 1. Función para contar palabras
def contar_palabras(texto):
    palabras = texto.split()
    frecuencias = {}
    for palabra in palabras:
        palabra = palabra.lower()  # opcional: ignorar mayúsculas/minúsculas
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

# 2. Función para reemplazar palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# 3. Función para eliminar una palabra
def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return " ".join(palabras_filtradas)

# 4. Función principal que procesa el texto
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para reemplazar se necesitan 2 argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para eliminar se necesita 1 argumento: palabra_a_eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Elige entre 'contar', 'reemplazar', 'eliminar'.")


# ------------------------------
# Caso de uso
# ------------------------------
texto_ejemplo = "Python es un lenguaje de programación. Python es muy poderoso."

# Contar palabras
resultado_contar = procesar_texto(texto_ejemplo, "contar")
print("Contar palabras:", resultado_contar)

# Reemplazar palabra
resultado_reemplazar = procesar_texto(texto_ejemplo, "reemplazar", "Python", "Java")
print("Reemplazar palabra:", resultado_reemplazar)

# Eliminar palabra
resultado_eliminar = procesar_texto(texto_ejemplo, "eliminar", "Python")
print("Eliminar palabra:", resultado_eliminar)




#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento_dia():
    try:
        # Pedimos la hora al usuario
        hora = int(input("Introduce la hora (0-23): "))
        
        if hora < 0 or hora > 23:
            print("Hora inválida. Debe estar entre 0 y 23.")
            return
        
        # Determinamos el momento del día
        if 6 <= hora < 12:
            momento = "Mañana / Día"
        elif 12 <= hora < 18:
            momento = "Tarde"
        else:
            momento = "Noche"
        
        print(f"Son las {hora}:00. Es {momento}.")
    
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero entre 0 y 23.")

# Ejecutar la función
determinar_momento_dia()




#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#Las reglas de calificación son:
#- 0 - 69 insuficiente
#- 70 - 79 bien
#- 80 - 89 muy bien
#- 90 - 100 excelente

def calificacion_texto():
    try:
        nota = float(input("Introduce la calificación del alumno (0-100): "))
        
        if nota < 0 or nota > 100:
            print("Calificación inválida. Debe estar entre 0 y 100.")
            return
        
        if 0 <= nota <= 69:
            texto = "Insuficiente"
        elif 70 <= nota <= 79:
            texto = "Bien"
        elif 80 <= nota <= 89:
            texto = "Muy bien"
        else:  # 90-100
            texto = "Excelente"
        
        print(f"La calificación {nota} corresponde a: {texto}")
    
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entre 0 y 100.")

# Ejecutar la función
calificacion_texto()




#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
#"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    figura = figura.lower()
    
    if figura == "rectangulo":
        # datos = (base, altura)
        if len(datos) != 2:
            raise ValueError("Para un rectángulo se necesitan 2 datos: base y altura.")
        base, altura = datos
        return base * altura
    
    elif figura == "circulo":
        # datos = (radio,)
        if len(datos) != 1:
            raise ValueError("Para un círculo se necesita 1 dato: radio.")
        radio = datos[0]
        return math.pi * radio ** 2
    
    elif figura == "triangulo":
        # datos = (base, altura)
        if len(datos) != 2:
            raise ValueError("Para un triángulo se necesitan 2 datos: base y altura.")
        base, altura = datos
        return (base * altura) / 2
    
    else:
        raise ValueError("Figura no válida. Debe ser 'rectangulo', 'circulo' o 'triangulo'.")


# ------------------------------
# Ejemplos de uso
# ------------------------------
print("Área rectángulo:", calcular_area("rectangulo", (5, 3)))
print("Área círculo:", calcular_area("circulo", (4,)))
print("Área triángulo:", calcular_area("triangulo", (6, 2)))




#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
#monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
#siguiente:
#1. Solicita al usuario que ingrese el precio original de un artículo.
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
#a cero). Por ejemplo, descuento de 15€.
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
#programa de Python.

def calcular_precio_final():
    try:
        # 1. Solicitar precio original
        precio_original = float(input("Introduce el precio original del artículo: "))
        if precio_original < 0:
            print("El precio no puede ser negativo.")
            return
        
        # 2. Preguntar si tiene cupón
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
        
        descuento = 0
        
        if tiene_cupon == "sí" or tiene_cupon == "si":
            # 3. Solicitar valor del cupón
            valor_cupon = float(input("Introduce el valor del cupón de descuento: "))
            
            # 4. Validar cupón
            if valor_cupon > 0:
                descuento = valor_cupon
            else:
                print("Valor de cupón inválido. No se aplicará descuento.")
        
        # 5. Calcular precio final
        precio_final = max(precio_original - descuento, 0)  # Evita que sea negativo
        print(f"El precio final de la compra es: {precio_final:.2f}€")
    
    except ValueError:
        print("Entrada inválida. Debes ingresar números válidos para precio y cupón.")

# Ejecutar la función
calcular_precio_final()


