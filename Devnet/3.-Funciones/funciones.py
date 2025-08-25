
#Por último para definir una función usamos la palabra reservada Def. 
#El siguiente ejemplo defina una función que calcula el máximo de dos números, 
# y cómo usarla para calcular el máximo entre 100 y 50.
###Ejemplo de función

def maximo(n1, n2): 
    if n1 < n2:
        return n2
    elif n2 < n1:  
        return n1
    else:
        return n1  

print(maximo(100, 50)) 



############################################################
#Función básica sin parámetros

def saludo():
    print("¡Hola, bienvenido a !")

saludo()  # Llamada a la #Función

############################################################

#Función con parámetros
def suma(a, b):
    return a + b
resultado = suma(5, 3)
print("Suma:", resultado)  # Salida: 8


############################################################
#Función con valores por defecto
def presentacion(nombre="Invitado"):
    print(f"Hola, {nombre}!")

presentacion()  # Usa el valor por defecto
presentacion("Carlos")  # Pasa un argumento


############################################################
#Función con múltiples parámetros (args)



def sumar_todo(*numeros):
    return sum(numeros)

print(sumar_todo(1, 2, 3, 4, 5))  # Salida: 15

############################################################
#Función con parámetros clave-valor (kwargs)



def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=30, ciudad="México")


############################################################
#Función con retorno múltiple
def operaciones(a, b):
    return a + b, a - b, a * b, a / b

suma, resta, multi, div = operaciones(10, 2)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multi}, División: {div}")


############################################################
#Función lambda (anónima)
doble = lambda x: x * 2
print(doble(5))  # Salida: 10


############################################################
#Función dentro de otra #Función (anidada)
def exterior(x):
    def interior(y):
        return x + y
    return interior

suma_dos = exterior(2)
print(suma_dos(3))  # Salida: 5

############################################################

#Función con map()
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]


############################################################
#Función recursiva
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Salida: 120


# Resumen
# Tipo de #Función	Ejemplo
# #Función básica	def hola():
# Con parámetros	def suma(a, b):
# Con valores por defecto	def saludo(nombre="Invitado"):
# Con *args	def sumar_todo(*numeros):
# Con **kwargs	def mostrar_info(**datos):
# Retorno múltiple	def operaciones(a, b):
# Lambda	doble = lambda x: x * 2
# Anidada	def exterior(x):
# map()	list(map(lambda x: x**2, numeros))
# Recursiva	def factorial(n):

