# Aquí tienes una lista de ejercicios para practicar Python, organizados por nivel de dificultad:

# ---

# 🟢 **Nivel Básico**

# 1. ** Operaciones matemáticas**: Escribe un programa que solicite dos números al usuario y muestre la suma, resta, multiplicación y división de ellos.

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

print("Operaciones disponibles:\n\t1- Suma\n\t2- Resta\n\t3- Multiplicación\n\t4- División")
operacion = input(
    "Introduce el número correspondiente al tipo de operación que quieres realizar: ")

if operacion == "1":
    resultado = numero_1 + numero_2
    print(f"La suma de {numero_1} y {numero_2} es: {resultado}")
elif operacion == "2":
    resultado = numero_1 - numero_2
    print(f"La resta de {numero_1} y {numero_2} es: {resultado}")
elif operacion == "3":
    resultado = numero_1 * numero_2
    print(f"La multiplicación de {numero_1} y {numero_2} es: {resultado}")
elif operacion == "4":
    if numero_2 != 0:
        resultado = numero_1 / numero_2
        print(f"La división de {numero_1} entre {numero_2} es: {resultado}")
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no válida.")

# 2. ** Par o impar**: Pide un número al usuario y determina si es par o impar.

numero = int(input("Introduce un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")


# 3. ** Área de un triángulo**: Calcula el área de un triángulo a partir de su base y altura.

base = float(input("Ingresa el valor de la base del triangulo :"))
altura = float(input("Ingresa el calor de la altura del triangulo :"))
area = (base * altura) / 2

print(f"El area de el triangulo es {area}")


# 4. ** Conversión de temperatura**: Convierte grados Celsius a Fahrenheit.

temperatura = float(input("Ingresa la temperatura :"))
fahrenheit = float(temperatura * 1.8) + 32

print(f"La temperetura en fahrenheit es {fahrenheit}")

# 5. ** Año bisiesto**: Pide un año al usuario y determina si es bisiesto.

año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

# 6. ** Contador de caracteres**: Solicita una frase y muestra cuántos caracteres tiene(sin contar espacios).

frase = input("Ingresa una frase: ")
print(f"Número de caracteres (sin espacios): {len(frase.replace(' ', ''))}")


# 7. ** Inversión de cadena**: Pide al usuario una palabra y muéstrala al revés.

palabra = input("Ingresa una palabra: ")

print(palabra[::-1])

# 8. ** Tablas de multiplicar**: Imprime la tabla de multiplicar de un número ingresado por el usuario.

num = int(input("Ingresa un número: "))
suma = sum(i for i in range(2, num+1, 2))
print(f"La suma de los números pares hasta {num} es: {suma}")


# 9. ** Suma de números pares**: Pide un número y muestra la suma de todos los números pares hasta ese número.

num = int(input("Ingresa un número: "))
suma = sum(i for i in range(2, num+1, 2))
print(f"La suma de los números pares hasta {num} es: {suma}")


# 10. ** Números primos**: Escribe un programa que determine si un número es primo.

num = int(input("Ingresa un número: "))
if num < 2:
    print("El número no es primo.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("El número no es primo.")
            break
    else:
        print("El número es primo.")

# ---

# Ejercicios Nuevos - Nivel Básico
# Calculadora de edad en días : Pide al usuario su edad en años y muestra cuántos días ha vivido aproximadamente.

edad = int(input("Ingresa tu edad: "))
dias = edad * 365
print(f"Has vivido aproximadamente {dias} días.")


# Cálculo del perímetro y área de un círculo : Solicita la radio de un círculo y muestra su perímetro y área. Usa math.pipara obtener π.

radio = float(input("Ingresa el radio del círculo: "))
perimetro = 2 * 3.1416 * radio
area = 3.1416 * radio**2    
print(f"El perímetro del círculo es {perimetro} y su área es {area}.")



# Conversión de kilómetros a millas : Pide una cantidad en kilómetros y conviértela a millas (1 km = 0,621371 millas).

kilometros = float(input("Ingresa la cantidad en kilómetros: "))
millas = kilometros * 0.621371
print(f"{kilometros} kilómetros equivalen a {millas} millas.")


# Promedio de tres números : Solicita tres números al usuario y muestra su promedio.

numero_1 = float(input("Ingresa el primer número: "))
numero_2 = float(input("Ingresa el segundo número: "))      
numero_3 = float(input("Ingresa el tercer número: "))

promedio = (numero_1 + numero_2 + numero_3) / 3
print(f"El promedio de los tres números es {promedio}.")



# Cálculo del factorial : Pide un número entero positivo y calcula su factorial sin usar librerías.

numero = float(input("Ingresa un número entero positivo: "))
factorial = 1
if numero < 0:
    print("El número debe ser positivo.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, int(numero) + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}.")

# Contador de vocales : Pide una palabra o frase y muestra cuántas vocales tiene.

palabra = input("Ingresa una palabra o frase: ")
vocales = sum(1 for i in palabra if i in "aeiouAEIOU")
print(f"La palabra o frase tiene {vocales} vocal(es).") 


# Verificación de palíndromos : Pide una palabra y verifica si se lee igual al revés.

palabra = input("Ingresa una palabra: ")
if palabra == palabra[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
    
    

# Generador de números pares : Solicita un número ny muestra los primeros nnúmeros pares.

numero = int(input("Ingresa un número: "))
pares = [i for i in range(2, numero*2, 2)]
print(f"Los primeros {numero} números pares son: {pares}")


# Generador de Fibonacci : Pide un número ny muestra los primeros nnúmeros de la serie de Fibonacci.

numero = int(input("Ingresa un número: "))
fibonacci = [0, 1]
for i in range(2, numero):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(f"Los primeros {numero} números de la serie de Fibonacci son: {fibonacci}")

# Adivina el número : Genera un número aleatorio entre 1 y 10 y pide al usuario que lo adivine. Responde si el número ingresado es mayor o menor hasta que aciertes.

import random

numero = random.randint(1, 10)
adivina = int(input("Adivina el número entre 1 y 10: "))
while adivina != numero:
    if adivina < numero:
        adivina = int(input("Intenta con un número mayor: "))
    else:
        adivina = int(input("Intenta con un número menor: "))
print("¡Correcto!")
