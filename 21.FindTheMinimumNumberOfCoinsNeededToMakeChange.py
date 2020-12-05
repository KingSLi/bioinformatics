import numpy as np
val = int(input())
coins = list(map(int, input().split(',')))

dp = np.zeros(val + 1, dtype=int)

for c in coins:
    if c < len(dp):
        dp[c] = 1
for i in range(1, val + 1):
    for coin in coins:
        if coin <= i:
            if dp[i - coin] == 0:
                continue
            dp[i] = (dp[i - coin] + 1) if (dp[i] == 0) else min(dp[i - coin] + 1, dp[i])

print(dp[val])

