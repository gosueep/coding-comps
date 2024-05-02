# 
#
# 

def mentorpick(students):

    studs = sorted(students)
    mentors = dict()

    bestM = 0
    for s in range(len(studs)):

        rating = studs[s] * 2

        while bestM < len(studs) and studs[bestM] <= rating:
            bestM += 1
        bestM -= 1          # go back to last mentor that isn't > 2 * rating

        if bestM == s:
            if bestM == 0:
                mentors[studs[s]] = -1
                bestM = s
            else:
                mentors[studs[s]] = studs[bestM-1]
        else:
            mentors[studs[s]] = studs[bestM]

    return [mentors[x] for x in students]


if __name__ == "__main__":

    for case in range(int(input())):
        numStudents = int(input())
        students = list(map(int, input().split()))

        print(f'Case #{case+1}: {" ".join([str(i) for i in mentorpick(students)])}')


