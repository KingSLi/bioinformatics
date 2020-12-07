mass = set()
with open("mass_table", "r") as f:
    for line in f.readlines():
        _, v = line.strip().split('   ')
        mass.add(int(v))

m = int(input())

dp = [0 for _ in range(m + 1)]
dp[0] = 1
for sum in range(m + 1):
    for mas in mass:
        if sum + mas <= m:
            dp[sum + mas] += dp[sum]

print(dp[m])

