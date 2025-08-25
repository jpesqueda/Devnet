
#El bucle while se ejecutaría de la siguiente forma
###Ejemplo while, imprime los primeros 20 numeros
i = 1
while i <= 25: 
    print(i)
    i += 1

# 1️ Bucle while básico
contador = 0
print("Bucle while básico:")
while contador < 5:
    print(contador)
    contador += 1  # Incrementar el contador
print()

# 2️ Bucle con condición de parada
print("Bucle con condición de parada:")
numero = 1
while numero != 0:
    numero = int(input("Introduce un número (0 para salir): "))
    print(f"Has introducido: {numero}")
print("Fin del programa.")
print()

# 3️ Bucle infinito con break
print("Bucle infinito con break:")
while True:
    respuesta = input("Escribe 'salir' para salir: ")
    if respuesta == 'salir':
        print("Saliendo del bucle.")
        break
    print(f"Has escrito: {respuesta}")
print()

# 4️ Bucle con continue
print("Bucle con continue:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Salta los números pares
    print(f"Imprimiendo número impar: {i}")
print()

# 5️ Bucle while con else
print("Bucle while con else:")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1
else:
    print("El bucle ha terminado sin interrupciones.")
print()

# 6️ Usar while para recorrer una lista
print("Usando while para recorrer una lista:")
numeros = [10, 20, 30, 40, 50]
indice = 0
print(len(numeros))
while indice < len(numeros):
    print(numeros[indice])
    indice += 1
print()

# 7️ Usar while con condiciones complejas
print("Usando while con condiciones complejas:")
numero = 0
while numero < 10 and numero != 5:
    print(f"Numero: {numero}")
    numero += 1
print()

# 8️ Bucle while con valor de retorno
print("Bucle while con valor de retorno:")
def contar_hasta_5():
    contador = 0
    while contador < 5:
        print(f"Contando: {contador}")
        contador += 1
    return "Contador finalizado"
print(contar_hasta_5())


