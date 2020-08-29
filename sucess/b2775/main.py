import sys

input = sys.stdin.readline

x = int(input())

for y in range(x):
    # 매 루프 마다 리스트 초기화
    s = [[i for i in range(0, 15)]]

    k = int(input())
    n = int(input())

    if k == 0:
        print(s[k][n])
        continue

    for i in range(0, k+1):
        if i == 0:
            continue

        a = []

        for j in range(0, n+1):
            if j == 0:
                a.append(0)
                continue
            if j == 1:
                a.append(1)
                continue
            a.append(s[i-1][j]+a[j-1])

        s.append(a)

    print(s[k][n])
