import numpy as np


def main():
    n, m = map(int, input().split())
    down = [list(map(int, input().split())) for i in range(n)]
    _ = input()
    right = [list(map(int, input().split())) for i in range(n + 1)]
    dp = np.zeros(shape=(n + 1, m + 1), dtype=int)
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i, j] = dp[i, j - 1] + right[i][j - 1]
            elif j == 0:
                dp[i, j] = dp[i - 1, j] + down[i - 1][j]
            else:
                dp[i, j] = max(dp[i - 1, j] + down[i - 1][j], dp[i, j - 1] + right[i][j - 1])
    print(dp[n, m])


if __name__ == '__main__':
    main()
