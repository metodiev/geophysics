# Exercises — 04-03-01 The Geologic Time Scale and Deep Time

Attempt these **closed-book** before opening the
[solutions](./01-geologic-time-scale-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/01-deep_time_demo.py`](../code/01-deep_time_demo.py) require you to run
it and report its actual output.

**Convention for this set.** Where an anchor age is needed, use
$4.54 \times 10^9$ a and state that it is a commonly tabulated value from a
compilation you must cite. No problem in this set asks you to assert a boundary
age of the geologic time scale.

---

## ★ Foundational

**★1.** On a linear bar representing $4.54 \times 10^9$ a, compute the time
represented by

(a) 1 mm on a bar 1 m long;
(b) 1 mm on a bar 100 m long;
(c) 1 s on a 24 h clock;
(d) 1 printed line of width 0.2 mm on a figure 200 mm wide.

---

**★2.** For the same anchor, compute

(a) the duration represented by 100 Ma on the 24 h clock;
(b) the ratio of the anchor to 100 Ma, and its base-10 logarithm;
(c) the duration represented by 1 Ga on the 24 h clock;
(d) the fraction of the anchor occupied by 1 per cent of the anchor, expressed
in years.

---

**★3.** Without using any age in years, list

(a) the four eons in order;
(b) the three eras of the Phanerozoic eon;
(c) the periods of the Paleozoic era;
(d) the periods of the Mesozoic and Cenozoic eras.

State what these names are, as opposed to the numbers attached to them.

---

## ★★ Applied

**★★4.** Two boundaries are dated at $400 \pm 5$ Ma and $500 \pm 5$ Ma
(SYNTHETIC values chosen for the arithmetic). Compute the duration and its
uncertainty for

(a) independent errors, $\rho = 0$;
(b) $\rho = 0.5$;
(c) $\rho = 0.9$;
(d) $\rho = 1$.

State in one sentence why the same data set gives four different answers.

---

**★★5.** Run [`../code/01-deep_time_demo.py`](../code/01-deep_time_demo.py).

(a) Report the value of 1 Ma on the 24 h clock and on the calendar-year
compression.
(b) Report what 1 day of the calendar-year compression represents.
(c) Report the reported error on all three anchor ages and their relative
magnitudes.
(d) Explain why one of the three anchors has a relative uncertainty two orders
of magnitude smaller than another, and what kind of quantity each is.

---

**★★6.** Using the same anchor,

(a) compute the size of recorded history (5000 a) on a 100 m bar;
(b) compute the duration represented by a gap of 1 mm on that bar;
(c) state which of (a) and (b) is smaller and what that implies for reading a
map at that scale.

---

**★★7.** A stratigraphic interval is claimed to be 2 Ma long.

(a) On a linear axis 200 mm wide for $4.54 \times 10^9$ a, compute the length
that represents 2 Ma.
(b) Compare it with the width of a printed line and state whether the claim can
be displayed on such an axis.
(c) State the shortest interval that can be displayed with a resolution of one
printed line.

---

## ★★★ Research-oriented

**★★★8.** A sedimentation rate is computed as thickness divided by duration:
$100$ m over $1$ Ma, with $\sigma(\text{thickness}) = 5$ m and
$\sigma(\text{duration}) = 0.2$ Ma, assumed independent.

(a) Compute the rate and its relative uncertainty.
(b) Repeat for $\sigma(\text{duration}) = 0.5$ Ma and comment on how the
uncertainty in the duration dominates.
(c) State the duration uncertainty at which the rate becomes uninformative if
"uninformative" is defined as a relative uncertainty exceeding 50 per cent.
(d) Explain how a correlation between the two boundaries of the duration — as
happens when one laboratory dates both — changes the answer, using the
propagation formula.

---

**★★★9.** You are asked to produce a graphic that communicates deep time
honestly to a general audience.

(a) Argue for or against the "Earth history in 24 hours" compression, using at
least two computed numbers from this set.
(b) Propose a presentation that is quantitative rather than metaphorical and
state what it sacrifices.
(c) Show that no single linear axis can display both the age of the Earth and an
interval of $10^5$ a with a resolution of one printed line, by computing the
figure width that would be required.
(d) State the one thing your presentation must carry that a compression graphic
does not: the provenance of every age used.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
