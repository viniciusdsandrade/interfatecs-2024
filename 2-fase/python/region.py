# Problema A

# Region

# Donald Harris is an american entrepreneur beginning business in Brazil. He is famous due to his chain
# of stores that provides in-person service at several addresses and makes home deliveries regardless of the
# purchase value.
# The only restriction on his delivery system is that the address must be within a region close to one of the
# physical stores in his network. Upon his arrival in Brazil, he learned about the CEP code system used by
# the brazilian company Correios and determined that a survey be carried out to determine which CEP codes
# would be considered for each store.
# Now that work is done, and he needs a computer program that can determine whether a customer’s address
# is within a service region or not, and you, lucky guy, have been hired to develop it.

# Input

# The input consists of a test case, the first line of which contains an integer QR (0 < QR  100) that defines
# the number of regions served by a store. Next, there are QR lines containing two valid CEP codes, according
# to the Brazilian standard. This section is not supposed to be ordered in any way.
# The next line contains an integer Q (0 < QR  1000) that represents the number of delivery requests,
# followed by Q lines containing the customer’s CEP code, according to the Brazilian standard. This section
# is also not ordered.
# It is ensured that all the CEP codes in the input are in a valid format.

# Output

# The program should provide information for each customer’s CEP code about whether they are served
# by the delivery system.
# First, the output should contain, in ascending order, the list of customer CEP codes served by the delivery
# system in a format consisting of the CEP code number followed by the phrase is served by our delivery
# system (in lowercase letters).
# Then, the unserved CEP codes should be listed, in ascending order, in a similar format with the CEP code
# followed by the phrase is not served by our delivery system (in lowercase letters).
# Remember the newline character at the end of each line.
# Maratona de Programação InterFatecs 2024 - Problema A: Region 3

# Exemplo de Entrada 1
# 1
# 15510-000 15512-000
# 5
# 15509-000
# 15510-000
# 15511-000
# 15512-000
# 15513-000

# Exemplo de Saída 1
# 15510-000 is served by our delivery system
# 15511-000 is served by our delivery system
# 15512-000 is served by our delivery system
# 15509-000 is not served by our delivery system
# 15513-000 is not served by our delivery system

# Exemplo de Entrada 2
# 3
# 07503-000 07550-900
# 07840-500 07850-000
# 08200-020 08240-500
# 10
# 07520-010
# 07395-550
# 08236-200
# 07835-060
# 07921-370
# 12410-030
# 07526-490
# 08209-000
# 08541-210
# 07550-900

# Exemplo de Saída 2
# 07520-010 is served by our delivery system
# 07526-490 is served by our delivery system
# 07550-900 is served by our delivery system
# 08209-000 is served by our delivery system
# 08236-200 is served by our delivery system
# 07395-550 is not served by our delivery system
# 07835-060 is not served by our delivery system
# 07921-370 is not served by our delivery system
# 08541-210 is not served by our delivery system
# 12410-030 is not served by our delivery system


# Função para formatar um CEP (código postal) em um formato padrão "xxxxx-xxx"
def format_cep(cep: int) -> str:
    # Divide o CEP em dois blocos: os primeiros 5 dígitos e os últimos 3
    return f"{cep // 1000:05}-{cep % 1000:03}"


# Função para processar as regiões de atendimento
def process_regions(qr: int) -> list[tuple[int, int]]:
    regions = []
    for _ in range(qr):
        # Lê duas entradas, remove o traço do CEP e converte para inteiros
        # Ordena os dois CEPs para garantir que o menor esteja à esquerda (a <= b)
        a, b = sorted([int(st.replace("-", "")) for st in input().split()])
        regions.append((a, b))  # Adiciona o par de região (início, fim) à lista
    return regions  # Retorna a lista de regiões (faixas de CEP)


# Função para processar os pedidos e determinar se são atendidos ou não
def process_requests(
        q: int,
        regions: list[tuple[int, int]]
) -> tuple[list[int], list[int]]:
    served, not_served = [], []  # Listas para armazenar os CEPs atendidos e não atendidos

    for _ in range(q):
        c = int(input().replace("-", ""))  # Lê e converte o CEP de entrada
        # Verifica se o CEP está dentro de alguma faixa de região atendida
        if any(a <= c <= b for a, b in regions):
            served.append(c)  # Adiciona à lista de atendidos
        else:
            not_served.append(c)  # Adiciona à lista de não atendidos

    # Retorna as listas de CEPs atendidos e não atendidos, ambas ordenadas
    return sorted(served), sorted(not_served)


# Função para imprimir os resultados do processamento de CEPs
def print_result(ceps: list[int], served: bool) -> None:
    for cep in ceps:
        # Determina o status (atendido ou não) com base no parâmetro 'served'
        status = "served" if served else "not served"
        # Formata e imprime o CEP com seu respectivo status
        print(f"{format_cep(cep)} is {status} by our delivery system")


def main():

    qr = int(input())
    regions = process_regions(qr)

    q = int(input())
    served, not_served = process_requests(q, regions)

    print_result(served, served=True)
    print_result(not_served, served=False)


if __name__ == "__main__":
    main()
