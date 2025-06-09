frutas= ["laranja", "maçã", "banana", "uva", "abacaxi"]
# frutas = []
letras = list("python")
# numero = lista(range(10))
carro = ["volkswagen", "F8", 420000, "SP", True, 2023]

#acesso
# frutas[0]  # Acessa o primeiro elemento da lista
# print(frutas[0]) :# Imprime o primeiro elemento da lista
# frutas[-1]  # Acessa o último elemento da lista

#matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz[0][0]  # Acessa o primeiro elemento da primeira lista
# print(matriz[0][0])  # Imprime o primeiro elemento da primeira lista
# print(matriz[0]) #imprime a primeira linha da matriz

#Fatiamento
lista = ["p", "y", "t", "h", "o", "n"]
# print(lista[2:]) # Fatiamento da lista a partir do índice 2
# print(lista[:3])  # Fatiamento da lista até o índice 3
# print(lista[0:3:2]) # Fatiamento da lista do índice 0 ao 3, pulando de 2 em 2
# print(lista[::]) # Fatiamento da lista completa
# print(lista[::-1]) # Fatiamento da lista invertida

#função enumerate
carros = ["gol", "celta", "uno", "palio", "fiorino"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros): #enumerate retorna o índice e o valor do elemento
    print(f"{indice} - {carro}") #Imprime o índice e o valor do elemento

numeros = [1, 2, 3, 4, 5]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)  # Adiciona o número par à lista pares
        print("Números pares:", pares)  # Imprime a lista de números pares

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]  # Compreensão de lista para filtrar números pares
# Adiciona o número par à lista pares
print("Números pares:", pares)  # Imprime a lista de números pares

print("printando lista antes de limpar", lista)
lista.clear()  # Limpa a lista, removendo todos os elementos
l2 = lista.copy()  # Cria uma cópia da lista
print("printando depois de limpar", lista) 

# print(id(lista))  # Imprime o ID da lista (endereço de memória)
# print(id(frutas))  # Imprime o ID da lista frutas (endereço de memória)

# l2[0] = 2
print(l2)

# use extend para adicionar elementos de outra lista
l2.extend([1, 2, 3])  # Adiciona os elementos da lista [1, 2, 3] à lista l2
print(l2)  # Imprime a lista l2 após adicionar os elementos 

linguagens = ["python", "java", "c++", "javascript"]

linguagens.index("python")  # Retorna o índice do elemento "python" na lista linguagens
print(linguagens.index("python"))  # Imprime o índice/posição do elemento "python" na lista linguagens
linguagens.append("c#")  # Adiciona o elemento "c#" ao final da lista linguagens
print(linguagens)  # Imprime a lista linguagens após adicionar o elemento "c#"

linguagens.pop()  # Remove e retorna o último elemento da lista linguagens
linguagens.pop(0)  # Remove e retorna o elemento no índice 0 da lista linguagens
linguagens.remove("java")  # Remove o elemento "java" da lista linguagens
linguagens.reverse()  # Inverte a ordem dos elementos na lista linguagens
linguagens.sort()  # Ordena os elementos da lista linguagens em ordem crescente
len(linguagens)  # Retorna o número de elementos(tamanho) na lista linguagens
sorted(linguagens)  # Retorna uma nova lista ordenada, sem modificar a lista original
