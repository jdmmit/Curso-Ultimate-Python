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

palabra = input("Ingresa una frase: ")

print(palabra[::-1])

# 8. ** Tablas de multiplicar**: Imprime la tabla de multiplicar de un número ingresado por el usuario.

num = int(input("Ingresa un número: "))
suma = sum(i for i in range(2, num+1, 2))
print(f"La suma de los números pares hasta {num} es: {suma}")


# 9. ** Suma de números pares**: Pide un número y muestra la suma de todos los números pares hasta ese número.

# 10. ** Números primos**: Escribe un programa que determine si un número es primo.

# ---
