"""
Simple Digit sum of 2^1000

1366
"""



N = 2**1000
# N=2**15

x = N
digitsum = 0
while x != 0:
    digitsum += x % 10      # Current right-most digit
    x = x // 10             # chop off right-most digit

# print(N)
print(digitsum)     # 1366