n = int(input())
result = []
for i in range(n):
    palavra = input()
    telefone = ""

    for letra in palavra:
        if letra in "ABC":
            telefone += "2"
        elif letra in "DEF":
            telefone += "3"
        elif letra in "GHI":
            telefone += "4"
        elif letra in "JKL":
            telefone += "5"
        elif letra in "MNO":
            telefone += "6"
        elif letra in "PQRS":
            telefone += "7"
        elif letra in "TUV":
            telefone += "8"
        elif letra in "WXYZ":
            telefone += "9"
    result.append(telefone)
print('\n'.join(result))
