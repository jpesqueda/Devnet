# Función sin parámetros ni retorno
def saludar():
    """Función que imprime un saludo"""
    print("Hola, bienvenido a Python.")

saludar()
print()

# Función con parámetros y retorno
def sumar(a, b):
    """Función que suma dos números y devuelve el resultado"""
    return a + b

print("Suma de cinco más tres:", sumar(5, 3))
print()

# Función con valores por defecto
def presentacion(nombre="Invitado"):
    """Función que muestra un saludo con un nombre por defecto"""
    print("Hola,", nombre)

presentacion()
presentacion("Carlos")
print()

# Función con múltiples argumentos
def suma_varios(*numeros):
    """Función que recibe varios números y devuelve su suma"""
    return sum(numeros)

print("Suma de varios números:", suma_varios(1, 2, 3, 4, 5))
print()

# Función con múltiples parámetros clave-valor
def informacion(**datos):
    """Función que recibe datos clave-valor y los imprime"""
    for clave, valor in datos.items():
        print(clave + ":", valor)

informacion(nombre="Carlos", edad=30, ciudad="México")
print()

# Función lambda o función anónima
doble = lambda x: x * 2
print("El doble de cuatro es:", doble(4))
print()

# Generador con yield
def contador(maximo):
    """Generador que cuenta hasta un número máximo"""
    num = 1
    while num <= maximo:
        yield num
        num += 1

print("Contador usando yield:")
for numero in contador(5):
    print(numero)
print()

# Manejo de excepciones con try y except
def dividir(a, b):
    """Función que maneja una división y captura errores"""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error no se puede dividir por cero"
    except TypeError:
        return "Error se requieren números"

print("División de diez entre dos:", dividir(10, 2))
print("División de diez entre cero:", dividir(10, 0))
print("División con error de tipo:", dividir(10, "a"))
print()

# Función recursiva para calcular el factorial
def factorial(n):
    """Función recursiva para calcular el factorial de un número"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial de cinco:", factorial(5))
print()

# Uso de la función map para aplicar una operación a una lista
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados de la lista", numeros, ":", cuadrados)
print()

# Uso de la función filter para filtrar elementos de una lista
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares en la lista", numeros, ":", pares)
print()

# Uso de la función zip para combinar listas
nombres = ["Carlos", "Ana", "Pedro"]
edades = [30, 25, 40]
datos = list(zip(nombres, edades))
print("Lista combinada de nombres y edades:", datos)


# Ejemplos con raise 
#Ejemplo uno: Lanzar un error si el número es negativo

def raiz_cuadrada(num):
    """Devuelve la raíz cuadrada de un número, pero lanza un error si es negativo"""
    if num < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return num ** 0.5

# Prueba
print(raiz_cuadrada(16))  # Funciona correctamente
print(raiz_cuadrada(-4))  # Lanza ValueError


#Ejemplo dos: Validar tipo de dato con raise
def dividir(a, b):
    """Divide dos números, pero lanza un error si los valores no son numéricos"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos valores deben ser números")
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

# Prueba
print(dividir(10, 2))  # Funciona correctamente
print(dividir("10", 2))  # Lanza TypeError
print(dividir(10, 0))  # Lanza ZeroDivisionError


# Ejemplo tres: Uso de raise con manejo de excepciones
def verificar_edad(edad):
    """Verifica si la edad es válida para votar"""
    if edad < 18:
        raise ValueError("Debes tener al menos 18 años para votar")
    return "Puedes votar"

try:
    print(verificar_edad(20))  # Funciona correctamente
    print(verificar_edad(16))  # Lanza ValueError
except ValueError as e:
    print(f"Error detectado: {e}")

# Salida esperada:
# Error detectado: Debes tener al menos 18 años para votar


# Ejemplo cuatro: Personalizar excepciones
class SaldoInsuficienteError(Exception):
    """Excepción personalizada para saldo insuficiente"""
    pass

def retirar_dinero(saldo, cantidad):
    """Función que simula un retiro bancario"""
    if cantidad > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar el retiro")
    return saldo - cantidad

try:
    print(retirar_dinero(1000, 500))  # Funciona correctamente
    print(retirar_dinero(1000, 1500))  # Lanza SaldoInsuficienteError
except SaldoInsuficienteError as e:
    print(f"Error detectado: {e}")