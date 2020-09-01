import sys
x = sys.stdin.readline

n = int(x())
s = list(map(float, x().split()))

sum = 0
max_s = max(s)

for i in range(n):
    s[i] = (s[i]/max_s)*100
    sum += s[i]

print(sum/n)
