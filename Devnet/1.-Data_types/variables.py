# 1. Variable de tipo entero (int)
edad = 25
print("Edad:", edad)

# 2. Variable de tipo flotante (float)
precio = 19.99
print("Precio:", precio)

# 3. Variable de tipo cadena de texto (str)
nombre = "Carlos"
print("Nombre:", nombre)

# 4. Variable de tipo booleano (bool)
es_mayor = True
print("¿Es mayor de edad?", es_mayor)

# 5. Variable tipo lista (list)
frutas = ["manzana", "plátano", "naranja"]
print("Lista de frutas:", frutas)

# 6. Variable tipo tupla (tuple)
coordenadas = (10, 20)
print("Coordenadas:", coordenadas)

# 7. Variable tipo diccionario (dict)
persona = {"nombre": "Carlos", "edad": 30, "ciudad": "México"}
print("Información de la persona:", persona)

# 8. Variable tipo conjunto (set)
numeros_unicos = {1, 2, 3, 4, 5}
print("Conjunto de números:", numeros_unicos)

# 9. Asignación múltiple
a, b, c = 10, 20, 30
print("Asignación múltiple:", a, b, c)

# 10. Variable con None (sin valor)
x = None
print("Valor de x:", x)

# 11. Conversión de tipo
num = "100"  # Tipo str
num = int(num)  # Convertir a entero
print("Conversión de tipo:", num + 50)

# 12. Variables globales y locales
mensaje = "Hola, mundo"  # Variable global

def imprimir_mensaje():
    mensaje = "Hola desde la función"  # Variable local
    print("Mensaje dentro de la función:", mensaje)

imprimir_mensaje()  # Salida: Hola desde la función
print("Mensaje global:", mensaje)  # Salida: Hola, mundo