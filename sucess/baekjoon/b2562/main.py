import sys

x = sys.stdin.readline

s = []
for i in range(0, 9):
    s.append(int(x()))

print(max(s))
print(s.index(max(s))+1)
