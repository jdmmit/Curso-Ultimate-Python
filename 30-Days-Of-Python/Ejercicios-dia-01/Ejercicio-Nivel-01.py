import math

"""Escriba un ejemplo para diferentes tipos de datos de Python, como Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set y Dictionary."""
# Number
integer_example = 10
float_example = 10.5
complex_example = 2 + 3j

print(integer_example)
print(float_example)
print(complex_example)

# String
string_example = "Hello, World!"

print(string_example)   

# Boolean
boolean_example = True

print(boolean_example)

# List
list_example = [1, 2, 3, 4, 5]

print(list_example)

# Tuple
tuple_example = (1, 2, 3, 4, 5)

print(tuple_example)

# Set
set_example = {1, 2, 3, 4, 5}

print(set_example)
# Dictionary
dictionary_example = {"name": "John", "age": 30, "city": "New York"}

print(dictionary_example)


"""Halla una distancia euclidiana entre (2, 3) y (10, 8)"""

point1 = (2, 3)
point2 = (10, 8)

euclidean_distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

print("La distancia euclidiana entre {} y {} es: {}".format(point1, point2, euclidean_distance))



