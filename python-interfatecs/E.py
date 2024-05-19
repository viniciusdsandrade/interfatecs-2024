n = int(input())
quantidade = list(map(int, input().split()))
m = int(input())
res = []
for i in range(m):
    regiao = input().split()
    nome = regiao.pop(0)
    regiao = list(map(int, regiao))
    grupos = []
    for j in range(n):
        grupos.append(regiao[j] // quantidade[j])
    res.append(f'{nome} {min(grupos)}')

print('\n'.join(res))
