n = int(4 * 1e6)

a, b = 0, 1
seq = []
evens = []

total = 0
while True:
    if a > n or b > n:
        break
    seq.append(b)
    if b % 2 == 0:
        total += b
        evens.append(b)
        
    a,b = b, a+b
    print(total)

print(seq)
print(evens)
print(sum(evens))

"""
4613732
"""