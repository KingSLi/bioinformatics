import numpy as np


def parse_blosom():
    alg = 'ACDEFGHIKLMNPQRSTVWY'
    blosom = {}
    with open('BLOSUM62.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            blosom[alg[i]] = {alg[j]: int(c) for j, c in enumerate(line.split(' '))}
    return blosom


def retract_answer(big, small, dp_path):
    ans1 = []
    ans2 = []
    i = len(big)
    j = len(small)
    while i > 0 or j > 0:
        if dp_path[i, j] == 1:
            ans1.append(big[i - 1])
            ans2.append('-')
            i -= 1
        elif dp_path[i, j] == -1:
            ans1.append('-')
            ans2.append(small[j - 1])
            j -= 1
        elif dp_path[i, j] == 0:
            ans1.append(big[i - 1])
            ans2.append(small[j - 1])
            i -= 1
            j -= 1

    return ''.join(reversed(ans1)), ''.join(reversed(ans2))


def main():
    blosom = parse_blosom()
    big = input()
    small = input()
    delta = -5
    n = len(big)
    m = len(small)

    # print(blosom['P']['M'])

    dp = np.zeros(shape=(n + 1, m + 1), dtype=int) - 1000000000
    dp_path = np.zeros(shape=(n + 1, m + 1), dtype=int)
    dp[0, 0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if j > 0 and dp[i, j - 1] + delta > dp[i, j]:
                dp[i, j] = dp[i, j - 1] + delta
                dp_path[i, j] = -1
            if i > 0 and dp[i - 1, j] + delta > dp[i, j]:
                dp[i, j] = dp[i - 1, j] + delta
                dp_path[i, j] = 1
            if i > 0 and j > 0 and dp[i - 1, j - 1] + blosom[big[i - 1]][small[j - 1]] > dp[i, j]:
                dp[i, j] = dp[i - 1, j - 1] + blosom[big[i - 1]][small[j - 1]]
                dp_path[i, j] = 0
    print(dp[n, m])
    up, down = retract_answer(big, small, dp_path)
    print(up)
    print(down)


if __name__ == '__main__':
    main()
