# Problema C

# Coroinha Munarinho

# Munarinho decidiu ser coroinha e para comemorar a decisão tentará reproduzir uma tentativa feita no passado
# por um padre que fisicamente mantinha com ele profunda semelhança física. Ele quebrou o porquinho,
# investiu todas as suas economias em balões e cilindros de gás hélio e está se preparando para voar preso
# apenas a balões, partindo de Sorocaba e indo até Araçoiaba da Serra, onde pousará na casa de um colega
# para uma festa de comida de caminhão (truck food). Procurando evitar acidentes, Munarinho estudou bem o
# uso do GPS e o clima da região. No entanto, ele entende que voar de balão é arriscado, pois não há controle
# da direção para a qual se vai. Desta forma, ele está escrevendo um software para prever
# possíveis locais de pouso dado o padrão de vento da região.

# Neste programa, a região pode ser vista como uma matriz bidimensional onde cada célula é um possível
# local de pouso. Munarinho sairá de uma célula e, dados golpes de vento, será levado a outras células. Para
# simplificar, Munarinho está assumindo que um golpe de vento o leva de uma célula para outra imediatamente
# acima, abaixo, à esquerda ou à direita.

# Ajude Munarinho a escrever este programa. Dado o tamanho da matriz da região, a célula onde terá a
# comida de caminhão e o número/direção de golpes de vento, determine a célula da qual Munarinho teria que
# partir para chegar inteiro à festa.

# Entrada

# A entrada é composta por um caso de teste. A primeira linha contém cinco números inteiros separados por
# um espaço em branco L C N CL CC representando, respectivamente, o número de linhas (1  L  100)
# e de colunas (1  C  100) da matriz da região, o número N de golpes de vento (1  N  1000), bem
# como a linha (1  CL  L) e coluna (1  CC  C) do local onde será a festa de comida de caminhão.
# A segunda linha contém N caracteres D (‘C’, ‘D’, ‘B’, ‘E’), representativos da direção do golpe de vento
# (Cima, Direita, Baixo, Esquerda).

# Saída

# A saída deve conter dois números inteiros X Y indicativos da linha e coluna da célula de onde Munarinho
# deverá partir para chegar à festa de comida de caminhão. Caso esta célula não exista na matriz,
# imprima −1 −1.

# Exemplo de Entrada 1
# 5 5 8 3 3
# CDBEEDDC

# Exemplo de Saída 1
# 4 2


# Exemplo de Entrada 2
# 10 10 5 0 0
# DDDDD

# Exemplo de Saída 2
# −1 -1

def calcula_partida(
        linhas: int,
        colunas: int,
        golpes: str,
        linha_festa: int,
        coluna_festa: int
) -> tuple[int, int]:

    # Mapeia o golpe de vento e suas operações inversas
    direcoes = {
        'C': (1, 0),   # Cima → Desloca 1 linha para baixo
        'B': (-1, 0),  # Baixo → Desloca 1 linha para cima
        'D': (0, -1),  # Direita → Desloca 1 coluna para a esquerda
        'E': (0, 1)    # Esquerda → Desloca 1 coluna para a direita
    }

    # Processa os golpes de vento na ordem inversa
    for golpe in reversed(golpes):
        delta_linha, delta_coluna = direcoes[golpe]
        linha_festa += delta_linha
        coluna_festa += delta_coluna

    # Verifica se a posição calculada está dentro dos limites da matriz
    if not (1 <= linha_festa <= linhas and 1 <= coluna_festa <= colunas):
        return -1, -1

    return linha_festa, coluna_festa


def main():

    # Leitura da entrada
    linhas, colunas, _, linha_festa, coluna_festa = map(int, input().split())
    golpes_de_vento = input().strip()

    # Chamada da função para calcular o ponto de partida
    linha_inicial, coluna_inicial = calcula_partida(linhas, colunas, golpes_de_vento, linha_festa, coluna_festa)

    # Impressão do resultado
    print(linha_inicial, coluna_inicial)


if __name__ == '__main__':
    main()
