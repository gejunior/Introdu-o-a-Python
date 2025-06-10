class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

a1 = Estudante("gui", 1)
a2 = Estudante("geo", 2)

mostrar_valores(a1, a2)

Estudante.escola = "python"
a3 = Estudante("chappie", 3)

mostrar_valores(a1, a2, a3)

#metodos de classe
#metodos estáticos