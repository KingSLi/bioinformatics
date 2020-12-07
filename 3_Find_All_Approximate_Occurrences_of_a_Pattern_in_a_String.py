def mismatch(a, b):
    assert len(a) == len(b)
    cnt = 0
    for i in range(len(a)):
        cnt += a[i] != b[i]
    return cnt


pattern = input()
genom = input()
d = int(input())

n = len(pattern)
ans = []
for i in range(len(genom) - n + 1):
    if mismatch(pattern, genom[i:i + n]) <= d:
        ans.append(str(i))
print(" ".join(ans))
