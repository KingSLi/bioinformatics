import itertools
from collections import defaultdict
from tqdm import tqdm


def mismatch(a, b):
    assert len(a) == len(b)
    cnt = 0
    for i in range(len(a)):
        cnt += a[i] != b[i]
    return cnt


genom = input()
k, d = map(int, input().split())

patterns = set([''.join(pattern) for pattern in itertools.product("ACTG", repeat=k)])

frequency = defaultdict(int)
for i in tqdm(range(len(genom) - k + 1)):
    for pattern in patterns:
        if mismatch(pattern, genom[i:i + k]) <= d:
            frequency[pattern] += 1

max_value = max(frequency.values())
print(' '.join([key for key, value in frequency.items() if value == max_value]))