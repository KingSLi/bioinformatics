import numpy as np
import operator


def MakeProfile(motifs):
    profile = {
        symb: [
            [motif[column] for motif in motifs].count(symb) * 1.0 / len(motifs)
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


def GreedyMotifSearch(dna, k, t):
    assert(len(dna) > 0)
    bestMotifs = [s[:k] for s in dna]
    n = len(dna[0])
    bestScore = 1000000000
    for i in range(n - k + 1):
        kmer = dna[0][i: i + k]
        motifs = [kmer]
        for j in range(1, t):
            profile = MakeProfile(motifs)
            most_probable_motif = GetMostProbableFromProfile(dna[j], k, profile)
            motifs.append(most_probable_motif)
        score = Score(motifs)
        if score < bestScore:
            bestScore = score
            bestMotifs = motifs
    return bestMotifs


def main():
    k, t = map(int, input().split())
    # t = int(input())
    DNA = []
    for _ in range(t):
        DNA.append(input())

    result = GreedyMotifSearch(DNA, k, t)
    for s in result:
        print(s)

    # prof = MakeProfile(DNA)
    # print(Consensus(DNA))


if __name__ == '__main__':
    main()
