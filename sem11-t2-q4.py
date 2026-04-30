# Cardápio de lanchonete: exibe menu, lê códigos até 'X' e exibe o total


def exibir_cardapio():
    # Exibe o cardápio antes de cada leitura de código
    print("CÓDIGO  PRODUTO         PREÇO (R$)")
    print("H       Hamburger       5,50")
    print("C       Cheeseburger    6,80")
    print("M       Misto Quente    4,50")
    print("A       Americano       7,00")
    print("Q       Queijo Prato    4,00")
    print("X       PARA TOTAL DA CONTA")


def calcular_conta():
    # Tabela de preços indexada pelo código do produto
    precos = {
        'H': 5.50,   # Hamburger
        'C': 6.80,   # Cheeseburger
        'M': 4.50,   # Misto Quente
        'A': 7.00,   # Americano
        'Q': 4.00,   # Queijo Prato
    }

    total = 0.0

    while True:
        exibir_cardapio()
        # upper()[0] garante maiúscula e usa apenas o primeiro caractere digitado
        codigo = input().strip().upper()[0]

        if codigo == 'X':          # 'X' encerra o pedido
            break
        elif codigo in precos:
            total += precos[codigo]
        else:
            print("Opção inválida.")

    return total


def main():
    total = calcular_conta()
    print(f"{total:.2f}")


if __name__ == '__main__':
    main()
