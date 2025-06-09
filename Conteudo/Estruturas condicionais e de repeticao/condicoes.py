#Estrutura condicional permite o desvio de fluxo de controle,
#quando determinadas expressões lógicas são atendidas.

#IF
#testa a expressão lógica, se for verdadeira executa o bloco de código
#correspondente, caso contrário pula para o próximo bloco de código.
#Sintaxe:
# if <expressão lógica>:
#     <bloco de código>
# Exemplo de uso do if
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
# Exemplo de uso do if com operadores lógicos
idade = 16

saldo = 2000.0
saque  = float(input("informe o valor do saque: R$ "))

if saldo >= saque and saque > 0:
    saldo -= saque
    print(f"Saque de R$ {saque:.2f} realizado com sucesso.")

if conta_normal:
    if saldo >= saque and saque > 0:
        saldo -= saque
        print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente ou valor de saque inválido.")
elif idade >= 18 and idade < 65:
    if saldo >= saque and saque > 0:
        saldo -= saque
        print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente ou valor de saque inválido.")
