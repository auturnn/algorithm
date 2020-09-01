# 참조 - https://this-programmer.com/entry/%EB%B0%B1%EC%A4%804673%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%ED%94%84-%EB%84%98%EB%B2%84

def d(n: list) -> list:
    x = []
    for i in n:
        for j in str(i):
            i += int(j)
        x.append(i)
    return x


n = [i for i in range(1, 10001)]
a = d(n)
self_num = [i for i in n if i not in a]

for i in self_num:
    print(i)
