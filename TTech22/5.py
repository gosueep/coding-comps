
"""
"Jmv Oibma: Q'u owvvi abmit qb.

Zqtmg Xwwtm: Epib?

Jmv Oibma: Q'u owvvi abmit bpm Lmktizibqwv wn Qvlmxmvlmvkm.

Vibqwvit Bzmiaczm."
"""
SHIFT = 18
if __name__ == '__main__':

    shifted = ". "

    for line in open('C5.txt').readlines():
        newLine = ""
        for c in line:
            if c.isalpha():
                if c.isupper():
                    newC = chr((ord(c) - ord('A') + SHIFT) % 26 + ord('A'))
                else:
                    newC = chr((ord(c) - ord('a') + SHIFT) % 26 + ord('a'))
                newLine += newC
            else:
                newLine += c

        print(newLine.strip())
        shifted += newLine.strip() + ' '


"""
"Ben Gates: I'm gonna steal it.

Riley Poole: What?

Ben Gates: I'm gonna steal the Declaration of Independence.

National Treasure."
"""