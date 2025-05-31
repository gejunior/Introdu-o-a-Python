saldo = 1000
saque = 200
limite = 100
print(saldo >= saque and saque <= limite) 
#>>> False
#ambos as partes tem q ser verdadeira
print(saldo >= saque or saque <= limite)
#>>> True
#uma ou outra parte tem q ser verdadeira

print(not limite > saque)
#>>> True
#negação, se for falso vira verdadeiro

contatos_emergencia = []

print(not contatos_emergencia)
#>>> True

print(not "saque 100")
#>>> False
# Se a string não estiver vazia, o not vai retornar False
print(not "")
#>>> True
# Se a string estiver vazia, o not vai retornar True

