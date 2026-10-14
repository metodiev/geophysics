"""Stratigraphic principles: relative-age constraints and graphic correlation.

Run:  .venv/bin/python 02-stratigraphic_principles_demo.py
Requires: NumPy.

Companion to lesson 04-03-02. Relative dating is a *deductive* system: from
superposition, original horizontality, cross-cutting relations, inclusions and
faunal succession you obtain a set of pairwise ordering constraints, and the
geological history is the set of total orders consistent with all of them. That
is a topological sort. When no such order exists the field observations
contradict each other, and the correct response is to re-examine the outcrop,
not to pick a convenient order.

This demo:

1. Takes a synthetic geological history (a known, constructed order of seven
   events), derives the field relations that this history would produce, and
   then solves for the order from the relations alone -- a round trip that
   verifies the solver rather than the input.
2. Injects one contradictory relation (the commonest field error: a fault that
   is recorded as both cutting and being cut by the same bed) and shows that
   the solver detects the cycle instead of returning a wrong answer.
3. Brackets the age of a fault between the youngest unit it cuts and the oldest
   unit that cuts it, which is the practical use of cross-cutting relations.
4. Performs a graphic correlation on three synthetic sections: it finds the
   taxon order that minimises sequence violations across all sections, reports
   the violation counts, and shows that one reworked specimen is detected as
   the single datum whose removal restores a perfect correlation.

All numeric inputs are labelled SYNTHETIC: they are constructed to exercise the
method, not measured. The geology they stand for is real; the numbers are not
data.
"""

from __future__ import annotations

import itertools

import numpy as np

# --------------------------------------------------------------------------
# 1. Field relations -> a consistent chronological order
# --------------------------------------------------------------------------

# SYNTHETIC history, youngest last.  The solver never sees this list; it is used
# only to check the answer.
TRUE_HISTORY = [
    "Sst-A",      # sandstone A, oldest
    "Sh-B",       # shale B
    "Lst-C",      # limestone C
    "Dike-D",     # dolerite dyke, intrudes A/B/C
    "Fault-F",    # normal fault, offsets A/B/C but not E
    "Sst-E",      # sandstone E, deposited on the fault scarp, unfaulted
    "Soil-G",     # youngest cover
]

# Field relations, each a pair (older, younger) as a field geologist reads them.
TRUE_RELATIONS = [
    ("Sst-A", "Sh-B"),    # superposition
    ("Sh-B", "Lst-C"),    # superposition
    ("Sst-A", "Dike-D"),  # cross-cutting: dyke cuts A
    ("Sh-B", "Dike-D"),
    ("Lst-C", "Dike-D"),
    ("Sst-A", "Fault-F"),  # fault cuts A
    ("Sh-B", "Fault-F"),
    ("Lst-C", "Fault-F"),
    ("Fault-F", "Sst-E"),  # E is deposited across the fault
    ("Sst-E", "Soil-G"),   # superposition
]

# The contradictory pair: recorded as both cutting and cut by Dike-D.
CONTRASTING_RELATIONS = TRUE_RELATIONS + [
    ("Soil-G", "Dike-D"),  # dike cuts the youngest soil -- possible ...
    ("Dike-D", "Soil-G"),  # ... and is also cut by it -- impossible together
]


def topological_orders(events: list[str], relations: list[tuple[str, str]]):
    """Return (all consistent orders, is_acyclic).

    A brute-force enumeration over permutations is used on purpose: with n = 7
    it is 5040 checks and it makes the *definition* of a consistent history
    visible -- an order is admissible when no relation is violated.
    """
    n = len(events)
    index = {name: i for i, name in enumerate(events)}
    relation_pairs = [(index[a], index[b]) for a, b in relations]
    admissible = []
    for order in itertools.permutations(range(n)):
        rank = [0] * n
        for position, item in enumerate(order):
            rank[item] = position
        if all(rank[a] < rank[b] for a, b in relation_pairs):
            admissible.append(tuple(order))
    return admissible, len(admissible) > 0


def report_order(events: list[str], admissible) -> None:
    names = [events[i] for i in admissible[0]]
    print("  one consistent order (oldest first):")
    for step, name in enumerate(names, start=1):
        print(f"    {step}. {name}")
    if len(admissible) > 1:
        partial = []
        for position in range(len(events)):
            candidates = {order[position] for order in admissible}
            if len(candidates) > 1:
                partial.append((position + 1,
                                sorted(events[i] for i in candidates)))
        print(f"  {len(admissible)} consistent orders exist, so the relations "
              f"constrain the history only partly:")
        for position, candidates in partial:
            print(f"    position {position} is any of: {', '.join(candidates)}")


def part_one() -> None:
    print()
    print("1. From field relations to a chronological order")
    print("-" * 62)
    admissible, ok = topological_orders(TRUE_HISTORY, TRUE_RELATIONS)
    print(f"  events: {len(TRUE_HISTORY)}, relations: {len(TRUE_RELATIONS)}, "
          f"consistent total orders: {len(admissible)} ({'acyclic' if ok else 'CYCLE'})")
    report_order(TRUE_HISTORY, admissible)

    recovered = [TRUE_HISTORY[i] for i in admissible[0]]
    print(f"  the recovered order equals the constructed history: "
          f"{recovered == TRUE_HISTORY}")

    print()
    print("  Now add the contradictory pair (Dike-D cuts Soil-G, and Soil-G "
          "cuts Dike-D):")
    bad, ok_bad = topological_orders(TRUE_HISTORY, CONTRASTING_RELATIONS)
    print(f"  consistent total orders: {len(bad)}; "
          f"solver verdict: {'a cycle is present' if not bad else 'no cycle'}")
    if not ok_bad:
        print("  A cycle means the two relations cannot both be true: one of "
              "them is a misreading, and the honest output is 'no consistent "
              "history', not the order that ignores one relation.")


# --------------------------------------------------------------------------
# 2. Cross-cutting relations as an age bracket
# --------------------------------------------------------------------------

def part_two() -> None:
    print()
    print("2. Bracketing the age of a fault by cross-cutting relations")
    print("-" * 62)
    cuts = ["Sst-A", "Sh-B", "Lst-C", "Dike-D"]      # fault offsets these
    does_not_cut = ["Sst-E", "Soil-G"]               # deposited after faulting
    print(f"  units offset by Fault-F:            {', '.join(cuts)}")
    print(f"  units that post-date faulting:      {', '.join(does_not_cut)}")
    print(f"  => Fault-F is younger than the youngest unit it cuts "
          f"({cuts[-1] if cuts else '--'})")
    print(f"  => Fault-F is older than the oldest unit that oversteps it "
          f"({does_not_cut[0] if does_not_cut else '--'})")
    print("  The bracket is as sharp as the stratigraphy allows: the age of the "
          "fault lies within the duration of the gap between those two units, "
          "which may be a single bed or an entire unconformity.")


# --------------------------------------------------------------------------
# 3. Graphic correlation: an order that minimises sequence violations
# --------------------------------------------------------------------------

TAXA = ["T1", "T2", "T3", "T4", "T5", "T6"]

# SYNTHETIC true order of first appearances (oldest first) and section offsets.
TRUE_FAD_ORDER = ["T1", "T2", "T3", "T4", "T5", "T6"]
# Synchronous levels, in metres above the base of each section's measured part.
BASE_LEVEL = {"T1": 4.0, "T2": 11.0, "T3": 19.0, "T4": 26.0, "T5": 38.0, "T6": 47.0}
# Per-section thickness scaling: a condensed vs an expanded section of the same
# interval.  No violation is introduced by a monotone rescaling.
SECTION_SCALE = {"AN": 1.00, "BD": 0.55, "CD": 1.35}

REWORKED = ("BD", "T4", 2.5)  # section, taxon, observed level (metres)


def observed_sections() -> dict[str, dict[str, float]]:
    sections: dict[str, dict[str, float]] = {}
    for section, scale in SECTION_SCALE.items():
        sections[section] = {t: BASE_LEVEL[t] * scale for t in TAXA}
    section, taxon, level = REWORKED
    sections[section][taxon] = level  # anomalously low: a reworked specimen
    return sections


def violations(order: list[str], sections: dict[str, dict[str, float]]) -> int:
    """Count pairs whose relative order disagrees between an arrangement and a section."""
    rank = {t: i for i, t in enumerate(order)}
    taxa = list(order)
    total = 0
    for _section, datums in sections.items():
        for a, b in itertools.combinations(taxa, 2):
            if (rank[a] - rank[b]) * (datums[a] - datums[b]) < 0:
                total += 1
    return total


def best_order(sections: dict[str, dict[str, float]]):
    best, best_v = None, None
    for perm in itertools.permutations(TAXA):
        v = violations(list(perm), sections)
        if best_v is None or v < best_v:
            best, best_v = list(perm), v
    return best, best_v


def part_three() -> None:
    print()
    print("3. Graphic correlation: an order that minimises sequence violations")
    print("-" * 62)
    sections = observed_sections()
    print(f"{'taxon':<7}{'true position (a.u.)':>22}"
          + "".join(f"{s:>10}" for s in SECTION_SCALE))
    for taxon in TAXA:
        row = "".join(f"{sections[s][taxon]:>10.2f}" for s in SECTION_SCALE)
        print(f"  {taxon:<5}{BASE_LEVEL[taxon]:>22.2f}{row}")
    print("  (true position is a synthetic synchronous level; section values are "
          "that level rescaled, plus the injected reworking)")

    truth = TRUE_FAD_ORDER
    print()
    print(f"  violations of the section data against the true order: "
          f"{violations(truth, sections)}")
    best, best_v = best_order(sections)
    print(f"  minimum achievable violations over all {len(list(itertools.permutations(TAXA)))} "
          f"arrangements: {best_v}, attained by {' '.join(best)}")
    print(f"  the minimum-violation arrangement equals the true order: "
          f"{best == truth}")
    print("  A non-zero minimum is the signature of a datum that is out of "
          "place: no arrangement can remove it.")

    # Remove the suspect datum and repeat, deciding which datum is suspect by a
    # leave-one-out test rather than by knowing the answer.
    print()
    print("  Leave-one-out test (which single datum, if removed, restores a "
          "zero-violation correlation?):")
    base_v = best_v
    for taxon in TAXA:
        reduced = {s: {t: v for t, v in datums.items() if t != taxon}
                   for s, datums in sections.items()}
        reduced_taxa = [t for t in TAXA if t != taxon]
        best_r, best_rv = None, None
        for perm in itertools.permutations(reduced_taxa):
            v = violations(list(perm), reduced)
            if best_rv is None or v < best_rv:
                best_r, best_rv = list(perm), v
        flag = ""
        if best_rv == 0 and base_v > 0:
            flag = "  <-- removing this datum gives a perfect correlation"
        print(f"    drop {taxon}: minimum violations = {best_rv}{flag}")
    print(f"  Injected reworking in the synthetic data: {REWORKED[0]} {REWORKED[1]} "
          f"at {REWORKED[2]} m.")


def main() -> None:
    print("=" * 74)
    print("Stratigraphic principles: relations, brackets and correlation")
    print("=" * 74)
    part_one()
    part_two()
    part_three()
    print()
    print("=" * 74)
    rng = np.random.default_rng(20261014)
    print("Determinism check: the solver enumerates permutations and uses no "
          "randomness;")
    print("this run's synthetic section data is fixed. A draw from the seeded "
          f"generator for reproducibility: {rng.integers(0, 10 ** 6)}")
    print("=" * 74)


if __name__ == "__main__":
    main()
