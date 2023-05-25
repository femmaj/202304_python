class Usuario:
    def __init__(self, name):
        self.name = name
        self.balance_cuenta = 0

    def hacer_deposito (self, amount):
        self.balance_cuenta += amount

    def hacer_retiro (self, amount):
        self.balance_cuenta -= amount

    def mostrar_balance_usuario (self):
        print(f"Usuario: {self.name} - Balance: {self.balance_cuenta}")

    def transferir_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount

usuario1 = Usuario("Fernanda")
usuario1.hacer_deposito(100)
usuario1.hacer_deposito(300)
usuario1.hacer_deposito(200)
usuario1.hacer_retiro(100)
usuario1.mostrar_balance_usuario()

usuario2 = Usuario("Antonia")
usuario2.hacer_deposito(1000)
usuario2.hacer_deposito(200)
usuario2.hacer_retiro(400)
usuario2.hacer_retiro(100)
usuario2.mostrar_balance_usuario()

usuario3 = Usuario("Andrea")
usuario3.hacer_deposito(1100)
usuario3.hacer_retiro(100)
usuario3.hacer_retiro(100)
usuario3.hacer_retiro(300)
usuario3.mostrar_balance_usuario()

usuario1.transferir_dinero(usuario3, 100)
usuario1.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()