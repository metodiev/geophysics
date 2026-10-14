# Solutions — 24-04-01 Conference Talks

> Read after attempting. Numbers computed. Lesson:
> [01 Conference Talks](../01-conference-talks.md).

---

## ★1 — Spoken word budget

Available speaking time $= 15 - 3 = 12$ minutes.

$$12\ \mathrm{min} \times 140\ \mathrm{words/min} = 1680\ \mathrm{words}.$$

That is $3.4$ pages of $500$ words — about four times an abstract, delivered with no
charts. The budget is small, which is why the selection of results is the real work.

---

## ★2 — Allocation

| Section | Share | Words | Minutes |
|---|---|---|---|
| Motivation | $15\%$ | $252$ | $1.8$ |
| Method | $30\%$ | $504$ | $3.6$ |
| Results | $40\%$ | $672$ | $4.8$ |
| Conclusion | $15\%$ | $252$ | $1.8$ |

Check: $252 + 504 + 672 + 252 = 1680$ words ✔ and $1.8 + 3.6 + 4.8 + 1.8 = 12$
minutes ✔. The results budget of $4.8$ minutes fits one primary result explained
properly and at most two supporting results.

---

## ★3 — Slides for a $10$-minute talk

$$N_{\text{slides}} = \frac{10}{1.5} = 6.7 \approx 7\ \text{slides},$$
$$\text{spoken words per slide} = \frac{10 \times 130}{6.7} = 195\ \text{words}.$$

At a visible-word ceiling of $20$, a $7$-slide deck shows $140$ words against $1300$
spoken ones — a ratio of $9.3$, close to the lesson's $9.8$. If your deck has $20$
slides for a $10$-minute talk, the density rule is violated before the talk begins:
each slide gets $30$ seconds.

---

## ★4 — Ideas delivered and retained

At $10$ seconds per idea over $12$ minutes:

$$N_{\text{ideas}} = \frac{12 \times 60}{10} = 72\ \text{ideas}.$$

With an audience capacity of $4$,

$$\text{retained} = \min(4, 72) = 4, \qquad \frac{4}{72} = 5.6\%.$$

Full retention requires delivering at most the capacity:

$$N_{\text{ideas}} \le 4 \quad\Rightarrow\quad 4 \times 10\ \mathrm{s} = 40\
\mathrm{s}\ \text{of the 720 available}.$$

The arithmetic is absurd on purpose: no talk delivers $72$ ideas and none should try.
The realistic version is that most twelve-minute talks contain between eight and
fifteen distinct ideas, and retain a third of them. Deciding *which four* survive is
the design act.

---

## ★5 — Cutting a $90$-second overrun

$$90\ \mathrm{s} = 1.5\ \mathrm{min},
\qquad \text{words to cut} = 1.5 \times 130 = 195\ \text{words},$$
$$\text{slides to cut} = \frac{1.5}{1.5} = 1.0\ \text{slide}.$$

Which idea to drop: the **third supporting result**, not the primary one, and not
part of the method. The rule is that the cut must remove a self-contained piece —
one slide, one supporting result — rather than shaving sentences from everywhere,
because shaving everywhere costs fluency and the audience notices pauses, not content.
A rehearsed plan names the slide ("the second validation panel") so the decision is
already made.

---

## ★6 — Deck density

$$\text{visible words} = 14 \times 45 = 630,$$
$$\text{ratio} = \frac{1560}{630} = 2.5 .$$

Against the design target of about $9.8$, this deck is nearly four times too dense:
the slides repeat the speech instead of carrying structure and evidence. The remedy
is not to delete words from slides one at a time but to halve the slide count by
merging related slides and moving explanatory text into the speaker's lines. A
useful test: photograph each slide and check whether the title plus the figure alone
communicates something.

---

## ★7 — Does slide density change recall?

**Manipulation.** The same $12$-minute talk, recorded, in two versions: slides capped
at $20$ visible words each, and the same slides at $45$ words each. Content and
speaker script are identical, so only the projected text differs.

**Outcome.** Immediate recall of the primary result, scored on a $100$-point index
from four items: state the result, state its uncertainty, state the scope, and state
one implication. Scored by two blinded raters.

**Sample size.** Between-subject at $\alpha = 0.05$, $80\%$ power, difference $12$
points, standard deviation $22$ points (chosen planning value):

$$n\ \text{per arm} = \frac{2(1.96 + 0.842)^{2}\times 22^{2}}{12^{2}}
= \frac{2\times 7.851\times 484}{144} = 52.8 \approx 53,$$

so $106$ participants, plus $15\%$ for exclusions: $122$.

**Confound.** The deck version with fewer words may also have fewer slides if the
author merges them, so slide count and density move together. Fix the slide count by
construction: both versions have $10$ slides, and only the visible word count differs.
If that is not possible, measure the slide count and analyse it as a covariate.

---

## ★8 — Does a rehearsed overrun plan reduce lateness?

**Unit.** One contributed talk at a conference.

**Outcome.** Minutes over or under the scheduled slot, recorded by the session chair
(or from the recording), plus whether the question time was reduced.

**Design.** Cluster-randomised by session: sessions are randomly assigned to a
briefing that requires speakers to mark optional slides, or to their usual practice.
Randomising by speaker within a session is not adequate because overruns affect the
whole session's schedule and the chair's announcements.

**Selection bias.** Speakers who volunteer for rehearsal are the ones who would
finish on time anyway. Cluster randomisation removes the volunteer effect for the
*assignment*, but not for *compliance*: some speakers in the treatment arm will not
mark optional slides. Report the analysis both as randomised (intention to treat)
and by compliance, and treat the compliance analysis as secondary for exactly this
reason.
