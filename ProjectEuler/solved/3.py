x = 13195
x = 600851475143
seq = [x]


y = seq[-1]

while True:
    print('y:', y)
    prime = True
    for i in range(2, int(y ** 1/2)):
        if y % i == 0:
            seq.append(i)
            print(f'{y} / {i} == {y//i}')
            y = y // i
            prime = False
            break
    if prime:
        seq.append(y)
        print(y, ' is prime!')
        break
    
print(seq)

"""
6857
"""