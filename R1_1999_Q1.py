def river(num):
    string = str(num)
    new = num
    for i in string:
        new += int(i)
    return new
n = int(input())
r1 = 1
r3 = 3
r9 = 9
values = [n]
if n == r1 or n == r3 or n == r9:
    print(f"first meets river {n} at {n}")
else:
    while True:
        n = river(n)
        values.append(n)
        r1 = river(r1)
        if r1 in values:
            print(f"first meets river 1 at {r1}")
            break
        r3 = river(r3)
        if r3 in values:
            print(f"first meets river 3 at {r3}")
            break
        r9 = river(r9)
        if r9 in values:
            print(f"first meets river 9 at {r9}")
            break
