if __name__ == '__main__':
    line = input()
    for i in range(1, 26):
        newLine = ""
        for c in line:
            if c.isalpha():
                if c.isupper():
                    newC = chr((ord(c) - ord('A') + i) % 26 + ord('A'))
                else:
                    newC = chr((ord(c) - ord('a') + i) % 26 + ord('a'))
                newLine += newC
            else:
                newLine += c

        print(f'Shift: {i} {newLine}')

"""
C:\Users\eugin\AppData\Local\Programs\Python\Python310\python.exe "C:/Users/eugin/Desktop/Code Writeups/TTech22/shiftFinder.py"
Eotaax ar Yuzqe
Shift: 1 Fpubby bs Zvarf
Shift: 2 Gqvccz ct Awbsg
Shift: 3 Hrwdda du Bxcth
Shift: 4 Isxeeb ev Cydui
Shift: 5 Jtyffc fw Dzevj
Shift: 6 Kuzggd gx Eafwk
Shift: 7 Lvahhe hy Fbgxl
Shift: 8 Mwbiif iz Gchym
Shift: 9 Nxcjjg ja Hdizn
Shift: 10 Oydkkh kb Iejao
Shift: 11 Pzelli lc Jfkbp
Shift: 12 Qafmmj md Kglcq
Shift: 13 Rbgnnk ne Lhmdr
                            Shift: 14 School of Mines
Shift: 15 Tdippm pg Njoft
Shift: 16 Uejqqn qh Okpgu
Shift: 17 Vfkrro ri Plqhv
Shift: 18 Wglssp sj Qmriw
Shift: 19 Xhmttq tk Rnsjx
Shift: 20 Yinuur ul Sotky
Shift: 21 Zjovvs vm Tpulz
Shift: 22 Akpwwt wn Uqvma
Shift: 23 Blqxxu xo Vrwnb
Shift: 24 Cmryyv yp Wsxoc
Shift: 25 Dnszzw zq Xtypd
"""