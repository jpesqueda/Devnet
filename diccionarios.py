# Resumen de los métodos y operaciones más comunes con diccionarios:
# Método	Descripción	Ejemplo
# get()	    Obtener un valor sin generar error si no existe	    persona.get("nombre")
# keys()	Obtener todas las claves del diccionario	        persona.keys()
# values()	Obtener todos los valores del diccionario	        persona.values()
# items()	Obtener todos los pares clave-valor	                persona.items()
# update()	Actualizar el diccionario con otro diccionario	    persona.update({"ciudad": "México"})
# copy()	Copiar el diccionario	                            persona.copy()
# clear()	Limpiar todos los elementos del diccionario	        persona.clear()
# del	    Eliminar un elemento del diccionario	            del persona["ciudad"]
# in	    Verificar si una clave está en el diccionario	    "nombre" in persona
# len()	    Obtener el número de elementos del diccionario	    len(persona)

# 1. Crear un diccionario
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "México"
}
print("Diccionario original:", persona)

# 2. Acceder a los valores por clave
print("Nombre:", persona["nombre"])  # Salida: Carlos
print("Edad:", persona["edad"])  # Salida: 30

# 3. Modificar un valor
persona["edad"] = 31
print("Diccionario después de modificar edad:", persona)

# 4. Agregar un nuevo par clave-valor
persona["profesión"] = "Ingeniero"
print("Diccionario después de agregar profesión:", persona)

# 5. Eliminar un elemento con `del`
del persona["ciudad"]
print("Diccionario después de eliminar ciudad:", persona)

# 6. Obtener un valor con `get()`
print("Profesión:", persona.get("profesión"))  # Salida: Ingeniero
print("Dirección:", persona.get("dirección", "No disponible"))  # Si no existe, devuelve "No disponible"

# 7. Verificar si una clave existe en el diccionario con `in`
if "nombre" in persona:
    print("La clave 'nombre' existe en el diccionario.")

# 8. Obtener todas las claves con `keys()`
claves = persona.keys()
print("Claves:", claves)

# 9. Obtener todos los valores con `values()`
valores = persona.values()
print("Valores:", valores)

# 10. Obtener todos los pares clave-valor con `items()`
items = persona.items()
print("Pares clave-valor:", items)

# 11. Copiar un diccionario con `copy()`
persona_copia = persona.copy()
print("Copia del diccionario:", persona_copia)

# 12. Limpiar el diccionario con `clear()`
persona.clear()
print("Diccionario después de clear:", persona)  # Salida: {}

# 13. Obtener la longitud del diccionario con `len()`
persona = {"nombre": "Carlos", "edad": 30}
print("Número de elementos en el diccionario:", len(persona))  # Salida: 2

# 14. Actualizar un diccionario con `update()`
persona.update({"ciudad": "México", "profesión": "Ingeniero"})
print("Diccionario después de update:", persona)

# 15. Iterar sobre un diccionario con un bucle
print("Iterando sobre las claves y valores del diccionario:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# 16. Tuplas como claves
diccionario_con_tuplas = {("a", 1): "valor1", ("b", 2): "valor2"}
print("Diccionario con tuplas como claves:", diccionario_con_tuplas)



# Crear y acceder a diccionarios: Mostramos cómo crear un diccionario y acceder a sus valores usando las claves.
# Modificar, agregar y eliminar elementos: Se explica cómo modificar un valor, agregar un nuevo par clave-valor y eliminar un elemento del diccionario.
# Métodos comunes:
# get(): Obtener un valor de forma segura (sin generar error si no existe la clave).
# keys(), values(), items(): Obtener las claves, valores y pares clave-valor respectivamente.
# copy(): Copiar el diccionario.
# clear(): Limpiar el diccionario.
# update(): Actualizar un diccionario con otros pares clave-valor.
# Verificación de claves: Usamos in para comprobar si una clave existe en el diccionario.
# Iteración: Cómo iterar sobre un diccionario con un bucle for.
# Uso de tuplas como claves: Mostrar que las tuplas pueden ser usadas como claves en un diccionario, ya que son inmutables.


