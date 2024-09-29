# Problema K
# Figura triângulo
# Arquivo fonte: figuratriangulo.{ c | cpp | java | py }
# Autor: Prof. Dr. Reinaldo Arakaki (Fatec São José dos Campos)
# Manuel é uma criança muito ativa, ele começa a escrever os números naturais em figuras triangulares de
# acordo com o padrão da figura abaixo:
# E, a seguir, escreve as letras A, B, C, D, E, F, G, H e I nestes triângulos conforme a ilustração:
# E começa uma brincadeira de codificação de números, por exemplo o número 5 é codificado como 1E, pois
# se encontra no triângulo 1 e sua posição no triângulo de letras é E! Ajude Manuel a codificar os números!
# Entrada
# Um número inteiro N (1  N  1.000.000).
# Saída
# O número codificado segundo o padrão descrito no texto.
# Exemplo de Entrada 1 Exemplo de Saída 1
# 5 1E
# Exemplo de Entrada 2 Exemplo de Saída 2
# 16 2G
# Exemplo de Entrada 3 Exemplo de Saída 3
# 27 3I

def codificar_numero(n):
    triangulo, posicao = divmod(n - 1, 9)
    letras = "ABCDEFGHI"
    return f"{triangulo + 1}{letras[posicao]}"


if __name__ == "__main__":
    n = int(input())
    print(codificar_numero(n))
