import sys

x = sys.stdin.readline

s = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7,
     7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]

word = str(x().rstrip())
sum = 0

for i in word:
    sum += s[ord(i)-65]

print(sum)
