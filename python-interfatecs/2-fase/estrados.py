n = int(input())

for _ in range(n):
    lt_estrado, qtd_ripas, largura_ripas = [int(k) for k in input().split()]

    res = (lt_estrado - (qtd_ripas * largura_ripas)) / (qtd_ripas - 1)

    if res < 10:
        print("projeto superdimensionado")
    elif res <= 20:
        print("projeto ok")
    else:
        print("projeto subdimensionado")
