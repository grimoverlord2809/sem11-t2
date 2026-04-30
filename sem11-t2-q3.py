# Menu interativo com opções de saudação, bronca, felicitação e saída
# Usa repetição com teste no final (do-while): sempre executa ao menos uma vez


def executar_menu():
    while True:                              # Loop infinito: sai pelo break
        print("OPÇÕES:")
        print("1 - SAUDAÇÃO")
        print("2 - BRONCA")
        print("3 - FELICITAÇÃO")
        print("0 - FIM")

        opcao = int(input().strip())

        if opcao == 1:
            print("1 - Olá. Como vai?")
        elif opcao == 2:
            print("2 - Vamos estudar mais.")
        elif opcao == 3:
            print("3 - Meus Parabéns!")
        elif opcao == 0:
            print("0 - Fim de serviço.")
            break                            # Encerra o laço quando opção for 0
        else:
            print("Opção inválida.")


def main():
    executar_menu()


if __name__ == '__main__':
    main()
