import sys

x = sys.stdin.readline
s = []
for i in range(0, 10):
    s.append(int(x()))

result = set()
for i in s:
    result.add(i % 42)
print(len(result))
