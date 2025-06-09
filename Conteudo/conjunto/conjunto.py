#Set é uma coleção de elementos únicos e não ordenados.
# Conjuntos são definidos com chaves e não permitem elementos duplicados
# Exemplo de conjuntos
set([1, 2, 3, 4, 5, 1, 3]) # Resultado: {1, 2, 3, 4, 5}
#o comando set ñ garante a ordem dos elementos
# Conjuntos podem ser criados a partir de listas, tuplas ou strings
set(("palio", "gol", "celta", "palio"))  # Resultado: {'palio', 'gol', 'celta'}
# Conjuntos podem ser criados a partir de strings
set("python")  # Resultado: {'p', 'y', 't', 'h', 'o', 'n'}

linguagens = {"Python", "Java", "C++", "Python"} 
print(linguagens)

## conjuntos ñ suportam indexação, fatiamento ou repetição de elementos
#caso queira acessar um elemento específico, é necessário converter o conjunto em uma lista ou tupla
# Exemplo de conversão de conjunto para lista
numeros = {1, 2, 3, 4, 5}
numeros = list(numeros)
print(numeros[0])  # Resultado: 1

#Union de conjuntos
# A união de conjuntos combina todos os elementos de dois ou mais conjuntos, removendo duplicatas
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto1.union(conjunto2)  # Resultado: {1, 2, 3, 4, 5}

#intersection de conjuntos
# A interseção de conjuntos retorna os elementos comuns entre dois ou mais conjuntos
conjunto1.intersection(conjunto2)  # Resultado: {3}
# Diferença de conjuntos
# A diferença de conjuntos retorna os elementos que estão em um conjunto, mas não no outro
conjunto1.difference(conjunto2)  # Resultado: {1, 2}
conjunto2.difference(conjunto1)  # Resultado: {4, 5}
# Diferença simétrica de conjuntos
# A diferença simétrica de conjuntos retorna os elementos que estão em um conjunto ou no outro, mas não em ambos

conjunto1.symmetric_difference(conjunto2)  # Resultado: {1, 2, 4, 5}
#elementos que estão em um conjunto ou no outro, mas não em ambos

#Issubset
# Verifica se um conjunto é subconjunto de outro
conjunto1.issubset(conjunto2)  # Resultado: True

#superset
# Verifica se um conjunto é superconjunto de outro

#isdisjoint
# Verifica se dois conjuntos não têm elementos em comum
conjunto1.isdisjoint(conjunto2)  # Resultado: False (pois 3 é comum)

#add
# Adiciona um elemento a um conjunto
sorteio = {1, 23}

sorteio.add(2)
serteio.copy()
sorteio.discard(2)  # Remove o elemento 2, se existir
sorteio.pop() # Remove e retorna um elemento aleatório do conjunto
sorteio.remove(-1)  # Remove o elemento -1, se existir, caso contrário, gera um erro
# neste caso, o elemento ñ existe
len(numeros)  # Retorna o número de elementos no conjunto

#In
1 in numeros  # Verifica se o elemento 1 está no conjunto (Resultado: True)
# not in
2 not in numeros  # Verifica se o elemento 2 não está no conjunto (Resultado: False)
