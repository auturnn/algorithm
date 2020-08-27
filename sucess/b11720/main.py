import sys
x = sys.stdin.readline

n = int(x())
s = str(x().rstrip())

sum = 0

for i in s:
    sum += int(i)

print(sum)
