def revert(perm, start, finish):
    perm[start:finish] = list(map(lambda x: x * -1, reversed(perm[start:finish])))


def print_(perm):
    print('({0})'.format(' '.join(list(map(lambda x: '{:+d}'.format(x), perm)))))


perm = list(map(int, input()[1:-1].split()))
for i in range(len(perm)):
    number = i + 1
    pos = perm.index(number) if number in perm else perm.index(-number)
    if pos != i:
        revert(perm, i, pos + 1)
        print_(perm)
    if perm[i] < 0:
        perm[i] *= -1
        print_(perm)
