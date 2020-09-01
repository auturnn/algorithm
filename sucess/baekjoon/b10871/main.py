import sys

input = sys.stdin.readline

n,x = map(int, input().split())
result = [i for i in list(map(int,input().split())) if i < x]

print(' '.join(map(str, result)))