# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47e79

def magic_well(lilies):
    best = float('inf')
    for i in range(1, lilies+1):
        rem = lilies - i
        altCost = i + 4 + 2 * (rem // i) + (rem % i)
        if lilies > altCost:
            if altCost < best:
                best = altCost

    if best < lilies:
        return best
    return lilies


if __name__ == "__main__":

    for case in range(int(input())):
        N = int(input())

        print(f'Case #{case + 1}: {magic_well(N)}')
