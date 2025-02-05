#Las estructuras condicionales se realizan de forma similar a casi todos los lenguajes de programación. Por ejemplo, el siguiente código recibe un número del usuario, e dice si es par o impar.
### Introducir un numero por teclado y decir si es par o impar
num = int(input('Introduzca un número: ')) 
if num % 2 == 0:
    print('Este numero es Par')  
else:
    print('Impar') 



#Si ejecutamos el código en un texto, se ejecuta la acción para cada letra
###Ejemplo foreach, imprime las letras TEXTO
for i in "TEXTO":
    print(i)

## Ejemplos de la condicion if 

####1. Condición simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

####2. Condición con else
numero = 5
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")



####3. Condiciones con elif
calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bien")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")


####4. Uso de if con operadores lógicos (and, or, not)
usuario = "admin"
contrasena = "1234"

if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")

####5. Uso de if en una sola línea (Operador ternario)

edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)


####6. Uso de if dentro de un bucle
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")

####7. Uso de if con listas y el operador in
frutas = ["manzana", "plátano", "naranja"]
if "manzana" in frutas:
    print("La manzana está en la lista")


####8. Uso de if con None
valor = None
if valor is None:
    print("El valor es None")

20
####9. Uso de if con try-except
try:
    numero = int(input("Ingresa un número: "))
    if numero > 0:
        print("El número es positivo")
    elif numero < 0:
        print("El número es negativo")
    else:
        print("El número es cero")
except ValueError:
    print("Eso no es un número válido")

####10. Uso de if con funciones
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print(es_par(4))  # True
print(es_par(7))  # False
