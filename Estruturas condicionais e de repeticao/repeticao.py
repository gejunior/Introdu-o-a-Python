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