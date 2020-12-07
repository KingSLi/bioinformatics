import numpy as np
from tqdm import tqdm
import random


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


def RandomizedMotifSearch(dna, k, t):
    bestMotifs = [GetRandomKMer(line, k) for line in dna]
    bestScore = 10000000000
    while True:
        profile = MakeProfileWithPseudoCounts(bestMotifs)
        motifs = MakeMotifsFromProfile(dna, profile, k)
        score = Score(motifs)
        if score < bestScore:
            bestScore = score
            bestMotifs = motifs
        else:
            break
    return bestMotifs


def main():
    k, t = map(int, input().split())
    DNA = []
    for _ in range(t):
        DNA.append(input())
    bestScore = 1000000000
    bestMotifs = None
    for _ in tqdm(range(10000)):
        motifs = RandomizedMotifSearch(DNA, k, t)
        if Score(motifs) < bestScore:
            bestMotifs = motifs
            bestScore = Score(motifs)

    for s in bestMotifs:
        print(s)


if __name__ == '__main__':
    main()
