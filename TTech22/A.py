from math import floor, ceil, sqrt


def isPrime(num):
    if num % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(num))+2, 2):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':

    for line in open('C1.txt').readlines():

        largest = 0
        length = len(line.strip())

        for i in range(length):
            for j in range(i+1, length+1):
                # print(line[i:j])
                num = int(line[i:j])
                if num > largest and isPrime(num):
                    largest = num

        print(largest)



