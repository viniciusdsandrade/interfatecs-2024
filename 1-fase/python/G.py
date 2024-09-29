n = int(input())

categorias = {
    "ALGORITMOS": [],
    "BOAS PRATICAS": [],
    "DESEMPENHO": [],
    "FLUXOGRAMAS": [],
    "INTERPRETACAO DE ENUNCIADOS": [],
    "SINTAXE DA LINGUAGEM": [],
    "FICA PARA PROXIMA!": []
}

chaves_categorias = list(categorias.keys())

nome = input()
while nome != '':
    partes_nome = nome.split()
    categorias_aluno = partes_nome[1:]
    if n > 0:
        for categoria in categorias_aluno:
            categorias[chaves_categorias[int(categoria) - 1]].append(partes_nome[0])
    else:
        categorias["FICA PARA PROXIMA!"].append(partes_nome[0])
    n -= 1
    nome = input()

for categoria, alunos in categorias.items():
    if categoria == "FICA PARA PROXIMA!":
        continue
    print("-" * 30)
    print(categoria)
    print("-" * 30)
    for aluno in sorted(alunos):
        print(aluno)
    print()

if categorias["FICA PARA PROXIMA!"]:
    print("-" * 30)
    print("FICA PARA PROXIMA!")
    print("-" * 30)
    for aluno in categorias["FICA PARA PROXIMA!"]:
        print(aluno)
    print()
