#El bucle de tipo for si tiene ciertas particularidades. 
# El siguiente ejemplo, muestra como imprimir en pantalla los 20 primeros números
###Ejemplo for, imprime los 20 primeros numeros en una linea

for i in range(20):
    print(i, end=" ") #imprimir numero, sin salto linea
    # print() #lineavacia
    # print(i)

#Por su parte, un “equivalente” a un bucle de tipo foreach tendría la siguiente pinta
###Ejemplo foreach, imprime los numeros de la lista
for i in [1, 5, 7]:
    print() #lineavacia
    print(i, end=" ") #imprimir numero, sin salto linea
    print() #lineavacia


# 1️ Recorrer una lista de nombres
nombres = ["Carlos", "Ana", "Pedro", "Marta"]
print("Recorriendo una lista de nombres:")
for nombre in nombres:
    print(nombre)

# 2️ Recorrer una cadena de texto
print("\nRecorriendo una cadena de texto:")
texto = "Python"
for letra in texto:
    print(letra)
    #print(letra, ", "join(letra))

print(", ".join(texto))

# 3️ Recorrer un rango de números
print("\nUsando range() para recorrer números:")
for i in range(5):  # 0 a 4
    print(i)

# 4️ Recorrer un rango con valores personalizados
print("\nRecorriendo un rango con valores personalizados:")
for i in range(2, 10, 2):  # De 2 a 10 con paso 2
    print(i)

# 5️ Iterar sobre un diccionario
persona = {"nombre": "Carlos", "edad": 30, "ciudad": "México"}
print("\nRecorriendo un diccionario (claves y valores):")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# 6️ Recorrer una lista con `enumerate()`
print("\nUsando enumerate() para obtener índice y valor:")
frutas = ["manzana", "banana", "uva"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# 7️ Iterar sobre dos listas al mismo tiempo con `zip()`
print("\nUsando zip() para recorrer dos listas simultáneamente:")
nombres = ["Carlos", "Ana", "Pedro"]
edades = [30, 25, 40]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")

# 8️ Filtrar números pares de una lista
print("\nFiltrando números pares de una lista:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", pares)

# 9️ Bucle con `break` (detener el bucle)
print("\nUsando break para detener el bucle al encontrar un número mayor a 5:")
for num in numeros:
    if num > 5:
        print(f"Se encontró {num}, deteniendo el bucle.")
        break
    print(num)

# 10 Bucle con `continue` (saltar una iteración)
print("\nUsando continue para saltar el número 5:")
for num in numeros:
    if num == 5:
        continue  # Salta la iteración cuando num es 5
    print(num)

# 1️1️ Iterar sobre una lista anidada (listas dentro de listas)
print("\nRecorriendo una lista anidada:")
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in lista_anidada:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Nueva línea

# 1️2️ Usando `for` con `else`
print("\nUsando for con else:")
for num in numeros:
    if num == 100:
        print("Encontramos el número 100.")
        break
else:
    print("No se encontró el número 100.")

# 1️3️ Crear una nueva lista usando list comprehension
print("\nUsando list comprehension para crear una lista con los cuadrados de los números:")
cuadrados = [num ** 2 for num in numeros]
print("Cuadrados:", cuadrados)

# 1️4️ Usar `for` con `sorted()` para ordenar listas
print("\nOrdenando una lista con sorted():")
desordenados = [5, 2, 9, 1, 7]
ordenados = sorted(desordenados)
print("Lista ordenada:", ordenados)

# 1️5️ Usar `for` con `reversed()` para recorrer una lista al revés
print("\nRecorriendo una lista al revés con reversed():")
for num in reversed(numeros):
    print(num)


# Explicación de los ejemplos en el programa:
# Recorrer una lista de nombres e imprimir cada uno.
# Recorrer una cadena de texto y mostrar cada letra.
# Recorrer un rango de números con range().
# Usar range() con valores personalizados (inicio, fin, paso).
# Recorrer un diccionario con .items() y mostrar claves y valores.
# Usar enumerate() para obtener índices junto con valores de una lista.
# Iterar sobre dos listas al mismo tiempo con zip().
# Filtrar números pares de una lista con list comprehension.
# Usar break para detener el bucle cuando se encuentra una condición.
# Usar continue para saltar una iteración específica.
# Recorrer una lista anidada (matriz) con bucles anidados.
# Usar for con else: Ejecutar código si el for termina sin interrupciones.
# Crear una nueva lista con list comprehension.
# Ordenar una lista con sorted().
# Recorrer una lista al revés con reversed().


# Resumen de métodos comunes en for:
# Método / Función	Descripción
# range(n)	                Genera una secuencia de números de 0 a n-1.
# range(inicio, fin, paso)	Genera una secuencia desde inicio hasta fin-1, con paso.
# .items()	                Itera sobre clave-valor en un diccionario.
# .keys()	                Itera sobre las claves de un diccionario.
# .values()	                Itera sobre los valores de un diccionario.
# enumerate(lista)	        Devuelve índice y valor en cada iteración.
# zip(lista1, lista2)	    Permite iterar sobre dos listas a la vez.
# sorted(lista)	            Ordena una lista sin modificar la original.
# reversed(lista)	        Itera sobre una lista en orden inverso.
# break	                    Detiene el bucle inmediatamente.
# continue	                Salta la iteración actual y pasa a la siguiente.
# else con for	            Se ejecuta solo si el bucle termina sin break.
# List comprehension	    
# 
# 
# 
# Crear listas de forma compacta.