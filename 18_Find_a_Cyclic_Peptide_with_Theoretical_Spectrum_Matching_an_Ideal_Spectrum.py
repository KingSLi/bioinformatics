import itertools


mass_table = []
with open("mass_table", "r") as f:
    for line in f.readlines():
        _, v = line.strip().split('   ')
        mass_table.append(int(v))


def expand(peptides):
    new_peptides = []
    for peptide in peptides:
        for m in mass_table:
            new_peptides.append(peptide + [m])
    return new_peptides


def Mass(peptide):
    return sum(peptide)


def ParentMass(spectrum):
    return spectrum[-1]


def CycloSpectrum(peptide):
    n = len(peptide)
    mass = Mass(peptide)
    spectrum = [0, mass]
    peptide.append(peptide[0])
    for i in range(1, n):
        for j in range(n):
            spectrum.append(Mass(peptide[j:j + i]))
    spectrum.sort()
    return spectrum


def LinearSpectrum(peptide):
    n = len(peptide)
    cum_sum = [0] + list(itertools.accumulate(peptide))
    lin_spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            lin_spectrum.append(cum_sum[j] - cum_sum[i])
    lin_spectrum.sort()
    return lin_spectrum


def InConsistent(peptide, spectrum):
    if Mass(peptide) > ParentMass(spectrum) - mass_table[0]:
        return True
    spec = LinearSpectrum(peptide)
    for mass in spec:
        if mass not in spectrum:
            return True
    return False


spectrum = list(map(int, input().split()))
peptides = [[]]
ans = []
while len(peptides) > 0:
    peptides = expand(peptides)
    for peptide in peptides.copy():
        if Mass(peptide) == ParentMass(spectrum):
            if CycloSpectrum(peptide) == spectrum:
                ans.append(peptide)
            peptides.remove(peptide)
        elif InConsistent(peptide, spectrum):
            peptides.remove(peptide)

print(' '.join(['-'.join(map(str, x)) for x in ans]))
