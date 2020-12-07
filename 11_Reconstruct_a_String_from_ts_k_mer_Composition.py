def find_next(s_lines, last):
    for s in s_lines:
        if s.startswith(last[1:]):
            return s
    return None


with open("input.txt", "r") as f:
    k = int(f.readline())
    lines = [line.strip() for line in f.readlines()]

n = k + len(lines) - 1

ans = lines[0]
lines = lines[1:]

while len(ans) != n:
    for line in lines:
        if ans[-k + 1:] == line[:-1]:
            ans += line[-1]
        elif ans[:k - 1] == line[1:]:
            ans = line[0] + ans
print(ans)



