import sys

x = sys.stdin.readline

a, b = map(str, x().split())

a = int(a[::-1])
b = int(b[::-1])

if a < b:
    print(b)
else:
    print(a)
