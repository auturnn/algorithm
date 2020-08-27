import sys

x = sys.stdin.readline

word = str(x().rstrip()).upper()
s = [word.count(chr(w)) for w in range(ord('A'), ord('Z')+1)]

if s.count(max(s)) != 1:
    print("?")
else:
    print(chr(s.index(max(s))+65))
