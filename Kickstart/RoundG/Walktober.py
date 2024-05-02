
def walktober():
    days, parts, john_id = map(int, input().split())

    john = []
    maxs = [0] * parts

    for d in range(days):
        steps = list(map(int, input().split()))
        if d+1 == john_id:
            john = steps
        for i in range(parts):
            if steps[i] > maxs[i]:
                maxs[i] = steps[i]

    total = 0
    for i in range(parts):
        total += maxs[i] - john[i]

    return total


if __name__ == '__main__':
    for case in range(int(input())):
        print(f'Case #{case + 1}: {walktober()}')
