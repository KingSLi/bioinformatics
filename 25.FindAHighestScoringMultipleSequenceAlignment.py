import numpy as np
import itertools


def retract_answer(a, b, c, dp_path):
    ans = [[], [], []]
    i = len(a)
    j = len(b)
    k = len(c)

    while i > 0 or j > 0 or k > 0:
        state1, state2, state3 = dp_path[i][j][k]

        if state1 == 1:
            ans[0].append(a[i - 1])
            i -= 1
        else:
            ans[0].append('-')

        if state2 == 1:
            ans[1].append(b[j - 1])
            j -= 1
        else:
            ans[1].append('-')

        if state3 == 1:
            ans[2].append(c[k - 1])
            k -= 1
        else:
            ans[2].append('-')

    return ''.join(reversed(ans[0])), ''.join(reversed(ans[1])), ''.join(reversed(ans[2]))


def main():
    a = input()
    b = input()
    c = input()

    n = len(a)
    m = len(b)
    l = len(c)

    dp = np.zeros(shape=(n + 1, m + 1, l + 1), dtype=int)
    dp_path = [[[' '] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    for i, j, k in itertools.product(range(n + 1), range(m + 1), range(l + 1)):
        for _i, _j, _k in itertools.product(range(2 - (i == n)), range(2 - (j == m)), range(2 - (k == l))):
            if _i == _j == _k == 0:
                continue
            value = dp[i][j][k] + int(_i == _j == _k == 1 and a[i] == b[j] == c[k])
            if dp[i + _i][j + _j][k + _k] < value or dp_path[i + _i][j + _j][k + _k] == ' ':
                dp[i + _i][j + _j][k + _k] = value
                dp_path[i + _i][j + _j][k + _k] = (_i, _j, _k)

    a1, b1, c1 = retract_answer(a, b, c, dp_path)
    print(dp[n][m][l])
    print(a1)
    print(b1)
    print(c1)


if __name__ == '__main__':
    main()
