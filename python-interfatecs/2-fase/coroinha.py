l, c, _, cl, cc = [int(m) for m in input().split()]

caminho = input()

for chr in caminho:
    if chr == "C":
        cl += 1
    elif chr == "D":
        cc -= 1
    elif chr == "B":
        cl -= 1
    elif chr == "E":
        cc += 1

if cl < 0 or cc < 0 or cl > l or cc > c:
    print("-1 -1")
else:
    print(cl, cc)
