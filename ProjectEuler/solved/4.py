bigs = [i for i in range(900, 1000)]
px, py = -1, -1
p = 0

for i in range(len(bigs)):
    x = bigs[i]
    for j in range(len(bigs)):
        y = bigs[j]
        
        z = x*y
        s = str(z)
        palindrome = True
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                palindrome = False
        if palindrome:
            if z > p:
                px, py = x, y
                p = z
print(p)
print(px, py)

"906609"