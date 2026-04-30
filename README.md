# Semana 11 — Turma T2 | Programação Estruturada

> **Prof.:** Ritomar Torquato | **IFPI** | **Período:** 2026-1

Exercícios de **repetição com flag de parada e menus interativos**. Todos os arquivos seguem a estrutura:

```python
def funcao_logica(...):
    # lógica aqui

def main():
    # chama a função e imprime resultados

if __name__ == '__main__':
    main()
```

---

## Questão 1 — `sem11-t2-q1.py`

### Enunciado
Leia um conjunto de números inteiros e exiba a soma dos mesmos. A condição de saída é a leitura do valor 0 (flag).

### Solução

```python
def somar_ate_zero():
    soma = 0
    n = int(input().strip())
    while n != 0:
        soma += n
        n = int(input().strip())
    return soma

def main():
    print(somar_ate_zero())

if __name__ == '__main__':
    main()
```

### Como foi resolvida

| Elemento | Descrição |
|---|---|
| `n = int(input())` antes do `while` | Lê o primeiro valor antes de verificar a condição |
| `while n != 0` | Para quando a flag 0 for digitada |
| `soma += n` | Acumula a soma de todos os valores lidos |
| Leitura no final do laço | Prepara o próximo valor para a próxima verificação |

**Exemplo:** entrada `3 5 2 0` → saída `10`

---

## Questão 2 — `sem11-t2-q2.py`

### Enunciado
Para um número indeterminado de pessoas, leia a idade de cada uma (0 encerra). Calcule e exiba: número de pessoas, média, menor e maior idade.

### Solução

```python
def analisar_idades():
    quantidade = 0
    soma = 0
    menor = None
    maior = None
    idade = int(input().strip())
    while idade != 0:
        quantidade += 1
        soma += idade
        if menor is None or idade < menor:
            menor = idade
        if maior is None or idade > maior:
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
```

### Como foi resolvida

| Elemento | Descrição |
|---|---|
| `menor = None` / `maior = None` | Inicialização segura: evita comparar com valor arbitrário |
| `if menor is None or idade < menor` | Inicializa no primeiro valor, atualiza nos demais |
| `soma / quantidade` | Média calculada ao final, após sair do laço |

**Exemplo:** idades `20 30 15 25 0` → 4 pessoas, média `22.50`, menor `15`, maior `30`

---

## Questão 3 — `sem11-t2-q3.py`

### Enunciado
Exiba um menu de opções e responda com a mensagem correspondente. Continue enquanto a opção for diferente de 0.

### Solução

```python
def executar_menu():
    while True:
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
            break
        else:
            print("Opção inválida.")

def main():
    executar_menu()

if __name__ == '__main__':
    main()
```

### Como foi resolvida

| Elemento | Descrição |
|---|---|
| `while True` + `break` | Simula do-while: o menu sempre é exibido ao menos uma vez |
| Menu impresso a cada iteração | Garante que o usuário veja as opções antes de cada escolha |
| Resposta com número + texto | Formato `"1 - Olá. Como vai?"` conforme saída esperada |
| `else: print("Opção inválida.")` | Trata qualquer opção fora do menu |

**Exemplo:** entrada `1 2 3 4 0` → exibe saudação, bronca, parabéns, inválida e encerra.

---

## Questão 4 — `sem11-t2-q4.py`

### Enunciado
Cardápio de lanchonete. Leia códigos de produtos e acumule o total. Ao digitar `X`, exiba o total a pagar. Exiba o cardápio antes de cada leitura.

### Solução

```python
def exibir_cardapio():
    print("CÓDIGO  PRODUTO         PREÇO (R$)")
    print("H       Hamburger       5,50")
    print("C       Cheeseburger    6,80")
    print("M       Misto Quente    4,50")
    print("A       Americano       7,00")
    print("Q       Queijo Prato    4,00")
    print("X       PARA TOTAL DA CONTA")

def calcular_conta():
    precos = {'H': 5.50, 'C': 6.80, 'M': 4.50, 'A': 7.00, 'Q': 4.00}
    total = 0.0
    while True:
        exibir_cardapio()
        codigo = input().strip().upper()[0]
        if codigo == 'X':
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
```

### Como foi resolvida

| Elemento | Descrição |
|---|---|
| `exibir_cardapio()` antes de cada `input` | Cardápio aparece a cada iteração do laço |
| `.upper()[0]` | Aceita minúsculas e usa só o 1º caractere digitado |
| `precos` (dicionário) | Mapeamento direto código → preço |
| `'X'` como flag | Encerra o laço e exibe o total |

**Exemplos:**

| Entrada | Total |
|---|---|
| M M X | 9.00 |
| M X | 4.50 |

---

## Questão 5 — `sem11-t2-q5.py`

### Enunciado
Leia a nota do aluno entre 0 e 10. Mostre "Nota inválida." se fora do intervalo e continue pedindo. Após nota válida, exiba o conceito.

### Solução

```python
def ler_nota_valida():
    while True:
        nota = float(input().strip())
        if 0 <= nota <= 10:
            return nota
        print("Nota inválida.")

def obter_conceito(nota):
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
```

### Como foi resolvida

| Elemento | Descrição |
|---|---|
| `while True` em `ler_nota_valida` | Repete até receber uma nota válida |
| `0 <= nota <= 10` | Encadeamento de comparação do Python |
| `print("Nota inválida.")` antes de continuar | Avisa o usuário e reinicia a leitura |
| `obter_conceito` separado | Isola a lógica de classificação da leitura |

**Tabela de conceitos:**

| Conceito | Nota mínima |
|---|---|
| A | >= 8,5 |
| B | >= 7,0 |
| C | >= 5,0 |
| D | >= 4,0 |
| E | >= 0 |
# sem11-t2
