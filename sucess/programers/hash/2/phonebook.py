# def solution(phone_book):
#     for i in phone_book:
#         for j in phone_book:
#             if i == j:
#                 continue
#             if i == j[0:len(i)]:
#                 return False

#     return True


def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
