class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = num_rodas

    def ligar_motor(self):
        print("ligando o motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        # if(self.carregado == True):
            # print("está carregado")
        # else:
            # print("não está carregado")
        print(f"{'Sim,' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "abc-123", 2)
moto.ligar_motor()

carro = Carro("branco", "bvg-423", 4)
carro.ligar_motor()

caminhao = Caminhao("roxa", "gfo-9878", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()