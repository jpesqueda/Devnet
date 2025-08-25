
#Aquí tienes un programa en Python que pide números infinitamente y solo permite que el usuario ingrese números cada vez mayores. El programa finalizará cuando el usuario ingrese un número menor que el anterior.

print("Introduce números cada vez mayores. Si ingresas un número menor que el anterior, el programa terminará.")
numero_anterior = float("-inf")  # Inicializamos con un valor muy bajo

while True:
    try:
        numero = float(input("Introduce un número: "))  # Pedir número al usuario
        
        if numero <= numero_anterior:
            print("Número menor detectado. Terminando el programa.")
            break  # Salir del bucle si el número es menor o igual al anterior

        numero_anterior = numero  # Actualizar el número anterior
    except ValueError:
        print("Error: Debes ingresar un número válido.")



# Explicación del código:
# Se muestra un mensaje inicial explicando al usuario cómo funciona el programa.
# Se inicializa numero_anterior con float("-inf") para asegurar que cualquier número ingresado sea mayor en la primera iteración.
# Se usa un while True para pedir números infinitamente.
# Se usa try-except para manejar errores si el usuario ingresa algo que no sea un número.
# Si el número ingresado es menor o igual que el anterior, el programa muestra un mensaje y termina con break.
# Si el número es válido y mayor, se actualiza numero_anterior para la siguiente comparación.