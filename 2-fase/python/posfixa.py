def parse(exp):
    symbol = ""
    op = ""

    i = 0
    lvl = 0
    while i < len(exp):
        if exp[i] == "(":
            lvl = 1
            new_exp = exp[i + 1]
            i += 2

    for chr in exp:
        if chr in ["+", "-", "*", "/", "^"]:
            op += chr
        else:
            symbol += chr

    return f"{op}{symbol}"
