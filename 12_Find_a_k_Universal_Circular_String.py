def calc(t, p, sequence, info):
    if t > n:
        if n % p == 0:
            sequence.extend(info[1: p + 1])
    else:
        info[t] = info[t - p]
        calc(t + 1, p, sequence, info)
        for j in range(info[t - p] + 1, 2):
            info[t] = j
            calc(t + 1, t, sequence, info)


def de_brejn(n):
    alphabet = ["0", "1"]
    info = [0] * n * 2
    sequence = []
    calc(1, 1, sequence, info)
    return "".join(alphabet[i] for i in sequence)


n = int(input())
print(de_brejn(n))
