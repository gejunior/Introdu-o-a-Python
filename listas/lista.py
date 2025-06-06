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