"""
Below 10

9 // 3 = 3

3*1 + 3*2 + 3*3
3 (1 + 2 + 3 ...)
3 * (geosum)


9 // 5 = 1

5*1 = 1


"""

N = 9
N = 1000

total = 0
for i in range(1, N):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

"""
233168
"""