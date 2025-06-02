#Interpolação de variáveis
curso = "Python"
# Old Style %
#s -> string
#d -> inteiro
#i -> inteiro
#c -> caractere
#f -> float
#exemplo 1
print("Curso: %s" % curso)
#exemplo 2 - metodo format
print("curso: {} e linguagem: {}".format("introdução a " + curso, curso))

print("Curso: {curso} e linguagem: {linguagem} vai ser em {local} ás {horario}"
      .format(curso = "introdução a Python", linguagem = curso, local = "SP", horario = "19:00"))

#exemplo 3 - formatar strings com f-strings
PI = 3.14159
print(f"Valor de PI: {PI:.2f}") # Formata PI com 2 casas decimais

print(f"Valor de PI: {PI:10.2f}")# Formata PI com 10 caracteres, incluindo 2 casas decimais