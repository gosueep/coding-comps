if __name__ == '__main__':
    f = open('signal.txt')

    symbols = []
    bytes = []
    noise = 0
    total_lines = 0

    while f:
        heights = []
        for i in range(32):
            line_fixed = f.readline().strip()
            if len(line_fixed) > 0:
                heights.append(float(line_fixed))

        if len(heights) == 0:
            break

        indexFirstZero = 0
        for i in range(32):
            if i > 0:
                if heights[i - 1] < 0 and heights[i] > 0:
                    indexFirstZero = i - 1
                    break

        minHeight = min(heights)
        maxHeight = max(heights)

        amplitude = (maxHeight - minHeight) / 2

        phaseShift = 0
        if indexFirstZero > 16:
            phaseShift = (1 - (indexFirstZero / 32)) * 2
        else:
            phaseShift = (indexFirstZero / 32) * 2

        bitstring = ""

        if amplitude > 0.5:
            bitstring += "1"
        else:
            bitstring += "0"

        total_lines += 1
        if phaseShift > 0.5:
            if phaseShift != 0.75:
                noise += 1
            bitstring += "1"
        else:
            if phaseShift != 0.25:
                noise += 1
            bitstring += "0"

        symbols.append(bitstring)

        if len(symbols) == 4:
            bytes.append(int("".join(symbols)[::-1], 2))
            symbols.clear()

    f.close()

    print(noise / total_lines)

    f = open('image.png', 'wb')
    f.write(bytearray(bytes))
    f.close()

