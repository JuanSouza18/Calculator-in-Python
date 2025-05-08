def adicao():
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    return numero1 + numero2

def subtracao():
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    return numero1 - numero2

def multiplicacao():
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    return numero1 * numero2

def divisao():
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    if numero2 == 0:
        print("Erro: Divisão por zero não é permitida!")
        return None
    return numero1 / numero2

def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "0":
            print("Encerrando calculadora...")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção Inválida! Tente Novamente.")
            continue

        if opcao == "1":
            resultado = adicao()
            print(f"O resultado da adição é: {resultado}")

        elif opcao == "2":
            resultado = subtracao()
            print(f"O resultado da subtração é: {resultado}")

        elif opcao == "3":
            resultado = multiplicacao()
            print(f"O resultado da multiplicação é: {resultado}")

        elif opcao == "4":
            resultado = divisao()
            if resultado is not None:
                print(f"O resultado da divisão é: {resultado}")


calculadora()
