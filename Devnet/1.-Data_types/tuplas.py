# Variable tipo tupla (tuple):
# Mutabilidad: Las tuplas son inmutables, lo que significa que no puedes modificar su contenido después de crearlas.
# Sintaxis: Se definen con paréntesis ().
# Orden: Mantienen un orden de los elementos.
# Elementos duplicados: Permiten elementos duplicados.
# Ejemplo:
# mi_tupla = (1, 2, 3, 4)
# # mi_tupla[0] = 10  # Esto daría un error, no se puede modificar
# print(mi_tupla)  # Salida: (1, 2, 3, 4)

# Resumen de los métodos y operaciones más comunes con tuplas
# Operación	Descripción	Ejemplo
# Acceso a elementos	Acceder a elementos de la tupla usando índices	tupla[0], tupla[-1]
# Slicing	            Obtener una subtupla usando el operador :	tupla[1:4]
# count()	            Contar cuántas veces aparece un elemento	tupla.count(2)
# index()	            Encontrar el índice de un elemento en la tupla	tupla.index("manzana")
# Desempaquetado	    Asignar los elementos de la tupla a variables	a, b, c = tupla
# Tuplas anidadas	    Tuplas dentro de otras tuplas	tupla_anidada[0][0]
# Concatenación	Unir dos tuplas	tupla1 + tupla2
# Repetición	        Repetir los elementos de una tupla	tupla * 3
# len()	                Obtener la longitud de una tupla	len(tupla)
# in	                Verificar si un elemento está en la tupla	"manzana" in tupla
# Conversión	        Convertir una lista en tupla y viceversa	tuple(lista), list(tupla)


# 1. Crear una tupla con diferentes tipos de datos
tupla = (1, 2, 3, "manzana", 3.14)
print("Tupla original:", tupla)

# 2. Acceder a un elemento por su índice
print("Primer elemento:", tupla[0])  # Salida: 1
print("Último elemento:", tupla[-1])  # Salida: 3.14

# 3. Slicing (Rebanado) de tupla
subtupla = tupla[1:4]
print("Subtupla:", subtupla)  # Salida: (2, 3, 'manzana')

# 4. Contar cuántas veces aparece un elemento con count()
tupla = (1, 2, 3, 2, 4, 2)
print("El número 2 aparece:", tupla.count(2))  # Salida: 3

# 5. Obtener el índice de un elemento con index()
tupla = (1, 2, 3, "manzana", 3.14)
print("Índice de 'manzana':", tupla.index("manzana"))  # Salida: 3

# 6. Desempaquetar una tupla
a, b, c, d, e = tupla
print("Desempaquetado:")
print(a, b, c, d, e)  # Salida: 1 2 3 manzana 3.14

# 7. Tuplas anidadas
tupla_anidada = ((1, 2), (3, 4), (5, 6))
print("Tupla anidada:", tupla_anidada)
print("Primer elemento de la primera subtupla:", tupla_anidada[0][0])  # Salida: 1

# 8. Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_combinada = tupla1 + tupla2
print("Tupla combinada:", tupla_combinada)  # Salida: (1, 2, 3, 4, 5, 6)

# 9. Repetir tuplas
tupla_repetida = (1, 2) * 3
print("Tupla repetida:", tupla_repetida)  # Salida: (1, 2, 1, 2, 1, 2)

# 10. Verificar la longitud de una tupla con len()
print("Longitud de la tupla:", len(tupla))  # Salida: 5

# 11. Verificar si un elemento está en la tupla con in
if "manzana" in tupla:
    print("Manzana está en la tupla.")
else:
    print("Manzana no está en la tupla.")

# 12. Convertir una lista a tupla y viceversa
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
print("Tupla convertida:", tupla_convertida)  # Salida: (1, 2, 3)

tupla = (4, 5, 6)
lista_convertida = list(tupla)
print("Lista convertida:", lista_convertida)  # Salida: [4, 5, 6]
