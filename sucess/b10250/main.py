import sys

x = sys.stdin.readline

t = int(x())

for i in range(t):
    h, w, n = map(int, x().split())
    m = [(x+y) for x in range(1, w+1)
         for y in range(100, (h+1)*100, 100)]
    print(m[n-1])
