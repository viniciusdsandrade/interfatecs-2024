regioes = {
    "superior": 0,
    "esquerda": 0,
    "centro": 0,
    "direita": 0,
    "inferior": 0
}
n = int(input())

for _ in range(n):
    matriz = []
    for _ in range(6):
        matriz.append(list(map(int, input().split())))

    for i in range(6):
        for j in range(3):
            if i <= 2 and j == 0:
                regioes["superior"] += matriz[i][j]
            elif j == 0:
                regioes["esquerda"] += matriz[i][j]
            elif j == 1:
                regioes["centro"] += matriz[i][j]
            elif j == 2:
                regioes["direita"] += matriz[i][j]
            if i == 5:
                regioes["inferior"] += matriz[i][j]

lista = []

for regiao, valor in regioes.items():
    lista.append((valor, regiao))

lista.sort(reverse=True)

nMax = lista[0][0]
nlista = [lista[0]]

for i in lista[1:]:
    if i[0] == nMax:
        nlista.append(i)

if len(nlista) > 1:
    nlista.sort(key=lambda x: x[1])
    print(nlista[0][1])
else:
    print(nlista[0][1])
