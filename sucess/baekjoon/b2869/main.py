import sys

x = sys.stdin.readline

a, b, v = map(int, x().split())

print((v-b-1)//(a-b)+1)
