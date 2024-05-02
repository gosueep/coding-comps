
# 20 - 1, 2, 4, 5, 10, 20
# 19
# 18 - 6, 3
# 17
# 16 - 4 DONE
# 15 - 5, 3 DONE
# 14 - 7 (ADD), 2
# 13
# 12 - 6,2 DONE
# 11
# 10 DONE
# 9 (maybe a 3)
# 8 - 4, 2 DONE
# 7 - DONE
# 6 - 2,3 DONE
# 5 - DONE
# 4 - DONE
# 3 DONE
# 2 DONE
s = set()
N = 20
# N=10
prod = 1
x = N
while x > 0:
    if x not in s:
        f=x
        for i in s:
            if f % i == 0:
                f = f // i
        
        for i in range(1, f+1):
            if x % i == 0:
                s.add(i)
        prod *= f

    print(x, prod, s, f)
    x -= 1

print(prod)

check = True
for i in range(1, N+1):
    if prod % i != 0:
        check = False
    # print(i, check)
print(check)

# 10 - 1, 2, 5
# 9 - 9
# 8 - 4 (ADD)
# 7
# 6 DONE
# 5 DONE
# 4 DONE
# 3 DONE
# 2


"""
232792560
"""

