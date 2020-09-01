import sys

x = sys.stdin.readline

n = int(x())
if n == 1:
    print(1)
else:
    i = 1
    end_room = 7
    esc = 2
    while True:
        if n <= end_room:
            print(esc)
            break
        esc += 1
        i += 1
        end_room += (i*6)
