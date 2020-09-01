import sys

x = sys.stdin.readline
n = int(x().rstrip())

cnt = 0

while True:
    if n % 5 == 0:
        n = (n//5) + cnt
        break
    elif n < 0:
        n = -1
        break
    cnt += 1
    n -= 3

print(n)
