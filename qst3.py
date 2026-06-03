class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo > valor:
            self._saldo -= valor
            print("Realizado com suceso!")
        else:
            print("SALDO INSUFICIENTE")

class Poupanca(Conta):
    def __init__(self, saldo, taxa_rendimento):
        super().__init__(saldo)
        self.__taxa = taxa_rendimento

    def render(self):
        self._saldo *= self.__taxa

class ContaEspecial(Conta):
    def __init__(self, saldo, limite):
        super().__init__(saldo)
        self.__limite = limite

    def sacar_especial(self, valor):
        if valor > self._saldo:
            if self.__limite + self._saldo >= valor:
                print("Realizado com sucesso!")
            else:
                print("SALDO INSUFICIENTE")
        else:
            print("Realizado com sucesso!")



pop = Poupanca(1000.00, 0.1)
pop.depositar(100.00)
pop.sacar(20.00)
pop.render()

cot=ContaEspecial( 1000.00, 200.90)
cot.depositar(10.90)
cot.sacar_especial(10000.00)