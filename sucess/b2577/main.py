import sys

x = sys.stdin.readline

s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n = int(x()) * int(x()) * int(x())
n = str(n)
for i in range(0, 10):
    for j in n:
        if str(i) == j:
            s[i] += 1

for i in s:
    print(i)
