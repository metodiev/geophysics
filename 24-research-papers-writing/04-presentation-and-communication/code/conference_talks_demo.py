#!/usr/bin/env python3
"""Conference talks: the word budget, the slide budget and what survives.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python conference_talks_demo.py

Everything here is SYNTHETIC.  The speaking rate, section allocation, slide timing
and recall model are chosen teaching values; no talk was recorded or measured.

Sections
--------
1. The word budget of a 12-minute talk.
2. Allocation across the four sections of the argument.
3. Slides: count, timing and density.
4. What the audience takes away, and what overrunning costs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
TALK_MINUTES = 12.0
SPEAKING_RATE = 130.0        # words per minute, deliberate delivery
ALLOCATION = {"motivation": 0.15, "method": 0.30, "results": 0.40, "conclusion": 0.15}
MIN_PER_SLIDE = 1.5
MAX_VISIBLE_WORDS = 20
QUESTION_MINUTES = 3.0
MIN_PER_QUESTION = 2.0
AUDIENCE_CAPACITY = 4.0      # ideas an audience retains from one talk
IDEAS = (3, 6, 9, 12, 18)
OVERRUN_MINUTES = 2.0


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. The word budget of a 12-minute talk")
    words = TALK_MINUTES * SPEAKING_RATE
    print(f"SYNTHETIC talk: {TALK_MINUTES:.0f} min at {SPEAKING_RATE:.0f} words/min "
          f"(deliberate pace, not conversational)")
    print(f"  total spoken words = {words:.0f}")
    print(f"  words per minute if you speak fast (170) = "
          f"{TALK_MINUTES * 170:.0f}; at 110 words/min = "
          f"{TALK_MINUTES * 110:.0f}")
    print(f"  a written page of 500 words = {words / 500:.1f} pages read aloud")
    print(f"  question time reserved = {QUESTION_MINUTES:.0f} min, i.e. "
          f"{QUESTION_MINUTES / MIN_PER_QUESTION:.1f} questions at "
          f"{MIN_PER_QUESTION:.0f} min each")
    print(f"  -> {words / 500:.1f} written pages of prose, delivered aloud: the talk is")
    print("     a selection from the paper, not a reading of it.")

    section("2. Allocation across the four sections of the argument")
    print(f"  section        share   words   minutes")
    for name, share in ALLOCATION.items():
        print(f"  {name:<13s} {share * 100:5.0f} % {words * share:7.0f} "
              f"{TALK_MINUTES * share:8.1f}")
    print(f"  checksum: shares sum to {sum(ALLOCATION.values()):.2f}, "
          f"words sum to {words:.0f}")
    print(f"  the results section gets {TALK_MINUTES * ALLOCATION['results']:.1f} min "
          f"= {words * ALLOCATION['results']:.0f} words")
    print("  -> choose the number of results that fit that budget before writing the")
    print("     slides: typically one primary result and at most two supporting ones.")

    section("3. Slides: count, timing and density")
    n_slides = TALK_MINUTES / MIN_PER_SLIDE
    print(f"  at {MIN_PER_SLIDE:.1f} min per slide the budget is {n_slides:.1f} slides")
    for slides in (8, 10, 12, 20, 30):
        print(f"  {slides:2d} slides -> {TALK_MINUTES * 60 / slides:5.1f} s per slide, "
              f"about {TALK_MINUTES * SPEAKING_RATE / slides:5.0f} spoken words each")
    print(f"  visible-word ceiling of {MAX_VISIBLE_WORDS} words per slide means an "
          f"{n_slides:.0f}-slide deck shows at most "
          f"{n_slides * MAX_VISIBLE_WORDS:.0f} words, vs {words:.0f} spoken ones")
    print(f"  ratio of spoken to displayed words = "
          f"{words / (n_slides * MAX_VISIBLE_WORDS):.1f}x")
    print("  -> slides carry the evidence and the structure; the speaker carries the")
    print("     argument.  A slide that repeats the speech wastes the channel.")

    section("4. What the audience takes away, and what overrunning costs")
    print(f"  audience capacity modelled as {AUDIENCE_CAPACITY:.0f} retained ideas")
    for ideas in IDEAS:
        recall = min(1.0, AUDIENCE_CAPACITY / ideas)
        print(f"  {ideas:2d} distinct ideas delivered -> "
              f"{recall * 100:5.1f} % retained "
              f"({min(AUDIENCE_CAPACITY, ideas):.0f} of {ideas})")
    print(f"  time overrun scenario: running {OVERRUN_MINUTES:.0f} min over means "
          f"cutting {OVERRUN_MINUTES * SPEAKING_RATE:.0f} spoken words and about "
          f"{OVERRUN_MINUTES / MIN_PER_SLIDE:.1f} slides on the fly")
    print(f"  at {n_slides:.0f} slides in {TALK_MINUTES:.0f} min, a 2-minute overrun "
          f"costs {OVERRUN_MINUTES / TALK_MINUTES * 100:.0f} % of the argument")
    print("  -> prepare the cut in advance: mark three slides as optional and rehearse")
    print("     the talk without them, so the overrun removes a planned piece.")


if __name__ == "__main__":
    main()
