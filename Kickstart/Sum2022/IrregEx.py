
VOWELS = "aeiou"


def isSpell(word):

    # substring starting from first vowel
    while word[0] not in VOWELS:
        word = word[1:]
    # if less than 5 letters, cannot be a spell
    if len(word) < 5:
        return False

    # find second vowel
    vow2 = 1
    while word[vow2] not in VOWELS:
        vow2 += 1

    firstWord = word[:vow2+1]
    # print(f'First Word: {firstWord}')

    ######## get middle word
    # get first vowel after firstWord
    vow3 = vow2 + 1
    while word[vow3] not in VOWELS:
        vow3 += 1
    # find second vowel after start (end of mid / start of last)
    vow4 = vow3 + 1
    while vow4 > len(word) and word[vow4] not in VOWELS:
        vow4 += 1


    # midWord = word[vow2+1:vow4]
    # print(f'Mid Word: {midWord}')
    #
    # print(f'Last Word: {word[vow4:]}')

    if firstWord in word[vow3:]:
        return True



    while vow4 > len(word):
        charsCut = vow2

        word = word[vow2:]
        vow2 = vow3 - charsCut
        vow3 = vow4 - charsCut

        vow4 += 1
        while word[vow4] not in VOWELS:
            vow4 += 1

        firstWord = word[:vow2 + 1]
        if firstWord in word[vow3:]:
            return True


    return False

#
# def findVowel(word):
#     pos = 0


if __name__ == "__main__":

    for case in range(int(input())):

        output = "Nothing."
        if isSpell(input()):
            output = "Spell!"

        print(f'Case #{case}: {output}')
