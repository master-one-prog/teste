class Conta():
    def __init__(self, saldo):
        self.saldo = saldo
    def sacar(self, retirada):
        saldo = saldo - retirada 
        print("Saque realizado com sucesso!!")
        print(f"Valor do saque: {retirada}")
        print(f"Saldo: {saldo}")

    def depositar(self, deposito):
        saldo += deposito
        print("Depósito realizado com sucesso!!")
        print(f"Valor do depósito: {deposito}")
        print(f"Saldo: {saldo}")

    def render(self):
        saldo *= 0.1
        print(saldo)
