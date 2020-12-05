import numpy as np


def parse_pam():
    alg = 'ACDEFGHIKLMNPQRSTVWY'
    pam = {}
    with open('PAM250.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            pam[alg[i]] = {alg[j]: int(c) for j, c in enumerate(line.split(' '))}
    return pam


def retract_answer(big, small, dp_path, x, y):
    ans1 = []
    ans2 = []
    i = x
    j = y

    while i > 0 or j > 0:
        if dp_path[i, j] == 2:
            break
        elif dp_path[i, j] == 1:
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
    pam = parse_pam()
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
                if dp[i, j - 1] + delta > 0:
                    dp[i, j] = dp[i, j - 1] + delta
                    dp_path[i, j] = -1
                else:
                    dp[i, j] = 0
                    dp_path[i, j] = 2
            if i > 0 and dp[i - 1, j] + delta > dp[i, j]:
                if dp[i - 1, j] + delta >= 0:
                    dp[i, j] = dp[i - 1, j] + delta
                    dp_path[i, j] = 1
                else:
                    dp[i, j] = 0
                    dp_path[i, j] = 2
            if i > 0 and j > 0 and dp[i - 1, j - 1] + pam[big[i - 1]][small[j - 1]] > dp[i, j]:
                if dp[i - 1, j - 1] + pam[big[i - 1]][small[j - 1]] > 0:
                    dp[i, j] = dp[i - 1, j - 1] + pam[big[i - 1]][small[j - 1]]
                    dp_path[i, j] = 0
                else:
                    dp[i, j] = 0
                    dp_path[i, j] = 2
    print(np.max(dp))
    x, y = np.argmax(dp) // dp.shape[1], np.argmax(dp) % dp.shape[1]
    up, down = retract_answer(big, small, dp_path, x, y)
    print(up)
    print(down)


if __name__ == '__main__':
    main()
