# Lista de exercícios para diagnóstico.


def kilometros_para_milhas(km):
    """Uma milha equivale a 1609 metros. Desenvolva uma função que receba um valor \
    em km e retorne o valor em milhas.

    Argumentos:
        km (float): uma quantidade de kilometros

    Retorna:
        (float): uma quantidade em milhas, com 6 casas decimais.
    """
    milha = 1.609
    return round(km/milha,6)

def multiplicacao_simples(n):
    """Multiplique o número por 8 se ele for par ou por 9 se for ímpar.

    Argumento:
        n (inteiro): um número inteiro

    Retorna:
        inteiro: um número, conforme o enunciado.
    """
    par = n*8
    impar = n*9
    if (n%2) == 0:
        return par
    else:
        return impar

def trimestre(mes):
    """Dado um mês como um inteiro de 1 a 12, retorna a qual trimestre do ano ele \
        pertence como um número inteiro. 
    Por exemplo: mês 2 (fevereiro), faz parte do primeiro trimestre; \
    o mês 6 (junho), faz parte do segundo trimestre; \
    e o mês 11 (novembro), faz parte do quarto trimestre.

    Argumento
        mes (inteiro): o mês

    Returna:
        inteiro: o quadrimestre (quarto) a que o mês pertence.
    """
    if mes <=3:
        return 1
    elif mes <=6:
        return 2
    elif mes <=9:
        return 3
    else:
        return 4

def camel_casing(s):
    """ Camel Casing é uma forma de escrever nomes de identificadores, \
    (como varíaveis e funções) usando letras maiúsculas para separar as palavras. \
    A palavra "camel" em inglês significa camelo (lembre-se das córcovas do camelo e tudo faz sentido).\
    Desenvolva uma solução que quebre o "camel casing", usando espaçoes entre as palavras.\

    Exemplo
    "camelCasing"  =>  "camel Casing"
    "mediaFinalAposRecuperacao"  =>  "media Final Apos Recuperacao"
    "soma"   =>  "soma"
    "" =>  ""

    Argumento:
        s (string): a palavra original que será processada.

    Returna:
        string: um conjunto de palavras, que foram separadas segundo o critério do "camel casing".
    """
    string = ""
    for c in s:
        if c.isupper():
            string += " "
        string += c
    return string

def crescimento_populacional_2(populacao_atual, percentual, aumento, populacao_final):
    """Determine quantos anos a população da cidade levará para ultrapassar a população final. \
        os valores de população atual, percentual de aumento anual, aumento por mudança \
            e da população final são informados como parâmetros da função.

    Aqui vai um exemplo: suponha que a população é p0 = 1000 no início do ano. \
    A população aumenta regularmente em 2% ao ano e, além disso, 50 novos \
    habitantes por ano vêm morar na cidade. \
    Quantos anos a cidade precisa para ver sua população maior ou igual a p = 1200 habitantes?

    No final do primeiro ano, haverá:
    1000 + 1000 * 0,02 + 50 => 1070 habitantes

    No final do 2º ano, haverá:
    1070 + 1070 * 0,02 + 50 => 1141 habitantes (o número de habitantes é um inteiro)

    No final do 3º ano, haverá:
    1141 + 1141 * 0,02 + 50 => 1213

    Serão necessários 3 anos inteiros.

    Observação:
    Não se esqueça de converter o parâmetro de porcentagem em porcentagem \
    no corpo de sua função: se o parâmetro de porcentagem for 2, você deve \
    convertê-lo para 0,02.

    Argumentos:
        populacao_atual (int): a população inicial, no ano zero.
        percentual (float): o percentual de aumento da população a cada ano.
        aumento (int): a quantidade de pessoas que chegam na cidade de fora.
        populacao_final (int): a população que se quer chegar.

    Retorna:
        int: a quantidade de anos até se alcançar (ou passar) a população final.
    """
    count = 0
    percentual_novo = percentual / 100

    while populacao_atual < populacao_final:
        populacao_atual += populacao_atual * percentual_novo + aumento
        count += 1
    return count

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = f"\033[31m{'Falhou'}"
    else:
        prefixo = f"\033[32m{'Passou'}"
        acertos += 1
    print(f"{prefixo} Esperado: {esperado} \tObtido: {obtido}\033[1;m")


def main():
    print("Kilometros para milhas: ")
    test(kilometros_para_milhas(1), 0.621504)
    test(kilometros_para_milhas(2), 1.243008)
    test(kilometros_para_milhas(3), 1.864512)
    test(kilometros_para_milhas(4), 2.486016)
    test(kilometros_para_milhas(5), 3.10752)

    print("Multiplicação simples:")
    test(multiplicacao_simples(1), 9)
    test(multiplicacao_simples(2), 16)
    test(multiplicacao_simples(4), 32)
    test(multiplicacao_simples(5), 45)
    test(multiplicacao_simples(8), 64)

    print("Trimestre: ")
    test(trimestre(1), 1)
    test(trimestre(2), 1)
    test(trimestre(3), 1)
    test(trimestre(4), 2)
    test(trimestre(5), 2)
    test(trimestre(6), 2)
    test(trimestre(7), 3)
    test(trimestre(8), 3)
    test(trimestre(9), 3)
    test(trimestre(10), 4)
    test(trimestre(11), 4)
    test(trimestre(12), 4)

    print("Camel Casing:")
    test(camel_casing("helloWorld"), "hello World")
    test(camel_casing("camelCase"), "camel Case")
    test(camel_casing("breakCamelCase"), "break Camel Case")
    test(camel_casing("quantidadeDeDiasPerdidosPorFumar"), "quantidade De Dias Perdidos Por Fumar")
    test(camel_casing("mediaFinalAposRecuperacao"), "media Final Apos Recuperacao")

    print("Crescimento Populacional 2:")
    test(crescimento_populacional_2(1000, 2, 50, 1200), 3)
    test(crescimento_populacional_2(1500, 5, 100, 5000), 15)
    test(crescimento_populacional_2(1500000, 2.5, 10000, 2000000), 10)


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
