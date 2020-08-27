
def solve(a: list) -> int:
    sum = 0
    for i in a:
        sum += i
    return sum


x = [1, 2, 3, 4, 5]
z = solve(a=x)
print(z)
