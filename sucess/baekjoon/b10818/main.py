import sys
x = sys.stdin.readline

n = int(x())
s = list(map(int, x().split()))

print(min(s), max(s))
