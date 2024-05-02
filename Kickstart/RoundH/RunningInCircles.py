# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c4766e

def circles():
    length, numRuns = map(int, input().split())
    distance = 0
    laps = 0
    for _ in range(numRuns):
        dist, direction = input().split()
        dist = int(dist)
        if direction == 'A':
            dist *= -1
        distance += dist

        if distance > 0:
            laps += distance // length
            distance = distance % length
        if distance < 0 and distance <= (-1 * length):
            laps += distance // (-1 * length)
            distance = distance % (-1 * length)

    return laps


if __name__ == "__main__":

    for case in range(int(input())):
        print(f'Case #{case + 1}: {circles()}')
