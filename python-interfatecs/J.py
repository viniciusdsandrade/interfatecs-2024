pessoas = int(input())
jogadores = []
for i in range(pessoas):
    jogadores.append(input())
rodadas = int(input())

pontos = [0] * pessoas

for i in range(rodadas):
    palitos = list(map(int, input().split()))
    palpites = list(map(int, input().split()))

    total = sum(palitos)
    acertou = False

    for j in range(pessoas):
        if palpites[j] == total:
            pontos[j] += 1
            acertou = True
            break

if pontos.count(max(pontos)) > 1:
    print('EMPATE')
else:
    print(f'{jogadores[pontos.index(max(pontos))]} GANHOU')
