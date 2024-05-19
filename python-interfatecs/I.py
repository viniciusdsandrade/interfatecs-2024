# Gumercindo é um profissional de TI que está desenvolvendo uma ferramenta para simular um certo tipo
# de problema de transporte, onde determinados fluxos são canalizados entre locais específicos de uma organização.
# Basicamente temos um ponto de partida único, vários locais interligados de forma hierárquica e,
# dependendo dos valores iniciais e das características internas desses pontos intermediários, os valores vão
# sendo modificados. Vamos chamar esses locais ou pontos de “estações”, para melhorar a sua compreensão.
# Temos então uma estação inicial, de onde o conjunto de fluxos se origina, a partir de parâmetros especificados
# por Gumercindo em sua aplicação. Essa estação inicial vai produzir dois fluxos, uma para uma
# primeira estação vizinha, e outro para uma segunda estação também sua vizinha. Cada uma dessas estações
# vizinhas, com base em suas configurações internas e na intensidade do fluxo recebido, pode produzir até
# dois fluxos próprios, que vão para até duas estações em sua vizinhança imediata. E assim sucessivamente,
# até que estações terminais são atingidas, onde o processo como um todo se completa. Devido a detalhes
# técnicos totalmente fora de nosso interesse, cada estação recebe um fluxo de entrada de apenas uma estação
# anterior, e pode ter no máximo duas estações para onde encaminhar seus fluxos de saída. Trata-se de uma
# configuração em camadas regulares: a camada inicial tem apenas a estação inicial; a segunda camada é
# composta pelas duas estações adjacentes à inicial; a terceira camada terá até quatro estações, duas para cada
# uma da camada anterior, e assim sucessivamente. Uma característica adicional e, até certo ponto, simplificadora
# da simulação produzida por Gumercindo é que as estações vão sempre completando a capacidade
# das camadas iniciais e apenas a camada final poderá ter menos estações do que o seu limite. Mas nesse caso,
# as estações existentes nessa última camada estarão sempre a preenchendo da esquerda para a direita, sem
# ficarem “buracos” no arranjo. A figura 1 ilustra esse tipo de configuração em uma simulação com 8 estações
# dispostas em 4 camadas. Observe que a camada 1 tem uma estação (a tal “estação inicial”), a camada 2
# tem as 2 estações possíveis ali, a camada 3 possui as 4 estações que nela podem ser colocadas e a última
# camada possui apenas uma estação, e ela está conectada no seu limite esquerdo. Caso tivéssemos mais uma
# estação, ela seria conectada nessa camada final imediatamente ao lado da estação já existente ali. Em outras
# palavras, ao construir a estrutura de conexão entre as estações, o processo ocorre camada por camada e, para
# cada camada, o preenchimento é sempre da esquerda para a direita. Na figura 1 a informação contida em
# cada estação expressa o valor do fluxo que a estação recebeu da camada anterior. No caso da estação inicial
# esse valor corresponde ao parâmetro de inicialização utilizado por Gumercindo naquela simulação. Assim,
# por exemplo, a figura mostra que a estação inicial recebeu um fluxo de valor 11 no início do processo e as
# duas estações da camada seguinte receberam, respectivamente, fluxos de valores 7 e 3. Em outras palavras,
# o dado contido em cada estação indica o fluxo recebido, conforme verificado na condução do experimento.
# Sempre que uma simulação ocorre, o programa de Gumercindo gera uma sequência contendo os valores que
# cada estação recebeu. Assim, por exemplo, para o caso da figura 1, o programa emitiria a sequência 11, 7,
# 3, 19, 13, 7, 17 e 5, o que é intuitivo, pois o primeiro valor é o da estação inicial, o segundo valor é o da
# primeira estação da segunda camada (aquela à esquerda na figura), o terceiro valor corresponde à segunda
# estação dessa segunda camada (aquela à direita na figura) e assim por diante. Após uma grande quantidade
# de simulações, Gumercindo percebeu que uma pequena parte delas produzia um resultado final onde, para
# qualquer estação, em qualquer camada, o fluxo recebido nunca era maior que o fluxo que ela encaminhava
# para a camada seguinte, como mostra a figura 2. Perceba que à medida que avançamos pelas camadas a
# partir da origem, o valor do fluxo recebido por uma estação nunca é menor do que o fluxo que a sua estação
# antecessora na camada anterior recebeu. Gumercindo chamou esse padrão de “Configuração de tipo 1”.

# A grande maioria das simulações produziu arranjos mais parecidos com o da figura 1, onde os valores
# recebidos pelas estações não seguiram nenhum dos padrões anteriores. Esse caso mais comum recebeu
# o nome de “Configuração de tipo 0”. Cansado de analisar seus resultados manualmente e pretendendo
# trabalhar com quantidades maiores de camadas e estações, Gumercindo veio pedir a você, seu estagiário,
# para construir um programa capaz de analisar uma sequência produzida pelo simulador e indicar se
# trata-se de um arranjo do tipo 0 ou do tipo 1 ou do tipo 2. Caso o arranjo possa ser classificado tanto como
# do tipo 1 como do tipo 2, ele deixa de ser interessante para o nosso herói, e seu programa deve classificá-lo
# como do tipo 0. Capriche aí no programinha, pois com ele você liberará seu chefe desse enfadonho trabalho
# analítico que ele chama, carinhosamente, de “encheção de linguiça” (sic).

# Entrada
# A entrada se inicia com um inteiro N (0 < N  1000) que indica a quantidade de estações existentes na
# simulação. Seguem-se N linhas, cada uma contendo um valor P (−100  P  300), indicando o valor
# recebido por aquela estação. A sequência dos valores corresponde à sequência produzida pelo programa
# simulador de Gumercindo ao final do processamento, agora dispostos na forma de um valor por linha, para
# simplificar o seu trabalho.

# Saída
# Imprima um inteiro entre 0 e 2 indicando o tipo de configuração correspondente ao arranjo lido da entrada,
# conforme descrito anteriormente.

# Exemplo de Entrada1
# 8
# 11
# 7
# 3
# 19
# 13
# 7
# 17
# 5
# Exemplo de Saída1  0


# Exemplo de Entrada2
# 8
# 3
# 5
# 7
# 11
# 13
# 7
# 17
# 19
# Exemplo de Saída2 1

# Exemplo de Entrada3
# 8
# 19
# 13
# 17
# 7
# 11
# 3
# 7
# 5
# Exemplo de Saída3 2
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


entrada = int(input())
root = Node(int(input()))

for i in range(1, entrada):
    node = Node(int(input()))
    current = root
    while True:
        if node.data < current.data:
            if current.left is None:
                current.left = node
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            else:
                current = current.right


def check_tree(node):
    if node is None:
        return 0, True, True

    left_sum, is_left_type1, is_left_type2 = check_tree(node.left) if node.left else (0, True, True)
    right_sum, is_right_type1, is_right_type2 = check_tree(node.right) if node.right else (0, True, True)

    is_type1 = is_left_type1 and is_right_type1 and node.data >= left_sum + right_sum
    is_type2 = is_left_type2 and is_right_type2 and node.data <= left_sum + right_sum

    if not is_type1 and not is_type2:
        return 0, False, False

    return node.data, is_type1, is_type2


_, is_type1, is_type2 = check_tree(root)
if is_type1 and not is_type2:
    print("1")  # Configuration of type 1
elif is_type2 and not is_type1:
    print("2")  # Configuration of type 2
else:
    print("0")  # Configuration of type 0
