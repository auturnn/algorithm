import sys

x = sys.stdin.readline

s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = str(x().rstrip())

for i in s:
    word = word.replace(i, "!")

print(len(word))
