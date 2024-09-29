import math

N, ang = map(int, input().split())
pi = 3.1415
ang = ang * pi / 180

result = []
for _ in range(N):
    point = list(map(int, input().split()))
    x, y = point
    result.append((x * math.cos(ang) - y * math.sin(ang), x * math.sin(ang) + y * math.cos(ang)))

for x, y in result:
    print(f'{x:.2f} {y:.2f}')
