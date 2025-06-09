class cachorro:
    def __init__(self, nome, cor, acordado = True): #Construtor
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def falar(self):
        print("au au")

    def __del__(self):
        print("removendo estancia da classe") #Destrutor

c = cachorro("chappie","amarelo")
c.falar