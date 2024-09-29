from math import sqrt


def calcular_area_triangulo(a, b, c):
    # Calcula o semiperímetro
    sp = (a + b + c) / 2
    # Aplica a fórmula de Heron
    area = sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    return area


# Entrada dos valores
a, b, c = map(float, input().split())

# Chama a função para calcular a área
heron = calcular_area_triangulo(a, b, c)

# Exibe a área com 2 casas decimais
print(f"{heron:.2f}")
