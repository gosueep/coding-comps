tests = int(input())

i = 0

for test in range(tests):
    i += 1

    bags, kids = list(map(int, input().split()))
    candyNums = list(map(int, input().split()))

    totalCandy = 0
    for candyNum in candyNums:
        totalCandy += candyNum

    print(f'Case #{i}: {totalCandy - int(totalCandy // kids * kids)}')


