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


# 3. ** Área de un triángulo**: Calcula el área de un triángulo a partir de su base y altura.


# 4. ** Conversión de temperatura**: Convierte grados Celsius a Fahrenheit.


# 5. ** Año bisiesto**: Pide un año al usuario y determina si es bisiesto.


# 6. ** Contador de caracteres**: Solicita una frase y muestra cuántos caracteres tiene(sin contar espacios).


# 7. ** Inversión de cadena**: Pide al usuario una palabra y muéstrala al revés.


# 8. ** Tablas de multiplicar**: Imprime la tabla de multiplicar de un número ingresado por el usuario.


# 9. ** Suma de números pares**: Pide un número y muestra la suma de todos los números pares hasta ese número.


# 10. ** Números primos**: Escribe un programa que determine si un número es primo.


# ---
