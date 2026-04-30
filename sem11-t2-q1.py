# Lê inteiros até 0 (flag) e exibe a soma de todos (excluindo o zero)


def somar_ate_zero():
    soma = 0

    n = int(input().strip())     # Lê o primeiro número
    while n != 0:                # Continua enquanto não for 0
        soma += n
        n = int(input().strip())

    return soma


def main():
    print(somar_ate_zero())


if __name__ == '__main__':
    main()
