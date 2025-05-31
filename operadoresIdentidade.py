curso = "Itroduçao a Python"
nome_curso = curso

print(curso is nome_curso)
#ocupam a msm posição/região na memória

print(curso is not nome_curso)
# Não ocupam a msm posição/região na memória
print(curso is "Python")
print(curso is not "Python")

print(curso is str())
# Verifica se o objeto é do tipo str
print(curso is not str())