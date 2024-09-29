# Problema B

# Bateria Anti-aérea

# Joãozinho, o conselheiro científico e militar dos Esbornianos, foi convocado para mais uma missão de alta
# importância. O exército dos Sneakys está utilizando um perigoso canhão de prótons, posicionado em um
# ponto estratégico no campo de batalha, que pode destruir completamente a unidade de controle de bateria
# anti-aérea móvel, uma estrutura circular crucial para a defesa do espaço aéreo dos Esbornianos.
# Se o canhão dos Sneakys estiver mirando exatamente no centro da unidade de controle, é impossível escapar
# da destruição. No entanto, graças à ajuda de Munarinho, amigo de Joãozinho, foi desenvolvido um sistema
# de scramble que desorienta o radar e a mira do canhão dos Sneakys. Com isso, a unidade de controle pode
# se mover para escapar do disparo, desde que o canhão não mire exatamente no centro da unidade.
# O objetivo é, dado a posição do canhão, o ângulo de disparo e a posição da unidade de defesa, determinar:
# 1. Se a unidade será atingida fatalmente (quando o canhão estiver mirando exatamente no centro).
# 2. Se a unidade não será atingida.
# 3. Quando possível escapar, calcular o menor deslocamento necessário para que a unidade de controle
# evite o disparo.
# Sua tarefa é ajudar Joãozinho a garantir a segurança da unidade de controle, verificando se ela será atingida
# ou não, e calculando o deslocamento mínimo, se possível.

# Entrada
# A entrada contém os seguintes valores:
# • xk, yk: Coordenadas do canhão.
# • ✓: Ângulo do canhão em relação ao eixo X, dado em graus.
# • xc, yc: Coordenadas do centro da unidade de controle circular.
# • r: Raio da unidade de controle circular.
# Saída

# Imprima:
# • "Atingido Fatalmente" se o canhão estiver mirando exatamente no centro da unidade de controle.
# • "Nao Atingido" se a unidade de controle não estiver na trajetória do projétil.
# • "Atingido" se a unidade estiver na trajetória do disparo, e também imprima a menor distância que o
# centro da unidade deve se mover para não ser atingido.
# Maratona de Programação InterFatecs 2024 - Problema B: Bateria Anti-aérea 5
# Restrições
# • 0  xk, yk, xc, yc  10000
# • 1  r  100
# • 0  ✓ < 360
# • Tolerância para comparação de ponto flutuante: 10

# Exemplo de Entrada 1
# 590.00 489.00 70.64 590.00 489.00 98.64
# Exemplo de Saída 1
# Atingido Fatalmente

# Exemplo de Entrada 2
# 981.00 285.00 238.54 1015.82 281.81 37.13
# Exemplo de Saída 2
# Atingido
# 5.76

# Exemplo de Entrada 3
# 131.00 206.00 162.88 763.00 484.00 7.74
# Exemplo de Saída 3
# Não Atingido


from math import pi, cos, sin, sqrt, atan2, degrees


# Função para converter graus em radianos
def graus_para_radianos(angulo_graus: float) -> float:
    return angulo_graus * pi / 180.0


# Função para calcular a distância perpendicular do ponto (xc, yc) à linha de disparo
def distancia_perpendicular(
        xk: float,
        yk: float,
        angulo_disparo: float,
        xc: float,
        yc: float
) -> float:

    # Coordenadas de um ponto na direção do disparo
    x2 = xk + cos(graus_para_radianos(angulo_disparo))
    y2 = yk + sin(graus_para_radianos(angulo_disparo))

    # Cálculo da distância perpendicular usando a fórmula da distância ponto-reta
    numerador = abs((y2 - yk) * xc - (x2 - xk) * yc + x2 * yk - y2 * xk)
    denominador = sqrt((y2 - yk) ** 2 + (x2 - xk) ** 2)
    return numerador / denominador


def verifica_impacto(
        xk: float,
        yk: float,
        angulo: float,
        xc: float,
        yc: float,
        r: float
) -> str:

    # Verifica se o canhão está exatamente no centro da unidade de controle
    if xk == xc and yk == yc:
        return "Atingido Fatalmente"

    # Ângulo de disparo fornecido em graus
    angulo_disparo = angulo % 360  # Mantém o ângulo no intervalo [0, 360)

    # Ângulo do vetor entre o canhão e o centro da unidade
    dx = xc - xk
    dy = yc - yk
    angulo_canhao_para_centro = degrees(atan2(dy, dx)) % 360

    # Verifica se o disparo está exatamente no centro (com tolerância para comparação)
    if abs(angulo_canhao_para_centro - angulo_disparo) < 1e-2:
        return "Atingido Fatalmente"

    # Calcula a distância perpendicular entre a trajetória e o centro da unidade
    dist_perp = distancia_perpendicular(xk, yk, angulo_disparo, xc, yc)

    # Verifica se a unidade será atingida
    if dist_perp > r:
        return "Nao Atingido"
    else:
        # A unidade está na trajetória do disparo
        # Calcula o deslocamento mínimo necessário para evitar o impacto
        deslocamento_minimo = r - dist_perp
        return f"Atingido\n{deslocamento_minimo:.2f}"


def main():

    # Leitura da entrada na ordem correta, sem mensagens extras
    xk, yk, angulo, xc, yc, r = map(float, input().split())

    # Verifica o impacto
    resultado = verifica_impacto(xk, yk, angulo, xc, yc, r)

    # Exibe o resultado
    print(resultado)


if __name__ == "__main__":
    main()
