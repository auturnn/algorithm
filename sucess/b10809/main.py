import sys

x = sys.stdin.readline

w = str(x())
s = [i for i in range(ord('a'), ord('z')+1)]

for i, v in enumerate(s):
    if chr(v) in w:
        s[i] = w.index(chr(v))
    elif chr(v) not in w:
        s[i] = -1

print(" ".join(map(str, s)))
