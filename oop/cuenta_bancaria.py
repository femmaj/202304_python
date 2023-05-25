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

cuenta1 = CuentaBancaria(0.01, 100)
cuenta1.deposito(50).deposito(100).deposito(50).retiro(20).generar_interes().mostrar_info()

cuenta2 = CuentaBancaria(0.01, 500)
cuenta2.deposito(100).deposito(300).retiro(50).retiro(100).retiro(30).retiro(70).generar_interes().mostrar_info()