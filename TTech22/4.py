if __name__ == '__main__':

    shifted = ". "

    for line in open('C4.txt').readlines():
        newLine = ""
        for c in line:
            if c.isalpha():
                if c.isupper():
                    newC = chr((ord(c) - ord('A') + 14) % 26 + ord('A'))
                else:
                    newC = chr((ord(c) - ord('a') + 14) % 26 + ord('a'))
                newLine += newC
            else:
                newLine += c

        print(newLine.strip())
        shifted += newLine.strip() + ' '

    # print(shifted)
    firstLetters = ''
    for index, c in enumerate(shifted):
        if c in '.!?' and index+2 < len(shifted):
            firstLetters += shifted[index+2]
    print(firstLetters)
