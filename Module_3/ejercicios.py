
import math

def suma_hasta(num):
    i = 0
    total = 0 
    while i <= num:
        total += i
        i += 1

    print(total)


def contine_a(palabra):
    secreta = "a"
    for letra in palabra:
        if letra == secreta:
            return "¡Encontrada!"
    return "No esta"


num = 5
palabra = "perro"
print(contine_a(palabra))
# suma_hasta(10)


# Write your code below and press Shift+Enter to execute
def count_little(strings):
    pal = []
    pal = strings.split()

    dic = {}

    for key in pal:
        if key == "little":
            dic[key] = pal.count(key)
    print("Total count: ", dic)


strings = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
count_little(strings)


class car:
    color = "white"
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage
        self.capacity = None

    def add_seating_cap(self, capacity):
        self.capacity = capacity

    def show_info(self):
        print("Propiedades del coche:")
        print("color:", self.color)
        print("velocidad maxima:", self.speed)
        print("Mileage:", self.mileage )
        print("capacidad:", self.capacity)    

car1 = car(speed="200 kmph", mileage= "20 kmpl")
car1.add_seating_cap(5)
car1.show_info()

car2 = car(speed="180 kmph", mileage= "25 kmpl")
car2.add_seating_cap(4)
car2.show_info()


A = ['1','2','3']

for a in A:
    print(2*a)



def division(numerador, denominador):
    try:
        div = numerador/denominador
        return("Resul: ", div)
    except ZeroDivisionError:
        return("No se puede dividir por 0")



numerador = 8 # int(input("introduce num:"))
denominador = 3 # int(input("introduce den:"))

print(division(numerador,denominador))


def square_root(num):
    try:
        resu = math.sqrt(num)
        return "correcto: ", resu
    except ValueError:
        return("Invalid input! Please enter a positive integer or a float value.")

numero = 5 # int(input("introduce numero: "))
print(square_root(numero))

def math_complex(num):
    try:
        dif = num/5
        result = num/dif
        return result
    except Exception as e:
        return("An error occurred during calculation -> ", e)

num = 10 # int(input("introduce numero: "))

print(math_complex(num))


##########################
def cuenta_regresiva(n):
    while n > 0:
        print(n)
        n -= 1
    return "BOOM.!!"    

n = 5
print(cuenta_regresiva(n))

###################
def invertir_palabra(palabra):
    inver = ""
    for letra in palabra:
        inver = letra + inver
    return inver

palabra = "perro"
print(invertir_palabra(palabra))

########################
def clasificar_numeros(lista):
    for num in lista:
        if num == 0:
            print("Es cero", num)
        elif num < 0:
            print("Es negativo", num)
            if num % 2 == 0:
                print("Es par", num)
            else:
                print("Es impar", num)  
        elif num > 0:
            if num % 2 == 0:
                print("Es par", num)
            else:
                print("Es impar", num)    

lista = [5, 0, -3, 4, -2, 1]

print(clasificar_numeros(lista))

###################################

def fizzbuzz(n):
    for i in range(1, n+1):        
        if i % 3 == 0 and i % 5 == 0:
            print(i,"FizzBuzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        elif i % 5 == 0:
            print(i,"Buzz")
        else:
            print(i)


n = 15

fizzbuzz(n)