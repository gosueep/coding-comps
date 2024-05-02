#
#
#

def fun(fabrics):

    ada = fabrics.copy()
    charles = fabrics.copy()

    ada.sort(key=lambda x: (x[0], x[2]))
    charles.sort(key=lambda x: (x[1], x[2]))


    count = 0
    for i in range(len(fabrics)):
        if ada[i][2] == charles[i][2]:
            count += 1

    return count


if __name__ == "__main__":

    for case in range(int(input())):
        N = int(input())
        fabrics = []
        for i in range(N):
            color, durability, uid = input().split()
            fabrics.append([color, int(durability), int(uid)])


        print(f'Case #{case + 1}: {fun(fabrics)}')
