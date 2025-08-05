# 🧪 Ejercicios prácticos para cada módulo del curso de Python
import math
import pandas as pd
import numpy as np
import requests as rqs

# ====================
# MODULE 1 - PYTHON BASICS
# ====================

# ✅ Ejercicio 1: Tu primer programa
# Imprime "Hola, mundo!" en pantalla
print("Hola, mundo!")
# ✅ Ejercicio 2: Tipos
# Crea una variable de tipo entero, flotante y string. Imprímelas junto a su tipo.
e = 5
f = 2.5
s = "variable"
print(type(e), e)
print(type(f), f)
print(type(s), s)
# ✅ Ejercicio 3: Expresiones y variables
# Calcula el área de un círculo de radio 5 (usa pi = 3.14) y guarda el resultado en una variable
radio = 5
print ("area = ", math.pi * radio ** 2)
# ✅ Ejercicio 4: Operaciones con strings
# Junta las palabras "Hola" y "mundo" en una sola cadena con un espacio entre ellas

str1 = "Hola"
str2 = "mundo"

print(str1 + " " + str2)

# ==========================
# MODULE 2 - DATA STRUCTURES
# ==========================

# ✅ Ejercicio 5: Listas y tuplas
# Crea una lista de 5 frutas. Cámbiala para que la primera fruta sea "pera"

frutas = ["manzana", "uva", "sandia", "pera", "tomate"]
print(frutas)
frutas[0] = "pera" 
print(frutas)
# ✅ Ejercicio 6: Sets
# Crea un set con los valores [1, 2, 2, 3, 4]. Imprime el set y fíjate qué pasó con los duplicados
set1 = {1, 2, 2, 3, 4}
print(set1)
# resp: los duplicados se eliminan

# ✅ Ejercicio 7: Diccionarios
# Crea un diccionario con tus datos: nombre, edad, y ciudad. Accede a la edad y súmale 1.

datos = {"nombre": "Bryan",
       "edad": 30,
       "ciudad": "Valencia"
       }

print(datos["edad"])
age = datos["edad"] + 1

print(age)


# ======================================
# MODULE 3 - PYTHON PROGRAMMING FUNDAMENTALS
# ======================================

# ✅ Ejercicio 8: Condiciones y ramas
# Escribe una función que reciba una edad y diga si la persona es mayor de edad o no

edad = 5 #int(input("introduce edad: "))

if edad >= 18:
    print("eres mayor de 18")
else:
    print("eres menor de 18")

# ✅ Ejercicio 9: Bucles
# Imprime los números del 1 al 10 usando un bucle for
for num in range(1,11):
    print(num)

# ✅ Ejercicio 10: Funciones
# Escribe una función que reciba un número y devuelva su cuadrado
def cuadrado(num):
    return num ** 2

num = 9 #float(input("introduce numero: "))
print("el cuadrado es:", cuadrado(num))

# ✅ Ejercicio 11: Objetos y clases
# Crea una clase "Perro" con los atributos "nombre" y "edad". Crea un objeto y muestra sus datos.
class perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("nombre:", self.nombre)
        print("edad:", self.edad)
       
dog = perro("Firulo", 8)

dog.imprimir()

# ====================================
# MODULE 4 - WORKING WITH DATA IN PYTHON
# ====================================

# ✅ Ejercicio 12: Leer archivos
# Crea un archivo de texto con varias líneas. Ábrelo y muestra su contenido línea por línea

with open("./python/ejercicio_12.txt", 'r') as file:
    for line in file:
        print(line)     

# ✅ Ejercicio 13: Escribir archivos
# Escribe 3 líneas de texto en un nuevo archivo llamado "salida.txt"
with open("./python/salida.txt", 'w') as file:
    lines = ["Mapache\n", "Mapachosa\n", "Mapachillo\n"]

    for line in lines:
        file.write(line)

with open("./python/salida.txt", 'r') as file:
    print("nuevo")
    for lin in file:
        print(lin)    

# ✅ Ejercicio 14: Cargar datos con Pandas
# Carga un CSV con pandas (usa uno genérico como ejemplo.csv si no tienes uno propio)
with pd.ExcelFile('python/iso.xlsx') as xls:
    df = pd.read_excel(xls)
    print(df.head())

# ✅ Ejercicio 15: Guardar datos con Pandas
# Crea un DataFrame con pandas y guárdalo como "datos.csv"

data = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]

frame = pd.DataFrame(data)

frame.to_csv('datos.csv', index=False)
    

# ============================================
# MODULE 5 - NUMPY ARRAYS AND SIMPLE APIS
# ============================================

# ✅ Ejercicio 16: Numpy 1D Arrays
# Crea un array de numpy con los números del 0 al 9 y calcula su media
datos = range(0,10)
arr = np.array(datos)
print(arr)
print(arr.mean())

# ✅ Ejercicio 17: Numpy 2D Arrays
# Crea una matriz 3x3 con valores del 1 al 9 e imprime la diagonal principal

mat = np.arange(1,10).reshape(3, 3)
print(mat)

diagonal = []
for i in range(len(mat)):
    diagonal.append(mat[i][i])
print(diagonal)    

# ✅ Ejercicio 18: Usar una API simple (ej. chiste aleatorio)
# Usa el módulo `requests` para llamar a una API pública y mostrar un resultado (por ejemplo: chiste)

r = rqs.get('https://api.chucknorris.io/jokes/random')
print(r.status_code)

resp = r.json()

#print(resp)

print(resp['value'])

# ✅ Ejercicio 19: Configurar API
# (Opcional) Escribe una función que reciba una URL y devuelva el JSON de la respuesta

try:
    r = rqs.get('https://api.chucknorris.io/jokes/random')
    print(r.status_code)
    if r.status_code == 200:
        resp = r.json()
        print(resp)
    else:
        print("Hay un error", r.status_code)    
except Exception as e:
    print("error:", e)

# === FIN DE LA PRÁCTICA ===