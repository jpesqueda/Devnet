print("Introduce números positivos. Si ingresas un número negativo, el programa terminará.")

suma_total = 0  # Variable para almacenar la suma

while True:
    try:
        numero = float(input("Introduce un número: "))  # Pedir un número al usuario

        if numero < 0:
            print("Número negativo detectado. Terminando el programa.")
            break  # Salir del bucle si el número es negativo

        suma_total += numero  # Sumar el número a la suma total

    except ValueError:
        print("Error: Debes ingresar un número válido.")

# Mostrar la suma total de los números ingresados
print(f"La suma total de los números ingresados es: {suma_total}")