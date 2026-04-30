# Lê a nota do aluno (0-10), valida e exibe o conceito correspondente


def ler_nota_valida():
    while True:
        nota = float(input().strip())
        if 0 <= nota <= 10:      # Nota válida: entre 0 e 10 inclusive
            return nota
        print("Nota inválida.")  # Informa e repete a leitura


def obter_conceito(nota):
    # Tabela de conceitos em ordem decrescente de nota
    if nota >= 8.5:
        return 'A'
    elif nota >= 7.0:
        return 'B'
    elif nota >= 5.0:
        return 'C'
    elif nota >= 4.0:
        return 'D'
    else:
        return 'E'


def main():
    nota = ler_nota_valida()
    print(obter_conceito(nota))


if __name__ == '__main__':
    main()
