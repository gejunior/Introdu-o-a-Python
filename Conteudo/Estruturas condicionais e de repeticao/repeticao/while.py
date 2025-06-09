opcao = -1

def menu():
    print("Opcoes")
    print("[1] opcao 1")
    print("[2] opcao 2")
    print("[3] opcao 3")
    print("[0] Sair")


while opcao != 0:
    menu()
    opcao = int(input("\nInforme uma opcao (0 para sair): "))

    if opcao == 1:
        print("Opcao 1 selecionada")
    elif opcao == 2:
        print("Opcao 2 selecionada")
    elif opcao == 3:
        print("Opcao 3 selecionada")
    elif opcao == 0:
        print("Saindo do programa")
    else:
        print("Opcao invalida, tente novamente")

contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue # Pula a iteração quando o contador é 3
    print(f"Contador: {contador}")
