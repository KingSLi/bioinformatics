import numpy as np
from tqdm import tqdm
import random
import itertools


def MakeProfileWithPseudoCounts(motifs):
    profile = {
        symb: [
            ([motif[column] for motif in motifs].count(symb) * 1.0 + 1) / len(motifs)
            for column in range(len(motifs[0]))]
        for symb in 'ACTG'
    }
    return profile


def GetProbability(pattern, profile):
    prob = 1.
    for i, c in enumerate(pattern):
        prob *= profile[c][i]
    return prob


def GetMostProbableFromProfile(motif, len_, profile):
    probs = [GetProbability(motif[i: i + len_], profile) for i in range(len(motif) - len_ + 1)]
    iter = np.argmax(probs)
    return motif[iter: iter + len_]


def Consensus(motifs):
    profile = {
        symb: [
            [motif[column] for motif in motifs].count(symb)
            for column in range(len(motifs[0]))]
        for symb in 'ACTG'
    }
    ans = []
    for i in range(len(motifs[0])):
        _, k = max([(v[i], k) for k, v in profile.items()])
        ans.append(k)
    return "".join(ans)


def HammingDistance(a, b):
    return sum([a[i] != b[i] for i in range(len(a))])


def Score(motifs):
    consensus = Consensus(motifs)
    score = sum([HammingDistance(consensus, motif) for motif in motifs])
    return round(score, 4)


def MakeMotifsFromProfile(dna, profile, k):
    motifs = [GetMostProbableFromProfile(line, k, profile) for line in dna]
    return motifs


def GetRandomKMer(s, k):
    i = random.randint(0, len(s) - k)
    return s[i:i + k]


def GetGibbsMostProbable(motif, len_, profile):
    probs = [GetProbability(motif[i: i + len_], profile) for i in range(len(motif) - len_ + 1)]
    sum_all_probs = sum(probs)
    probs = [p / sum_all_probs for p in probs]
    accum_brobs = list(itertools.accumulate(probs))
    dies = random.random()
    for i, prob in enumerate(accum_brobs):
        if dies < prob:
            return motif[i: i + len_]


def GibbsSampler(dna, k, t, N):
    motifs = [GetRandomKMer(line, k) for line in dna]
    bestScore = 100000000000
    bestMotifs = motifs
    for _ in range(N):
        i_to_remove = random.randint(0, t - 1)
        profile = MakeProfileWithPseudoCounts(motifs[:i_to_remove] + motifs[i_to_remove + 1:])
        motif = GetGibbsMostProbable(dna[i_to_remove], k, profile)
        motifs = motifs[:i_to_remove] + [motif] + motifs[i_to_remove + 1:]
        score = Score(motifs)
        if score < bestScore:
            bestScore = score
            bestMotifs = motifs.copy()
    return bestMotifs


def main():
    k, t, N = map(int, input().split())
    DNA = []
    for _ in range(t):
        DNA.append(input())

    bestScore = 100000000000
    bestMotifs = None
    for _ in tqdm(range(20)):
        motifs = GibbsSampler(DNA, k, t, N)
        score = Score(motifs)
        if score < bestScore:
            bestMotifs = motifs
            bestScore = score

    for s in bestMotifs:
        print(s)


if __name__ == '__main__':
    main()
