#
#
#
import sys
from collections import defaultdict
sys.setrecursionlimit(2**30)


class node:

    children = None
    parent = None
    amount = 0

    def __init__(self, children, parent):
        self.children = children
        self.parent = parent

    def add_water(self, added):

        self.amount += added

        if self.amount >= 1 and self.parent is not None:

            # remove this node from parent's children list, and add this nodes children to parent's children
            self.parent.children.remove(self)
            self.parent.children.append(self.children)
            for child in self.children:
                child.parent = self.parent

            # distribute leftover water to children if there is any
            leftover = self.amount - 1
            if leftover != 0:
                for child in self.children:
                    child.add_water(leftover / len(self.children))




def add_water(pdict, tree, node, amount):

    # add water - if no water left over, end (base case)
    leftover = tree[node] + amount - 1
    if leftover <= 0:
        tree[node] += amount
        return

    # else, distribute remaining water to children (recursive case)
    children = len(pdict[node])
    water = leftover / children
    for child in pdict[node]:
        add_water(pdict, tree, child, water)


def fun(pdict, Q, N):

    if Q == N:
        return N

    root = node([], None)

    for parent in pdict

    for query in range(Q-1):
        add_water(pdict, tree, 1, 1)

    return filled


if __name__ == "__main__":

    for case in range(int(input())):
        N, Q = map(int, input().split())


        pdict = defaultdict(list)
        for _ in range(N-1):
            parent, child = map(int, input().split())
            pdict[parent].append(child)

        queries = []
        for _ in range(Q):
            queries.append(int(input()))


        print(f'Case #{case + 1}: {fun(pdict, Q, N)}')

