#estética
# Indentação e blocos de código
# A indentação é importante em Python, pois define blocos de código.
# Em Python, a indentação é obrigatória e define o escopo dos blocos de código.
# Exemplo de uso de indentação
if True:
    print("Este é um bloco de código indentado.")
    if False:
        print("Este é um bloco de código aninhado.")
    print("Ainda dentro do primeiro bloco.")
# Exemplo de uso de indentação com loops
for i in range(3):
    print(f"Iteração {i}")
    if i % 2 == 0:
        print("Este é um número par.")
    else:
        print("Este é um número ímpar.")
# Exemplo de uso de indentação com funções
def exemplo_funcao():
    print("Esta é uma função.")
    if True:
        print("Dentro da função, dentro de um bloco condicional.")
    for j in range(2):
        print(f"Loop dentro da função: iteração {j}")
# Chamada da função
exemplo_funcao()
# Exemplo de uso de indentação com classes
class ExemploClasse:
    def metodo(self):
        print("Este é um método da classe.")
        if True:
            print("Dentro do método, dentro de um bloco condicional.")
        for k in range(2):
            print(f"Loop dentro do método: iteração {k}")
# Criação de uma instância da classe e chamada do método
exemplo_objeto = ExemploClasse()
exemplo_objeto.metodo()
# Exemplo de uso de indentação com listas
lista_exemplo = [1, 2, 3]
for numero in lista_exemplo:
    print(f"Número da lista: {numero}")
    if numero % 2 == 0:
        print("Este é um número par.")
    else:
        print("Este é um número ímpar.")
# Exemplo de uso de indentação com dicionários
