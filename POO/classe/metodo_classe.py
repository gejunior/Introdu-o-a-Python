class Pessoa:
    def __init__(self, nome= None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_apartir_data_nasc(cls, ano, mes, dia, nome):#se preciso de estância de objeto, metodo de classe
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):#ñ preciso de estância de objeto, metodo estatico
        return idade >= 18

# p = Pessoa("Genilson", 23)
# print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nasc(2002,1,14,"Genilson")
print(p2.nome, p2.idade)