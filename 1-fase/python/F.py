placa = input()
if len(placa) <= 6 and placa[0] in "AP" and placa[1:].isnumeric():
    print("Placa muito antiga")
elif len(placa) <= 7 and placa.isnumeric():
    print("Placa numerica")
elif len(placa) == 6 and placa[:2].isalpha() and placa[2:].isnumeric():
    print("Placa AA-9999")
elif len(placa) == 7 and placa[:3].isalpha() and placa[3:].isnumeric():
    print("Placa AAA-9999")
elif len(placa) == 7 and placa[:3].isalpha() and placa[3].isnumeric() and placa[4].isalpha() and placa[5:].isnumeric():
    print("Placa Mercosul")
else:
    print("Placa invalida")
