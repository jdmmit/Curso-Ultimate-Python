animal = "  chanCHito feliz  "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("cH"))
print(animal.replace("nCH", "j"))
print("nCH" in animal)
print("nCH" not in animal)

# Métodos de cadenas (str)

# 1. str.lower(): Convierte todos los caracteres de la cadena a minúsculas.
texto = "Hola Mundo"
print(texto.lower())  # Salida: hola mundo

# 2. str.upper(): Convierte todos los caracteres de la cadena a mayúsculas.
texto = "Hola Mundo"
print(texto.upper())  # Salida: HOLA MUNDO

# 3. str.capitalize(): Convierte el primer carácter de la cadena a mayúscula y el resto a minúscula.
texto = "hola mundo"
print(texto.capitalize())  # Salida: Hola mundo

# 4. str.strip(): Elimina los espacios en blanco al principio y al final de la cadena.
texto = "   Hola Mundo   "
print(texto.strip())  # Salida: Hola Mundo

# 5. str.replace(): Reemplaza todas las ocurrencias de una subcadena por otra.
texto = "Hola Mundo"
print(texto.replace("Mundo", "Python"))  # Salida: Hola Python

# 6. str.split(): Divide una cadena en una lista utilizando un separador.
texto = "manzana,pera,plátano"
print(texto.split(","))  # Salida: ['manzana', 'pera', 'plátano']

# 7. str.join(): Une elementos de un iterable en una cadena utilizando un separador.
frutas = ['manzana', 'pera', 'plátano']
print(", ".join(frutas))  # Salida: manzana, pera, plátano

# 8. str.find(): Devuelve el índice de la primera aparición de una subcadena o -1 si no se encuentra.
texto = "Hola Mundo"
print(texto.find("Mundo"))  # Salida: 5

# 9. str.startswith(): Devuelve True si la cadena comienza con el prefijo especificado.
texto = "Hola Mundo"
print(texto.startswith("Hola"))  # Salida: True

# 10. str.endswith(): Devuelve True si la cadena termina con el sufijo especificado.
texto = "Hola Mundo"
print(texto.endswith("Mundo"))  # Salida: True

# 11. str.isdigit(): Devuelve True si todos los caracteres de la cadena son dígitos.
texto = "12345"
print(texto.isdigit())  # Salida: True

# 12. str.isalpha(): Devuelve True si todos los caracteres de la cadena son letras.
texto = "Hola"
print(texto.isalpha())  # Salida: True

# 13. str.count(): Cuenta las veces que una subcadena aparece en la cadena.
texto = "banana"
print(texto.count("a"))  # Salida: 3

# 14. str.index(): Devuelve el índice de la primera aparición de una subcadena o lanza un error si no se encuentra.
texto = "Hola Mundo"
print(texto.index("Mundo"))  # Salida: 5

# Métodos de listas (list)

# 15. list.append(): Agrega un elemento al final de la lista.
numeros = [1, 2, 3]
numeros.append(4)
print(numeros)  # Salida: [1, 2, 3, 4]

# 16. list.pop(): Elimina y devuelve el elemento en el índice especificado (por defecto, el último).
numeros = [1, 2, 3]
print(numeros.pop())  # Salida: 3
print(numeros)  # Salida: [1, 2]

# 17. list.insert(): Inserta un elemento en una posición específica.
numeros = [1, 2, 3]
numeros.insert(1, 5)
print(numeros)  # Salida: [1, 5, 2, 3]

# 18. list.remove(): Elimina la primera aparición de un elemento.
numeros = [1, 2, 3, 2]
numeros.remove(2)
print(numeros)  # Salida: [1, 3, 2]

# 19. list.sort(): Ordena la lista en su lugar.
numeros = [3, 1, 2]
numeros.sort()
print(numeros)  # Salida: [1, 2, 3]

# 20. list.reverse(): Invierte el orden de los elementos en la lista.
numeros = [1, 2, 3]
numeros.reverse()
print(numeros)  # Salida: [3, 2, 1]

# 21. list.clear(): Elimina todos los elementos de la lista.
numeros = [1, 2, 3]
numeros.clear()
print(numeros)  # Salida: []

# Métodos de diccionarios (dict)

# 22. dict.get(): Devuelve el valor asociado a una clave o un valor por defecto si no existe.
datos = {"nombre": "Juan", "edad": 30}
print(datos.get("edad", "No disponible"))  # Salida: 30

# 23. dict.keys(): Devuelve una vista de las claves del diccionario.
datos = {"nombre": "Juan", "edad": 30}
print(datos.keys())  # Salida: dict_keys(['nombre', 'edad'])

# 24. dict.values(): Devuelve una vista de los valores del diccionario.
datos = {"nombre": "Juan", "edad": 30}
print(datos.values())  # Salida: dict_values(['Juan', 30])

# 25. dict.items(): Devuelve una vista de los pares clave-valor del diccionario.
datos = {"nombre": "Juan", "edad": 30}
print(datos.items())  # Salida: dict_items([('nombre', 'Juan'), ('edad', 30)])

# 26. dict.update(): Actualiza el diccionario con pares clave-valor de otro diccionario.
datos = {"nombre": "Juan"}
datos.update({"edad": 30})
print(datos)  # Salida: {'nombre': 'Juan', 'edad': 30}

# 27. dict.pop(): Elimina una clave y devuelve su valor.
datos = {"nombre": "Juan", "edad": 30}
edad = datos.pop("edad")
print(edad)  # Salida: 30
print(datos)  # Salida: {'nombre': 'Juan'}

# Métodos de conjuntos (set)

# 28. set.add(): Agrega un elemento al conjunto.
numeros = {1, 2, 3}
numeros.add(4)
print(numeros)  # Salida: {1, 2, 3, 4}

# 29. set.remove(): Elimina un elemento del conjunto, generando un error si no existe.
numeros = {1, 2, 3}
numeros.remove(2)
print(numeros)  # Salida: {1, 3}

# 30. set.union(): Devuelve la unión de dos conjuntos.
a = {1, 2}
b = {2, 3}
print(a.union(b))  # Salida: {1, 2, 3}

# 31. set.intersection(): Devuelve la intersección de dos conjuntos.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # Salida: {2, 3}

# 32. set.difference(): Devuelve los elementos del conjunto que no están en el otro.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))  # Salida: {1}

# 33. set.symmetric_difference(): Devuelve los elementos no comunes entre dos conjuntos.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))  # Salida: {1, 4}

# 34. set.discard(): Elimina un elemento del conjunto sin generar error si no existe.
numeros = {1, 2, 3}
numeros.discard(4)  # No genera error
print(numeros)  # Salida: {1, 2, 3}

# Métodos de tuplas (tuple)

# 35. tuple.count(): Devuelve la cantidad de veces que un valor aparece en la tupla.
tupla = (1, 2, 2, 3)
print(tupla.count(2))  # Salida: 2

# 36. tuple.index(): Devuelve el índice de la primera aparición de un valor.
tupla = (1, 2, 3)
print(tupla.index(2))  # Salida: 1
