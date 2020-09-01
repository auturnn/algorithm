import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()
waits = 0
for i in range(len(p)+1):
    if i == 0:
        continue
    else:
        waits += sum(p[:i])

print(waits)
