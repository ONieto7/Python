class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: {self.balance}€"

    def depositar(self, dinero_deposito):
        self.balance += dinero_deposito
        print("Deposito aceptado")

    def retirar(self, dinero_retiro):
        if self.balance >= dinero_retiro:
            self.balance -= dinero_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")


def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input().upper()

        if opcion == 'D':
            monto_dep = int(input("Cantidad a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Cantidad a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print("Gracias por operar en Banco Python")


inicio()