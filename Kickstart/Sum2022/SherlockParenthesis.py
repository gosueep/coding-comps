def find_max_num_balanced_substrings(l, r):
    max_num_substrings = 0
    # TODO: Add logic to find the maximum possible number of balanced non-empty

    pairs = min(l,r)

    # substrings
    return int(pairs * (pairs+1) / 2)


def main():
    # Get number of test cases
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        # Get total of left and right parentheses
        l, r = map(int, input().split())
        ans = find_max_num_balanced_substrings(l, r)
        print(f"Case #{test_case}: {ans}")


if __name__ == "__main__":
    main()
