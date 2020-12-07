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
    peptide_copy = peptide + peptide
    for i in range(1, n):
        for j in range(n):
            spectrum.append(Mass(peptide_copy[j:j + i]))
    spectrum.sort()
    return spectrum


def Score(peptide, spectrum):
    cyclospectrum = CycloSpectrum(peptide)
    score = 0
    spectrum_copy = spectrum.copy()
    for spec in cyclospectrum:
        if spec in spectrum_copy:
            score += 1
            spectrum_copy.remove(spec)
        elif spec > ParentMass(spectrum):
            return 0
    return score


def Cut(leaderboard, spectrum, N):
    n = len(leaderboard)
    if n <= N:
        return leaderboard

    scores = [Score(x, spectrum) for x in leaderboard]
    border_score = sorted(scores)[-N]
    new_leaderboard = []
    for i in range(n):
        if scores[i] > 0 and scores[i] >= border_score:
            new_leaderboard.append(leaderboard[i])
    return new_leaderboard


def LeaderboardCyclopeptideSequencing(spectrum, N):
    leader_bord = [[]]
    leader_peptide = []
    while len(leader_bord) > 0:
        leader_bord = expand(leader_bord)
        for peptide in leader_bord:
            if Mass(peptide) == ParentMass(spectrum):
                if Score(peptide, spectrum) > Score(leader_peptide, spectrum):
                    leader_peptide = peptide.copy()
            elif Mass(peptide) > ParentMass(spectrum):
                leader_bord.remove(peptide)
        leader_bord = Cut(leader_bord, spectrum, N)
        # print(leader_bord)
    return leader_peptide


n = int(input())
spectrum = list(map(int, input().split()))

ans = LeaderboardCyclopeptideSequencing(spectrum, n)
print('-'.join(map(str, ans)))
