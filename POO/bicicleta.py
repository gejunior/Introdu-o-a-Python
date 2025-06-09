class bicicleta:
    #SELF é a instancia do objeto q foi passado
    #é o this de java
    def __init__(self, cor, modelo, ano, valor): #construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def businar(self):
        print("plin plin")

    def parar(self):
        print("parô!!!")

    def correr(self):
        print("vruuuuum!")


b1 = bicicleta("vermelha", "caloy", 2022, 600) #instancia de bicicleta
b1.businar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
