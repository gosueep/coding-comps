def isPali(s):
    L = 0
    R = len(s)-1
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True

ans = 0
palis = set()
for x in range(0, 10):
    a = x * 1e5 + x
    for y in range(0, 10):
        b = y * 1e4 + y * 10
        for z in range(0, 10):
            c = z * 1e3 + z * 1e2
            ten = int(a + b + c)
            if x == 0:
                ten //= 10
                if y == 0:
                    ten //= 10
            res = bin(ten)[2:]
            # print(a, b, c)
            print(ten, res)
            if isPali(str(res)):
                print(ten, res)
                if ten not in palis:
                    ans += ten
                palis.add(ten)
print(ans)