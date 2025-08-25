print("Hola Mundo")

#imprimir desde una vriable 
mensaje="Hola Mundo variable"
print(mensaje)

#imprimir dos lineas en una utilizando el simbolo ;
print("Hola Mundo 2"); print("adios Mundo2")


#Para imprimir un número o texto en pantalla, usamos la función Printprint(‘Hola mundo’)
#Para recibir un texto por el usuario, empleamos la función Input

texto=input('Introduzca un numero: ')


#Si queremos recibir un número, tenemos que convertirlo con la función Int
num = int(input('Introduzca un numero: '))

#Las estructuras condicionales se realizan de forma similar a casi todos los lenguajes de programación. Por ejemplo, el siguiente código recibe un número del usuario, e dice si es par o impar.

### Introducir un numero por teclado y decir si es par o impar
num = int(input('Introduzca un numero: '))
ifnum % 2 == 0: 
print('Par')
else:
print('Impar')


#El bucle de tipo for si tiene ciertas particularidades. El siguiente ejemplo, muestra como imprimir en pantalla los 20 primeros números



###Ejemplo for, imprime los 20 primeros numeros en una linea
for i in range(20):
print(i, end=" ") #imprimir numero, sin salto linea
print() #lineavacia
#"Por su parte, un “equivalente” a un bucle de tipo foreach tendría la siguiente pinta



###Ejemplo foreach, imprime los numeros de la lista
for i in [1, 5, 7]:
print(i, end=" ") #imprimir numero, sin salto linea
print() #lineavacia
#Si ejecutamos el código en un texto, se ejecuta la acción para cada letra



###Ejemplo foreach, imprime las letras TEXTO
for i in "TEXTO":
print(i)
#El bucle while se ejecutaría de la siguiente forma



###Ejemplo while, imprime los primeros 20 numeros
i = 1
while i <= 25: 
print(i),
i += 1


#Por último para definir una función usamos la palabra reservada Def. 
#El siguiente ejemplo defina una función que calcula el máximo de dos números, 
# y cómo usarla para calcular el máximo entre 100 y 50.
###Ejemplo de función
defmax (n1, n2)
if n1 < n2
return n2
elif n2 < n1
return n1
else:
return n1

print(max(100, 50))