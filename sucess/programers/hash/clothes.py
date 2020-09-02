def solution(clothes):
    s = {k[1]: 0 for k in clothes}

    for k in s:
        for i in clothes:
            if i[1] == k:
                s[k] += 1

    v = [i+1 for i in s.values()]

    cnt = 1
    for i in v:
        cnt *= i

    return cnt-1
