def to_rna(dna):
    return dna.replace('T', 'U')


def reverse_dna(dna):
    reverting_map = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return ''.join([reverting_map[base] for base in dna])[::-1]


codon2protein = {}
with open("codon2protein", "r") as f:
    for line in f.readlines():
        k, v = line.strip().split(' ')
        codon2protein[k] = v


def to_peptid(dna):
    res = []
    for i in range(0, len(dna), 3):
        protein = codon2protein[dna[i:i + 3]]
        if protein == '-':
            break
        res.append(protein)
    return "".join(res)


dna = input()
peptid = input()

window_len = len(peptid)

ans = []
for i in range(len(dna) - 3 * window_len + 1):
    sub_dna = dna[i: i + 3 * window_len]
    rev_dna = reverse_dna(sub_dna)

    sub_peptid = to_peptid(to_rna(sub_dna))
    rev_peptid = to_peptid(to_rna(rev_dna))

    if peptid == sub_peptid or peptid == rev_peptid:
        ans.append(sub_dna)

for s in ans:
    print(s)
