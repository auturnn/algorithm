import sys

x = sys.stdin.readline

t = int(x())

result = []
for i in range(t):
    replaceWord = ""
    r, s = x().split()
    for j in s:
        replaceWord += j*int(r)
    result.append(replaceWord)

for i in result:
    print(i)
