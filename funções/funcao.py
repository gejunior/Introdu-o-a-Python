def exibir_mensagem():
    print("Olá mundo!")

exibir_mensagem()

#Args e kwargs
def exibir_informacoes(nome, idade, **kwargs):
    print(f"Nome: {nome}, Idade: {idade}")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_informacoes("João", 30, cidade="São Paulo", profissao="Engenheiro") 
#Args são argumentos posicionais, enquanto kwargs são argumentos nomeados que permitem passar um número variável de argumentos adicionais.

# Função com retorno
def calcular_area(base, altura):
    return base * altura
area = calcular_area(5, 10)
print(f"A área do retângulo é: {area}")

# Função com parâmetros padrão
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")
saudacao()  # Chama a função sem passar o parâmetro, usa o valor padrão
def saudacao_personalizada(nome):
    print(f"Olá, {nome}!")
saudacao_personalizada("Maria")  # Chama a função passando um nome personalizado


#positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Fusca", 1970, "ABC-1234", marca="Volkswagen", motor="1.6", combustivel="Gasolina")
#válido
# criar_carro(modelo="Fusca", ano=1970, placa="ABC-1234", marca="Volkswagen", motor="1.6", combustivel="Gasolina")
#inválido

#keyword only
def criar_usuario(nome, idade, *, email, senha):
    print(f"Usuário: {nome}, Idade: {idade}, Email: {email}, Senha: {senha}")

criar_usuario("João", 30, email="a", senha ="b")
#válido
# criar_usuario("João", 30, "a", "b")  # inválido, pois email e senha são keyword only

#soma
def soma(a, b):
    return a + b

def funcao_soma(funcao, x, y):
    resultado = funcao(x, y)
    print(f"O resultado da soma é: {resultado}")

funcao_soma(soma, 5, 10)  # Passando a função soma como argumento

salario = 2000

def calcular_salario(bonus):
    global salario
    salario += bonus
    return salario

calcular_salario(500)

def calcular_salario(bonus, lista):
    global salario

    lista_aux = lista.copy() 
    lista_aux.append(2)
    print(f"Lista dentro da função: {lista_aux}")
    salario += bonus
    return salario

lista = [1]
calcular_salario(500, lista)
print(f"Lista fora da função: {lista}")
