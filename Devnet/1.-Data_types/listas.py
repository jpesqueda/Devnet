# Variable tipo lista (list):
# Mutabilidad: Las listas son mutables, lo que significa que puedes modificar su contenido después de crearlas (agregar, eliminar o cambiar elementos).
# Sintaxis: Se definen con corchetes [].
# Orden: Mantienen un orden de los elementos (el orden en que se insertan).
# Elementos duplicados: Permiten elementos duplicados.
# Ejemplo:
# mi_lista = [1, 2, 3, 4]
# mi_lista.append(5)  # Agregar un elemento
# print(mi_lista)  # Salida: [1, 2, 3, 4, 5]


# Acceso a elementos por índice y modificación de los mismos.
# Agregar y eliminar elementos con append(), extend(), insert(), remove() y pop().
# Métodos para trabajar con listas:
# Métodos como clear(), count(), index(), sort(), reverse(), copy() y len() para manipular y consultar listas.
# Manejo de listas dentro de listas:
# Listas anidadas: Listas dentro de otras listas y cómo acceder a sus elementos.

# Crear una lista con elementos de diferentes tipos
frutas = ["manzana", "plátano", "naranja"]
print("Lista original:", frutas)

# 1. Acceder a un elemento por su índice
print("Primer elemento:", frutas[0])  # Salida: manzana
print("Último elemento:", frutas[-1])  # Salida: naranja

# 2. Modificar un valor en la lista
frutas[1] = "fresa"
print("Lista modificada:", frutas)  # Salida: ['manzana', 'fresa', 'naranja']

# 3. Agregar un solo elemento al final de la lista
frutas.append("kiwi")
print("Después de append:", frutas)  # Salida: ['manzana', 'fresa', 'naranja', 'kiwi']

# 4. Agregar múltiples elementos al final de la lista
otras_frutas = ["mango", "uva"]
frutas.extend(otras_frutas)
print("Después de extend:", frutas)  # Salida: ['manzana', 'fresa', 'naranja', 'kiwi', 'mango', 'uva']

# 5. Insertar un elemento en una posición específica
frutas.insert(2, "cereza")
print("Después de insert:", frutas)  # Salida: ['manzana', 'fresa', 'cereza', 'naranja', 'kiwi', 'mango', 'uva']

# 6. Eliminar el primer elemento que coincida con el valor
frutas.remove("fresa")
print("Después de remove:", frutas)  # Salida: ['manzana', 'cereza', 'naranja', 'kiwi', 'mango', 'uva']

# 7. Eliminar un elemento por índice y devolverlo
eliminado = frutas.pop(2)
print("Después de pop:", frutas)  # Salida: ['manzana', 'cereza', 'kiwi', 'mango', 'uva']
print("Elemento eliminado:", eliminado)  # Salida: naranja

# 8. Eliminar todos los elementos de la lista
frutas.clear()
print("Después de clear:", frutas)  # Salida: []

# 9. Buscar el índice de un elemento
frutas = ["manzana", "plátano", "naranja", "kiwi"]
indice = frutas.index("kiwi")
print("Índice de 'kiwi':", indice)  # Salida: 3

# 10. Verificar si un elemento está en la lista
if "manzana" in frutas:
    print("Manzana está en la lista.")
else:
    print("Manzana no está en la lista.")

# 11. Contar cuántas veces aparece un elemento
frutas.append("manzana")
print("Número de manzanas:", frutas.count("manzana"))  # Salida: 2

# 12. Ordenar la lista de forma ascendente
frutas.sort()
print("Lista ordenada:", frutas)  # Salida: ['kiwi', 'manzana', 'naranja', 'plátano']

# 13. Ordenar la lista de forma descendente
frutas.sort(reverse=True)
print("Lista ordenada en reversa:", frutas)  # Salida: ['plátano', 'naranja', 'manzana', 'kiwi']

# 14. Crear una nueva lista ordenada sin modificar la original
frutas_ordenadas = sorted(frutas)
print("Lista ordenada (sin modificar la original):", frutas_ordenadas)  # Salida: ['kiwi', 'manzana', 'naranja', 'plátano']
print("Lista original sin cambios:", frutas)

# 15. Invertir el orden de la lista
frutas.reverse()
print("Lista invertida:", frutas)  # Salida: ['kiwi', 'manzana', 'naranja', 'plátano']

# 16. Hacer una copia superficial de la lista
frutas_copia = frutas.copy()
print("Copia de la lista:", frutas_copia)  # Salida: ['kiwi', 'manzana', 'naranja', 'plátano']

# 17. Obtener la longitud de la lista
print("Número de elementos en frutas:", len(frutas))  # Salida: 4

# 18. Listas dentro de listas
listas_anidadas = [["manzana", "plátano"], ["naranja", "kiwi"]]
print("Lista anidada:", listas_anidadas)
print("Acceder a una sublista:", listas_anidadas[0])  # Salida: ['manzana', 'plátano']
print("Acceder a un elemento dentro de la sublista:", listas_anidadas[1][1])  # Salida: kiwi


# Comprobar si 'manzana' está en la lista
if "manzana" in frutas:
    print("Manzana está en la lista.")
else:
    print("Manzana no está en la lista.")

# Comprobar si 'kiwi' está en la lista
if "kiwi" in frutas:
    print("Kiwi está en la lista.")
else:
    print("Kiwi no está en la lista.")


# Resumen de métodos comunes para trabajar con listas:
# Método	Descripción	Ejemplo
# append()	Agrega un elemento al final	frutas.append("kiwi")
# extend()	Agrega múltiples elementos al final	frutas.extend(["mango", "uva"])
# insert()	Inserta un elemento en una posición	frutas.insert(2, "cereza")
# remove()	Elimina el primer elemento que coincida	frutas.remove("fresa")
# pop() 	Elimina el elemento en una posición	frutas.pop(1)
# clear()	Elimina todos los elementos	frutas.clear()
# index()	Devuelve el índice de un elemento	frutas.index("kiwi")
# count()	Cuenta cuántas veces aparece un valor	frutas.count("manzana")
# sort()	Ordena la lista	frutas.sort()
# reverse()	Invierte el orden de los elementos	frutas.reverse()
# copy()	Crea una copia superficial	frutas_copia = frutas.copy()
# len()	    Devuelve la longitud de la lista	len(frutas)