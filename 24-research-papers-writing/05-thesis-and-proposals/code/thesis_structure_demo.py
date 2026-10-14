#!/usr/bin/env python3
"""Thesis structure: chapter budgets, redundancy and the contribution statement.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thesis_structure_demo.py

Everything here is SYNTHETIC.  Chapter lengths, overlap fractions, publication
status and writing rates are chosen teaching values; no thesis was measured.

Sections
--------
1. The chapter word budget against a page limit.
2. Redundancy: how much of the thesis is repeated material.
3. The contribution statement: is each claim supported by words somewhere?
4. Time: the writing budget in weeks.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
CHAPTERS = (
    ("1 Introduction", 7000, 0.05),
    ("2 Setting and data", 9000, 0.15),
    ("3 Method", 12000, 0.30),
    ("4 Result one", 10000, 0.12),
    ("5 Result two", 11000, 0.22),
    ("6 Synthesis and discussion", 10000, 0.18),
    ("7 Conclusions", 4000, 0.10),
    ("Appendices", 6000, 0.00),
)
WORDS_PER_PAGE = 400
PAGE_LIMIT = 160
P_PUBLISHED_CHAPTER = 0.40
CONTRIBUTIONS = (
    ("a new processing chain", (2, 3, 4)),
    ("the first regional velocity model", (4, 5)),
    ("a quantified uncertainty budget", (3, 5)),
    ("an open dataset and code", (2,)),
    ("a revised tectonic interpretation", (5, 6)),
    ("a methodological recommendation", (7,)),
)
SUPPORT_THRESHOLD = 15000
WORDS_PER_DAY = 450.0


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. The chapter word budget against a page limit")
    total = sum(words for _, words, _ in CHAPTERS)
    print(f"SYNTHETIC thesis: {len(CHAPTERS)} chapters, "
          f"{total} words, {WORDS_PER_PAGE} words per page, "
          f"limit {PAGE_LIMIT} pages")
    print("  chapter                     words   share   pages   cumulative pages")
    cumulative = 0.0
    for name, words, _ in CHAPTERS:
        pages = words / WORDS_PER_PAGE
        cumulative += pages
        print(f"  {name:<24s} {words:6d} {words / total * 100:6.1f} % "
              f"{pages:6.0f} {cumulative:17.0f}")
    print(f"  total = {total} words = {total / WORDS_PER_PAGE:.0f} pages "
          f"against a limit of {PAGE_LIMIT}")
    over = total / WORDS_PER_PAGE - PAGE_LIMIT
    print(f"  {'over' if over > 0 else 'under'} the limit by {abs(over):.0f} pages "
          f"({abs(over) / PAGE_LIMIT * 100:.0f} % of the limit)")
    print(f"  words to cut to fit the limit = "
          f"{max(0.0, total - PAGE_LIMIT * WORDS_PER_PAGE):.0f}")
    print("  -> the cut should come from the chapters with the highest overlap, not")
    print("     evenly: evenly distributed cuts cost every chapter its clearest prose.")

    section("2. Redundancy: how much of the thesis is repeated material")
    redundancy = 0.0
    for i in range(len(CHAPTERS) - 1):
        words_next = CHAPTERS[i + 1][1]
        overlap = CHAPTERS[i][2]
        repeated = overlap * words_next
        redundancy += repeated
        print(f"  {CHAPTERS[i][0]:<24s} -> {CHAPTERS[i + 1][0]:<24s} "
              f"overlap {overlap * 100:4.0f} % of the following chapter "
              f"= {repeated:6.0f} words")
    print(f"  total repeated words = {redundancy:.0f} "
          f"({redundancy / total * 100:.1f} % of the thesis)")
    print(f"  published fraction of chapters = {P_PUBLISHED_CHAPTER * 100:.0f} % "
          f"(a chosen value, not measured)")
    print(f"  if a third of the overlap sits in published chapters, the duplicative")
    print(f"  material already in print is about {redundancy / 3:.0f} words")
    print("  -> a thesis is allowed to be redundant across chapters, but the redundancy")
    print("     must be by reference, not by repetition: 'as described in chapter 3'.")

    section("3. The contribution statement: is each claim supported?")
    chapter_words = {name: words for name, words, _ in CHAPTERS}
    print("  claimed contribution                 supporting chapters   words")
    supported = 0
    for claim, chapters in CONTRIBUTIONS:
        words = sum(chapter_words[CHAPTERS[c - 1][0]] for c in chapters
                    if 1 <= c <= len(CHAPTERS))
        ok = words >= SUPPORT_THRESHOLD
        supported += int(ok)
        print(f"  {claim:<36s} {str(chapters):<21s} {words:5d} "
              f"{'ok' if ok else 'thin'}")
    print(f"  contributions with at least {SUPPORT_THRESHOLD} supporting words = "
          f"{supported} of {len(CONTRIBUTIONS)}")
    print(f"  contributions mapped to a single chapter = "
          f"{sum(1 for _, c in CONTRIBUTIONS if len(c) == 1)}")
    print("  -> a claim supported by one chapter is a chapter result, not a thesis")
    print("     contribution; the synthesis chapter is what turns results into a claim.")

    section("4. Time: the writing budget in weeks")
    days = total / WORDS_PER_DAY
    print(f"  net new words (after removing {redundancy:.0f} repeated) = "
          f"{total - redundancy:.0f}")
    print(f"  at {WORDS_PER_DAY:.0f} words per day that is "
          f"{(total - redundancy) / WORDS_PER_DAY:.0f} writing days")
    print(f"  as weeks at 5 days per week = "
          f"{(total - redundancy) / WORDS_PER_DAY / 5:.1f} weeks of full-time writing")
    print("  revision multiplies this: the lesson on editing measures a 23 % cut")
    print("  over three passes, which is roughly 9 h for a 6200-word draft")
    print("  -> the writing is not the long pole; the analysis and the revision are.")


if __name__ == "__main__":
    main()
