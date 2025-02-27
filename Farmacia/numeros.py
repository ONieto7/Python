#Generadores de numeros para las colas de la farmacia
def numeros_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"

def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"

def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}" 

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(seccion):

    print("\n" + "*" * 23)
    print("Su numero es: ")
    if seccion == "P":
        print(next(p))
    elif seccion == "F":
        print(next(f))
    elif seccion == "C":
        print(next(c))
    
    print("Esperre para ser atendido")
    print("*" * 23 + "\n")