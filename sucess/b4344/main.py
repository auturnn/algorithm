import sys

input = sys.stdin.readline

c = int(input())
avgScore = []

for i in range(c):
    score = []
    sum, cnt = 0, 0

    score = list(map(int, input().split()))

    for j in range(1, score[0]+1):
        sum += score[j]

    avg = float(sum/score[0])
    for x in range(1, score[0]+1):
        if avg < score[x]:
            cnt += 1

    avg = float(cnt/score[0]) * 100
    print('{0:.3f}%'.format(avg))
