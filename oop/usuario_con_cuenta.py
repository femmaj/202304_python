class Usuario:
    def __init__(self, name):
        self.name = name
        self.cuenta = CuentaBancaria(0.01, 0)

    def hacer_deposito (self):
        self.cuenta.deposito(850)
        return self

    def hacer_retiro (self):
        self.cuenta.retiro(100)
        return self

    def mostrar_balance_usuario (self):
        print(f"Usuario: {self.name} - Balance: {self.cuenta}")
        return self

    def transferir_dinero(self, other_user, amount):
        self.cuenta -= amount
        other_user.cuenta += amount
        return self


class CuentaBancaria:
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance - amount >=0:
            self.balance -= amount
        else:
            print("No tienes fondos suficientes")
        return self
    
    def mostrar_info(self):
        print(f"Tu balance es: {self.balance}")
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.tasa_interes)
        return self
    
    def __str__(self) -> str:
        return f"{self.balance}"

usuario1 = Usuario("Fernanda")
usuario1.hacer_deposito().mostrar_balance_usuario()

