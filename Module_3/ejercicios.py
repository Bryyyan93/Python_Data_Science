
def suma_hasta(num):
    i = 0
    total = 0 
    while i <= num:
        total += i
        i +=1

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
#suma_hasta(10)