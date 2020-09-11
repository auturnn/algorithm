import sys

input = sys.stdin.readline

n = int(input())
s = [0] * 10001

for i in range(n):
    s[int(input())] += 1
    
for i in range(10001):
    if s[i] != 0:
        for j in range(s[i]):
            print(i)