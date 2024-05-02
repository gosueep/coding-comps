
N=100
# N=10

sumsq = sum(x**2 for x in range(1,N+1))

sqsum = N * (N+1) // 2
sqsum = sqsum**2

print(sumsq, sqsum, sqsum-sumsq)

"""
38350 25502500 25164150
"""