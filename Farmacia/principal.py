import numeros

def preguntar():
    print("Bienvenido a la farmacia")

    while True:
        print("Seleccione una seccion")
        print("[P] - Perfumeria")
        print("[F] - Farmacia")
        print("[C] - Cosmetica")

        try:
            mi_seccion = input("Ingrese una opcion: ").upper()
            ["P", "F", "C"].index(mi_seccion)
        except ValueError:
            print("Opcion incorrecta")
        else:
            break
    
    numeros.decorador(mi_seccion)

def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Desea otro turno? [S/N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Opcion incorrecta")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()
        