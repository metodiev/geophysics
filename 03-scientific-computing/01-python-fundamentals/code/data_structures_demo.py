"""Lists, tuples, dictionaries, sets and the cost of getting the wrong one.

Run:  python3 data_structures_demo.py
Requires: Python standard library only.

Companion to lesson 03-01-05.  The lesson's claim is blunt: the choice of
container decides whether a processing script finishes or not.  This demo
measures that claim on realistic-looking synthetic survey bookkeeping.

Demonstrates:

1. Lookup: list scan O(n) versus dictionary O(1), measured.
2. Membership: list versus set versus dict, measured.
3. Duplicate detection: nested loop O(n^2) versus set O(n), measured.
4. Tuples as immutable records, namedtuple for readability, sorting by key.
5. Counting with collections.Counter, and grouping with a dict of lists.
6. A size table so the asymptotic talk is anchored to real bytes.
"""

import random
import sys
import time
from collections import Counter, defaultdict, namedtuple

N_STATIONS = 2_000
N_LOOKUPS = 20_000
N_DUPLICATES = 3_000
SEED = 20261014


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def build_survey():
    """Return (names, elevations, name_to_elevation) for a synthetic survey."""
    rng = random.Random(SEED)          # seeded: the whole demo is reproducible
    names = [f"STA{i:05d}" for i in range(N_STATIONS)]
    elevations = [100.0 + 40.0 * rng.random() for _ in range(N_STATIONS)]
    lookup = dict(zip(names, elevations))
    return names, elevations, lookup


def part1_lookup():
    section("1. Station lookup: list scan versus dictionary")
    names, elevations, lookup = build_survey()
    rng = random.Random(SEED + 1)
    probes = [rng.randrange(N_STATIONS) for _ in range(N_LOOKUPS)]

    start = time.perf_counter()
    total = 0.0
    for index in probes:
        target = names[index]
        for name, elevation in zip(names, elevations):   # O(n) scan
            if name == target:
                total += elevation
                break
    t_list = time.perf_counter() - start

    start = time.perf_counter()
    total2 = 0.0
    for index in probes:
        total2 += lookup[names[index]]                   # O(1) hash lookup
    t_dict = time.perf_counter() - start

    print(f"  stations           : {N_STATIONS:,}")
    print(f"  lookups            : {N_LOOKUPS:,}")
    print(f"  list scan (O(n))   : {t_list:.4f} s"
          f"  = {t_list / N_LOOKUPS * 1e6:8.2f} us per lookup")
    print(f"  dict lookup (O(1)) : {t_dict:.4f} s"
          f"  = {t_dict / N_LOOKUPS * 1e6:8.2f} us per lookup")
    print(f"  speed-up           : {t_list / t_dict:.0f}x")
    print(f"  identical totals   : {abs(total - total2) < 1e-9}")
    print()
    print(f"  The list scan compares against about {N_STATIONS / 2:,.0f} names on")
    print("  average.  At 10^5 samples the same code is not slower, it is")
    print("  unusable: 10^5 lookups into a 10^5 list is 5x10^9 comparisons.")


def part2_membership():
    section("2. Membership: 'in' on a list, a set and a dict")
    names, _elevations, lookup = build_survey()
    name_set = set(names)
    probe = names[N_STATIONS - 1]           # worst case for the list
    repeats = 200

    start = time.perf_counter()
    for _ in range(repeats):
        hit = probe in names
    t_list = time.perf_counter() - start
    start = time.perf_counter()
    for _ in range(repeats):
        hit_set = probe in name_set
    t_set = time.perf_counter() - start
    start = time.perf_counter()
    for _ in range(repeats):
        hit_dict = probe in lookup
    t_dict = time.perf_counter() - start
    print(f"  {repeats} membership tests for the LAST station in the list")
    print(f"  list : {t_list * 1e6:9.2f} us total  ({hit})")
    print(f"  set  : {t_set * 1e6:9.2f} us total  ({hit_set})")
    print(f"  dict : {t_dict * 1e6:9.2f} us total  ({hit_dict})")
    print(f"  list/set ratio: {t_list / t_set:.0f}x")
    print()
    print("  A set is a dictionary without values: same hash table, same O(1)")
    print("  membership.  If you are about to write 'while x in my_list', stop")
    print("  and build a set once.")


def part3_duplicates():
    section("3. Duplicate detection: O(n^2) versus O(n)")
    rng = random.Random(SEED + 2)
    codes = [f"STA{rng.randrange(N_DUPLICATES // 2):05d}"
             for _ in range(N_DUPLICATES)]
    print(f"  catalogue size: {len(codes):,} station codes,")
    print(f"  drawn from only {N_DUPLICATES // 2:,} distinct codes, so there are")
    print("  many repeats by construction (such repeats are data errors).")
    print("  Both versions below do the SAME complete job: count every repeat.")
    print()

    start = time.perf_counter()
    quadratic_pairs = 0
    for i in range(len(codes)):
        for j in range(i + 1, len(codes)):
            if codes[i] == codes[j]:
                quadratic_pairs += 1
    t_quad = time.perf_counter() - start

    start = time.perf_counter()
    occurrences = Counter()
    for code in codes:
        occurrences[code] += 1
    linear_pairs = sum(k * (k - 1) // 2 for k in occurrences.values())
    t_lin = time.perf_counter() - start

    print(f"  comparisons (n*(n-1)/2): {N_DUPLICATES * (N_DUPLICATES - 1) // 2:,}")
    print(f"  nested loops (O(n^2)): {t_quad * 1e3:9.3f} ms"
          f"   duplicate pairs: {quadratic_pairs:,}")
    print(f"  set + Counter (O(n)) : {t_lin * 1e3:9.3f} ms"
          f"   duplicate pairs: {linear_pairs:,}")
    print(f"  identical answers    : {quadratic_pairs == linear_pairs}")
    print(f"  speed-up             : {t_quad / t_lin:.0f}x")
    print()
    print("  A set alone answers 'is there a repeat?' but not 'how many pairs?'.")
    print("  Counting occurrences in one pass, then combining the counts, gives")
    print("  the same number as the nested loops.")
    print()
    counts = Counter(codes)
    print(f"  Counter: {len(counts):,} distinct codes; the three most frequent:")
    for code, n in counts.most_common(3):
        print(f"    {code}: {n} occurrences")
    print()
    print("  This is a *scaling* argument, not a micro-optimisation.  The")
    print(f"  quadratic version performs {N_DUPLICATES * (N_DUPLICATES - 1) // 2:,} comparisons at")
    print(f"  n = {N_DUPLICATES:,}; the set version performs {N_DUPLICATES:,} hash probes.")
    print("  Raising n to 10^5 multiplies the pair count by about 1111, so the")
    print(f"  measured {t_quad * 1e3:.0f} ms becomes roughly {t_quad * 1111:.0f} s - and the set version")
    print("  still finishes in milliseconds.  There is no constant-factor rescue")
    print("  for the wrong container.")


def part4_tuples():
    section("4. Tuples, namedtuples and sorting records")
    raw = [("STA01", 112.4, 0.31), ("STA02", 118.9, 0.27), ("STA03", 121.7, 0.29)]
    print(f"  plain tuples      : {raw}")
    print(f"  unpack in a loop  : ", end="")
    for code, elevation, anomaly in raw:
        print(f"{code}={anomaly}", end="  ")
    print()
    Station = namedtuple("Station", "code elevation anomaly")
    records = [Station(*row) for row in raw]
    print(f"  namedtuple        : {records[0]}")
    print(f"  attribute access  : records[0].anomaly = {records[0].anomaly}")
    ordered = tuple(sorted(records, key=lambda r: -r.anomaly))
    print(f"  sorted by anomaly : {[r.code for r in ordered]}")
    print()
    print("  A tuple is immutable and hashable, so it can be a dictionary key or")
    print("  a set member; a list cannot.  namedtuple keeps that property and")
    print("  adds readable field names without the cost of a class.")


def part5_grouping():
    section("5. Grouping: a dict of lists, then a dict of sums")
    readings = [("L1", 110.0), ("L2", 95.0), ("L1", 240.0),
                ("L2", 260.0), ("L1", 5.0), ("L2", 12.0)]
    grouped = defaultdict(list)
    for line, height in readings:
        grouped[line].append(height)
    print(f"  defaultdict(list): {dict(grouped)}")
    sums = defaultdict(float)
    for line, height in readings:
        sums[line] += height
    print(f"  running sums     : {dict(sums)}")
    print(f"  mean per line    : "
          f"{ {k: round(v / len(grouped[k]), 2) for k, v in sums.items()} }")
    print()
    print("  defaultdict removes the 'if key not in d' boilerplate without")
    print("  changing the O(n) character.  This is the manual version of the")
    print("  group-by that module 03-04 does in one line.")


def part6_sizes():
    section("6. Sizes in real bytes, so the asymptotics have units")
    n = 100_000
    a_list = [0.0] * n
    a_dict = {i: 0.0 for i in range(n)}
    a_set = set(range(n))
    a_tuple = tuple(a_list)
    print(f"  {n:,} elements")
    print(f"  list   of float : {sys.getsizeof(a_list):>12,} bytes"
          f"  ({sys.getsizeof(a_list) / n:.1f} B/element)")
    print(f"  tuple  of float : {sys.getsizeof(a_tuple):>12,} bytes"
          f"  ({sys.getsizeof(a_tuple) / n:.1f} B/element)")
    print(f"  dict   int->float: {sys.getsizeof(a_dict):>11,} bytes"
          f"  ({sys.getsizeof(a_dict) / n:.1f} B/element)")
    print(f"  set    of int   : {sys.getsizeof(a_set):>12,} bytes"
          f"  ({sys.getsizeof(a_set) / n:.1f} B/element)")
    print()
    print("  A list stores pointers, so the 8 bytes per element is the pointer,")
    print("  not the double.  A dict and a set trade memory for O(1) lookup -")
    print("  and that is the only reason to prefer them.")


if __name__ == "__main__":
    part1_lookup()
    part2_membership()
    part3_duplicates()
    part4_tuples()
    part5_grouping()
    part6_sizes()
