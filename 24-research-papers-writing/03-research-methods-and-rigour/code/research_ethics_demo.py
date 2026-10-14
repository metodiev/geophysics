#!/usr/bin/env python3
"""Research ethics: text similarity across paraphrase levels and authorship credit.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_ethics_demo.py

Everything here is SYNTHETIC.  The text is a generated word sequence over a small
vocabulary, not prose from any source, and the contribution matrix is invented.
No real text is compared with anything.

Sections
--------
1. Text similarity as a function of paraphrase level.
2. Where a similarity threshold can and cannot separate copying from paraphrase.
3. Authorship criteria: how many contributors qualify under different rules.
4. Gift and ghost contributions: the arithmetic of an inflated author list.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_WORDS = 220
VOCAB = 90
SUBSTITUTION_LEVELS = (0.0, 0.05, 0.10, 0.20, 0.30, 0.50)
SHINGLE = 5
N_CONTRIBUTORS = 6
CRITERIA = 4               # ICMJE-style criteria, binary per contributor
P_CRITERION = ((0.95, 0.90, 0.80, 0.75),   # lead author
               (0.90, 0.85, 0.70, 0.60),   # second
               (0.85, 0.80, 0.60, 0.35),   # third
               (0.70, 0.55, 0.30, 0.20),   # fourth
               (0.55, 0.35, 0.15, 0.10),   # technician
               (0.25, 0.10, 0.05, 0.02))   # gift authorship candidate


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def shingles(words, k=SHINGLE):
    return {" ".join(words[i:i + k]) for i in range(len(words) - k + 1)}


def jaccard(a, b):
    return len(a & b) / len(a | b)


def cosine(a, b):
    keys = set(a) | set(b)
    va = np.array([a.get(k, 0) for k in keys], dtype=float)
    vb = np.array([b.get(k, 0) for k in keys], dtype=float)
    return float(va @ vb / (np.linalg.norm(va) * np.linalg.norm(vb)))


def main():
    section("1. Text similarity as a function of paraphrase level")
    source = [f"w{int(i)}" for i in RNG.integers(0, VOCAB, N_WORDS)]
    src_shingles = shingles(source)
    src_counts = {w: source.count(w) for w in set(source)}
    print(f"SYNTHETIC passage: {N_WORDS} words drawn from a {VOCAB}-word vocabulary")
    print(f"  {len(src_shingles)} {SHINGLE}-word shingles in the source")
    print("  substitution rate   shingle Jaccard   cosine similarity")
    for rate in SUBSTITUTION_LEVELS:
        text = [f"w{int(RNG.integers(0, VOCAB))}" if RNG.random() < rate else w
                for w in source]
        counts = {w: text.count(w) for w in set(text)}
        print(f"  {rate * 100:15.0f} %   {jaccard(src_shingles, shingles(text)):15.3f}   "
              f"{cosine(src_counts, counts):17.3f}")
    print("  -> the shingle measure collapses with substitution; the bag-of-words")
    print("     cosine barely moves, because word identity survives substitution.")
    print("     They detect different things: sequence reuse and vocabulary reuse.")

    section("2. Where a similarity threshold can and cannot separate")
    verbatim = source
    light = [f"w{int(RNG.integers(0, VOCAB))}" if RNG.random() < 0.10 else w
             for w in source]
    heavy = [f"w{int(RNG.integers(0, VOCAB))}" if RNG.random() < 0.30 else w
             for w in source]
    independent = [f"w{int(i)}" for i in RNG.integers(0, VOCAB, N_WORDS)]
    for label, text in (("verbatim copy", verbatim),
                        ("light paraphrase", light),
                        ("heavy paraphrase", heavy),
                        ("independent text", independent)):
        print(f"  {label:<20s} shingle Jaccard vs source = "
              f"{jaccard(src_shingles, shingles(text)):.3f}, "
              f"cosine = {cosine(src_counts, {w: text.count(w) for w in set(text)}):.3f}")
    print("  -> a threshold near 0.7 separates a copy from heavy paraphrase, and also")
    print("     separates heavy paraphrase from an independent text -- but the same")
    print("     threshold cannot distinguish a legitimate re-description of a standard")
    print("     method from reuse of a specific passage.  A score is a screen, not a")
    print("     finding; the finding requires reading the passage and its source.")

    section("3. Authorship criteria: how many contributors qualify")
    matrix = np.array([[RNG.random() < p for p in row] for row in P_CRITERION])
    met = matrix.sum(axis=1)
    print(f"SYNTHETIC contribution matrix: {N_CONTRIBUTORS} contributors x "
          f"{CRITERIA} criteria")
    print("  contributor   criteria met   all 4   >= 3   >= 2   >= 1")
    for i, row in enumerate(matrix):
        print(f"  {i + 1:11d}   {int(row.sum()):12d}   "
              f"{str(bool(row.all())):<7s} "
              f"{str(bool(row.sum() >= 3)):<6s} {str(bool(row.sum() >= 2)):<6s} "
              f"{str(bool(row.sum() >= 1)):<6s}")
    counts = {k: int(np.sum(met >= k)) for k in range(1, CRITERIA + 1)}
    print(f"  authors under 'any contribution' (>= 1 criterion)   = {counts[1]}")
    print(f"  authors under a '>= 2 criteria' rule                = {counts[2]}")
    print(f"  authors under a '>= 3 criteria' rule                = {counts[3]}")
    print(f"  authors under 'all 4 criteria'                      = {counts[4]}")
    print("  -> the author list is a threshold choice, and the same six people give")
    print("     four different lists.  State the rule and apply it to everyone.")

    section("4. Gift and ghost contributions: the arithmetic of an inflated list")
    rule = 3
    listed = met >= rule
    ghosts = (met >= 2) & ~listed
    print(f"  stated rule: a contributor is an author if they meet >= {rule} criteria")
    print(f"  authors listed = {int(listed.sum())}, "
          f"ghosts (real contribution, not listed) = {int(ghosts.sum())}, "
          f"people with < 1 criterion who are contributors = "
          f"{int(np.sum(met < 1))}")
    scenes = {
        "stated rule (>= 3)": met[listed],
        "plus one gift author (0 criteria)": np.append(met[listed], 0.0),
        "loosest rule (>= 1)": met[met >= 1],
        "stated rule, strongest contributor omitted": np.delete(
            met[listed], int(np.argmax(met[listed]))),
    }
    for label, values in scenes.items():
        print(f"  {label:<40s} list size {values.size:2d}, "
              f"mean criteria per author {values.mean():.2f}")
    print("  -> each addition to the list lowers the mean credit per author, and each")
    print("     omission raises it for the rest: authorship is zero-sum in that sense.")
    print("     A stated criterion applied uniformly is the only defensible rule.")


if __name__ == "__main__":
    main()
