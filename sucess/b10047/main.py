import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
cnt = 0
for i in range(n):
    coin.append(int(input()))

coin.reverse()

for i in coin:
    if k == 0:
        break
    if k // i == 0:
        continue
    elif k // i != 0:
        cnt += (k//i)
        k %= i

print(cnt)
