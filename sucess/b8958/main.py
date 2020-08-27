import sys

x = sys.stdin.readline

n = int(x())
s = []

# sys.stdin.readline = 개행 포함 || + .rstrip = 개행 빼고

for i in range(n):
    s.append(str(x().rstrip()))

# for j in i[:-1]로 해도 상관없음
for i in s:
    score = 0
    cnt = 0
    for j in i:
        if j == "O":
            cnt = cnt+1
        elif j == "X":
            cnt = 0
        score += cnt
    print(score)
