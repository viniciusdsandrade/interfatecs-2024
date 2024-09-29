# Problema G
# Estrados

# Meu jovem, você acaba de receber grande oportunidade na sua vida. O Sr. Temístocles Leopoldo, velho
# amigo do seu pai, passou a administrar a empresa Bons Sonhos fabricante de estrados de madeira de alta
# qualidade para camas luxuosas.

# O estrado é a estrutura que sustenta o colchão e é essencial para garantir uma base estável e uniforme para
# alguém dormir. Eles podem ser de madeira, metal ou plástico. A Bons Sonhos fabrica estrados de madeira,
# montados com ripas longitudinais pregadas em caibros transversais grossos e resistentes, como mostrado na
# figura.

# O estrado sempre usa 5 caibros transversais e o que varia são 3 parâmetros: a largura da madeira da ripa; a
# quantidade de ripas; o espaçamento entre as ripas.

# Há estrados de várias larguras: criança, solteiro, casal, king size, etc.
# Embora a empresa seja lucrativa, o Sr. Temístocles tem detectado diversas falhas administrativas, que se
# forem sanadas podem ajudar a empresa a lucrar mais ainda.
# Uma das falhas mais severas está na área de produção onde ocorrem dois tipos de problemas que levam ao
# retrabalho dos estrados produzidos, diminuindo a eficiência e a lucratividade.
# Alguns estrados são especificados com excesso de ripas, com gasto excessivo de material.
#
# Outros estrados
# são especificados com ripas a menos, fazendo com que o espaço entre elas seja grande demais, o que
# causa desconforto ao dorminhoco, insatisfação e pedidos de reembolso. Estudos técnicos mostram que o
# espaçamento entre duas ripas vizinhas deve estar entre 10 cm e 20 cm.

# Se o espaçamento for menor que 10 cm há excesso de ripas e o projeto está superdimensionado. Se esse
# espaçamento for maior que 20 cm há poucas ripas e o projeto está subdimensionado.
# Caro programador, dito isto, chega sua vez de agir. Por conhecê-lo desde pequeno e saber de seu potencial,
# o Sr. Temístocles, o contrata para escrever um programa que verifique todas as especificações de projeto
# antes de enviá-los para a produção.

# Seu trabalho é escrever um programa que leia a largura total do estrado, a quantidade de ripas e a largura da
# ripa. Em seguida calcule o espaçamento entre ripas, de modo que a largura total não seja ultrapassada e imprima
# uma de três possíveis situações: projeto ok, projeto superdimensionado ou projeto subdimensionado.

# Entrada
# A primeira linha da entrada contém um número inteiro Q (0 < Q  1000) que é a quantidade de projetos a
# serem analisados. Em seguida estão Q linhas de dados de estrados contendo 3 números inteiros separados
# por um espaço em branco, a saber:
# • Largura total do estrado LT (60 ≤ LT ≤ 210)
# • Quantidade de ripas QR (4 ≤ QR ≤ 15)
# • Largura de uma ripa LR (3 ≤ LR ≤ 8)
# As medidas de largura são expressas em centímetros.

# Saída
# Para cada linha de dados de estrados o programa deve imprimir o seguinte:
# • Se o espaçamento entre ripas for menor que 10 cm imprima projeto superdimensionado
# • Se o espaçamento entre ripas for maior que 20 cm imprima projeto subdimensionado
# • Se o espaçamento estiver entre 10 e 20 cm, incluindo estes valores imprima projeto ok

# Exemplo de Entrada 1
# 12
# 88 8 8
# 88 8 5
# 88 6 4
# 88 6 3
# 96 4 3
# 96 7 3
# 96 10 4
# 120 8 3
# 120 10 4
# 200 8 3
# 200 12 4
# 200 14 5

# Exemplo de Saída 1
# projeto superdimensionado
# projeto superdimensionado
# projeto ok
# projeto ok
# projeto subdimensionado
# projeto ok
# projeto superdimensionado
# projeto ok
# projeto superdimensionado
# projeto subdimensionado
# projeto ok
# projeto ok

def verifica_projeto(lt_estrado: int, qtd_ripas: int, largura_ripas: int) -> str:

    # Calcula a distância entre as ripas
    res = (lt_estrado - (qtd_ripas * largura_ripas)) / (qtd_ripas - 1)

    # Avalia o resultado e retorna a classificação do projeto
    if res < 10:
        return "projeto superdimensionado"
    elif res <= 20:
        return "projeto ok"
    else:
        return "projeto subdimensionado"


def main():

    # Leitura do número de testes
    n = int(input())

    # Processa cada teste
    for _ in range(n):
        lt_estrado, qtd_ripas, largura_ripas = [int(k) for k in input().split()]
        resultado = verifica_projeto(lt_estrado, qtd_ripas, largura_ripas)
        print(resultado)


if __name__ == "__main__":
    main()
