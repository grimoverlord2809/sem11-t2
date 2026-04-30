# Lê idades até 0 (flag) e exibe: quantidade, média, menor e maior idade


def analisar_idades():
    quantidade = 0
    soma = 0
    menor = None
    maior = None

    idade = int(input().strip())    # Lê a primeira idade
    while idade != 0:               # 0 é a flag de encerramento
        quantidade += 1
        soma += idade

        if menor is None or idade < menor:   # Inicializa ou atualiza o menor
            menor = idade
        if maior is None or idade > maior:   # Inicializa ou atualiza o maior
            maior = idade

        idade = int(input().strip())

    media = soma / quantidade if quantidade > 0 else 0.0
    return quantidade, media, menor, maior


def main():
    quantidade, media, menor, maior = analisar_idades()
    print(quantidade)
    print(f"{media:.2f}")
    print(menor)
    print(maior)


if __name__ == '__main__':
    main()
