import sys

x = sys.stdin.readline

a, b, c = map(int, x().split())
if b >= c:
    print("-1")
elif a < b-c:
    print("-1")
else:
    print((a//(c-b))+1)
