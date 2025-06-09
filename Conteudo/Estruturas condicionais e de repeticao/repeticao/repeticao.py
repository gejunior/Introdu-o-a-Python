print("Programa 1: for")
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print("\nPrograma 2: while")

a = int(input("Informe um numero inteiro: "))
while a > 0:
    a-= 1
    print(a, end=" ") #para não pular linha
print("\nFim do programa")

print("Programa 3: for com range")
#Range
for numero in range(0, 11):
    print(numero, end=" ") #para não pular linha

# list(range(4)) # [0, 1, 2, 3]

print()#pula uma linha

#exivindo a tabuada
for numero in range(0, 51, 5):
    print(numero, end=" ")
