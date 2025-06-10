class conta:
    def __init__(self, agencia, saldo =0):
        self.saldo = saldo
        self.agencia = agencia

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor

    def saldo(self):
        print(self.saldo)

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' 
                                                        for chave, valor in self.__dict__.items()])}"

conta = conta("001", 100)
print(conta.__str__())
