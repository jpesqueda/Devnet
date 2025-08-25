
#  Resumen de operadores
#  Aritméticos: +, -, *, /, %, //, **
#  Relacionales: ==, !=, >, <, >=, <=
#  Lógicos: and, or, not
#  Identidad: is, is not
#  Membresía: in, not in
#  Bit a bit: &, |, ^, ~, <<, >>




################   Operadores Aritméticos (+, -, *, /, %, //, ))
print ("Operadores Aritméticos (+, -, *, /, %, //, )")
a = 10
b = 3

if a + b == 13:
    print("Suma correcta")

if a - b == 7:
    print("Resta correcta")

if a * b == 30:
    print("Multiplicación correcta")

if a / b == 10 / 3:
    print("División correcta")

if a % b == 1:
    print("Residuo correcto")

if a // b == 3:
    print("División entera correcta")

if a ** b == 1000:
    print("Potencia correcta")
	
	
	
################   Operadores Aritméticos (==, !=, >, <, >=, <=)
print ("Operadores Relacionales (==, !=, >, <, >=, <=)")
x = 5
y = 10

if x == 5:
    print("x es igual a 5")

if y != 5:
    print("y es diferente de 5")

if y > x:
    print("y es mayor que x")

if x < y:
    print("x es menor que y")

if y >= 10:
    print("y es mayor o igual a 10")

if x <= 5:
    print("x es menor o igual a 5")
	


################  Operadores Lógicos (and, or, not)
print ("Operadores Lógicos (and, or, not)")
usuario = "admin"
contrasena = "1234"

if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido")

if usuario == "admin" or contrasena == "0000":
    print("Uno de los datos es correcto")

if not usuario == "user":
    print("El usuario no es 'user'")
	


################   Operadores de Identidad (is, is not)
print ("Operadores de Identidad (is, is not)")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

if a is b:  # Ambas variables apuntan al mismo objeto en memoria
    print("a y b son el mismo objeto")

if a is not c:  # Aunque tienen los mismos valores, son objetos diferentes
    print("a y c no son el mismo objeto")
	




################   Operadores de Membresía (in, not in)
print ("Operadores de Membresía (in, not in)")
lista = [1, 2, 3, 4, 5]

if 3 in lista:
    print("El número 3 está en la lista")

if 10 not in lista:
    print("El número 10 no está en la lista")
	
	


################   Operadores Bit a Bit (&, |, ^, ~, <<, >>
print("Operadores Bit a Bit (&, |, ^, ~, <<, >>)")

a = 5  # 101 en binario
b = 3  # 011 en binario

if a & b == 1:  # 101 & 011 = 001 (1)
    print("AND bit a bit correcto")

if a | b == 7:  # 101 | 011 = 111 (7)
    print("OR bit a bit correcto")

if a ^ b == 6:  # 101 ^ 011 = 110 (6)
    print("XOR bit a bit correcto")

if ~a == -6:  # Complemento a uno (NOT bit a bit)
    print("NOT bit a bit correcto")

if a << 1 == 10:  # 101 << 1 = 1010 (10)
    print("Desplazamiento a la izquierda correcto")

if a >> 1 == 2:  # 101 >> 1 = 10 (2)
    print("Desplazamiento a la derecha correcto")

