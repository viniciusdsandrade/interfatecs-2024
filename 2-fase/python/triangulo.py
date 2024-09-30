# Problema K

# Figura triângulo

# Manuel é uma criança muito ativa, ele começa a escrever os números naturais em figuras triangulares conforme
#  o padrão da figura abaixo:
# E, a seguir, escreve as letras A, B, C, D, E, F, G, H e I nestes triângulos conforme a ilustração:
# E começa uma brincadeira de codificação de números, por exemplo, o número 5 é codificado como 1E, pois
# se encontra no triângulo 1 e sua posição no triângulo de letras é E! Ajude Manuel a codificar os números!

# Entrada
# Um número inteiro N (1  N  1.000.000).

# Saída
# O número codificado segundo o padrão descrito no texto.

# Exemplo de Entrada 1
# 5
# Exemplo de Saída 1
# 1E

# Exemplo de Entrada 2
# 16
# Exemplo de Saída 2
# 2G

# Exemplo de Entrada 3
# 27
# Exemplo de Saída 3
# 3I

from math import sqrt


def calcular_area_triangulo(a: float, b: float, c: float) -> float:
    sp = (a + b + c) / 2  # Calcula o semiperímetro
    area = sqrt(sp * (sp - a) * (sp - b) * (sp - c))  # Aplica a fórmula de Heron
    return area


def main():
    a, b, c = map(float, input().split())  # Entrada dos valores
    heron = calcular_area_triangulo(a, b, c)  # Chama a função para calcular a área
    print(f"{heron:.2f}")  # Exibe a área com 2 casas decimais


if __name__ == '__main__':
    main()
