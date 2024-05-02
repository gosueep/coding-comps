memo = {
    0: 0,
    1: 1,
    2: 1,
    3: 2
}


def trib(n):
    if n in memo:
        return memo[n]

    t = trib(n-1) + trib(n-2) + trib(n-3)
    memo[n] = t
    return t


if __name__ == "__main__":
    print(trib(int(input())))