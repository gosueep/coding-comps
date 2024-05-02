from random import randrange


def buildPal(questions):

    seenList = [[0] * 26]

    for char in input():
        alphaList = list(seenList[-1])          # makes a new list, not pointing to original
        alphaList[ord(char) - ord('A')] += 1
        seenList.append(alphaList)

    palindromes = 0

    for _ in range(questions):
        start, end = map(int, input().split())

        odd = 0
        for char in range(26):
            if (seenList[end][char] - seenList[start-1][char]) % 2 == 1:
                odd += 1
                if odd == 2:
                    palindromes -= 1
                    break

        palindromes += 1


    return palindromes


if __name__ == "__main__":

    # Get number of test cases
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        # Get total of left and right parentheses
        n, q = map(int, input().split())

        count = buildPal(q)

        print(f"Case #{test_case}: {count}")
