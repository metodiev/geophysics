# Solutions — 01-10-07 Two-Dimensional Fourier Analysis and Wavenumber Filtering

> **Read this after attempting the exercises, not before.**
>
> All values below were computed. Values quoted from the supplied script are the
> values it printed.

---

## ★1 — Axes of a 2-D transform

**(a)**

| quantity | value |
|---|---|
| array length $L = N_x\,dx$ | $64\times12.5 = 800$ m |
| record length $T = N_t\,dt$ | $256\times0.004 = 1.024$ s |
| wavenumber bin $dk_x = 1/L$ | $0.00125$ cycles/m |
| frequency bin $df = 1/T$ | $0.9766$ Hz |
| Nyquist wavenumber $1/(2\,dx)$ | $0.04$ cycles/m |
| Nyquist frequency $1/(2\,dt)$ | 125 Hz |

**(b)** $\lvert k_x\rvert = f/v = 25/2000 = 0.0125$ cycles/m. In bins:
$0.0125/0.00125 = 10$. Since $p > 0$ (arrival time increasing with offset) and the
convention places those at negative $k_x$,

$$k_x = \boxed{-10\ \text{bins}} .$$

**(c)** $\lvert k_x\rvert = 15/1200 = 0.0125$ cycles/m, i.e. 10 bins again. Here
$p < 0$ (arrival time *decreasing* with offset, energy moving towards decreasing
$x$), so the sign flips:

$$k_x = \boxed{+10\ \text{bins}} .$$

**The check worth making every time:** the two events have the same
$\lvert k_x\rvert$ and appear at symmetric positions in the f-k plane. A filter
that keeps one and rejects the other is a *direction* filter, and getting the
sign convention wrong reverses exactly this decision — with no visible change in
the output's appearance.

---

## ★2 — From a moveout to a wavenumber

**(a)** The first break advances 2.5 ms per 12.5 m of offset, so

$$p = \frac{2.5\times10^{-3}}{12.5} = 2.0\times10^{-4}\ \mathrm{s/m},
\qquad v = \frac1p = \boxed{5000\ \mathrm{m/s}} .$$

**(b)** $k = f/v = 30/5000 = \boxed{6.0\times10^{-3}\ \text{cycles/m}}$.

**(c)** The alias frequency is
$f_a = v/(2\,dx) = 5000/25 = 200$ Hz, far above 30 Hz, so the event is
**not aliased**. Fast events are hard to alias: the phase step between traces is
$2\pi f\,dx/v$, which is small when $v$ is large.

---

## ★3 — Separability

The 2-D kernel factorises as
$e^{-2\pi ik_xn_x/N_x}\cdot e^{-2\pi ik_fn_t/N_t}$, so the double sum can be
rearranged into two successive single sums; each is a 1-D DFT, giving one
transform per trace followed by one per frequency, i.e. $2N$ 1-D transforms
instead of $N^{2}$ direct double sums.

If the second pass is applied to the wrong axis, the result is still an array of
complex numbers of plausible magnitude, but the wavenumber axis contains
frequencies and vice versa: every subsequent filter, mask or interpretation of
the f-k panel is then wrong, and the error is invisible in a display because the
panel still *looks* like an f-k panel. The check that catches it is to transform a
synthetic single dipping plane wave, where the answer is known (one line at
$k_x = p\,f$), before trusting any pipeline.

---

## ★4 — Four components of a shot gather in the f-k plane

- **(a) Fast reflection dipping one way:** a straight line through the origin at
  slope $p = 1/v$ (small $\lvert p\rvert$), in one half-plane.
- **(b) Fast reflection dipping the other way:** a straight line through the
  origin with the opposite sign of $k_x$, the mirror of (a) about the $f$ axis.
- **(c) Slow ground roll:** a straight line through the origin with a *large*
  $\lvert p\rvert$, so a shallow slope — nearer the $k_x$ axis than the
  reflections. If the spatial sampling is too coarse, the line wraps
  ([01-10-05](../05-windowing-aliasing.md)) and may appear in the wrong
  half-plane.
- **(d) Random noise:** *not* a line. Random noise fills the whole plane with a
  roughly uniform amplitude, so it provides the background against which the
  lines are seen and it is what limits any amplitude-based filtering.

**Which are lines:** (a), (b) and (c) — and that is the point of the lesson. Random
noise, scattered energy and any non-plane-wave component do not localise, so an
f-k filter cannot separate them no matter how well designed it is.

---

## ★★5 — Designing a fan filter

**(a)** Ground roll at 400 m/s has $p = 1/400 = 2.5\times10^{-3}$ s/m. Reflections
above 1600 m/s have $\lvert p\rvert < 1/1600 = 6.25\times10^{-4}$ s/m. So the mask
must **reject everything with $\lvert p\rvert > 6.25\times10^{-4}$ s/m** (slower
than 1600 m/s), which includes the ground roll, and keep the rest.

**(b)** Since $p = k_x/f$, the mask is

$$\text{keep if }\quad \left\lvert\frac{k_x}{f}\right\rvert < \frac{1}{1600}
\qquad\Longleftrightarrow\qquad \lvert k_x\rvert < \frac{f}{1600} .$$

Note that the boundary is a *line through the origin* — a cone in the
$(f,k_x)$ plane — not a horizontal or vertical line. A mask on $k_x$ alone would
reject a different set of events at every frequency.

**(c)** At 10 Hz the boundary is at
$\lvert k_x\rvert = 10/1600 = 6.25\times10^{-3}$ cycles/m
$= 6.25\times10^{-3}/1.25\times10^{-3} = \boxed{5}$ bins from the origin. So at
10 Hz the filter passes only the events whose f-k line lies within 5 bins of the
$f$ axis.

**(d)** At 2 Hz the boundary is at
$\lvert k_x\rvert = 2/1600 = 1.25\times10^{-3}$ cycles/m — exactly **one
wavenumber bin**. A one-bin offset at 2 Hz corresponds to an apparent velocity of
$2/(1.25\times10^{-3}) = 1600$ m/s, i.e. precisely the boundary velocity. So at
2 Hz the filter can only express "inside one bin or outside it": there is no
resolution to do anything finer. **Implication:** the origin region is where all
events' lines coincide, so it must be left unmuted, and the low-frequency content
of the record is effectively passed unfiltered. Any processing report that claims
ground roll was removed "at all frequencies" is claiming more than the transform
can deliver.

---

## ★★6 — Grid-aligned plane waves through a fan filter

**(a)** With the lesson's grid ($dk_x = 0.00125$ cycles/m, $df = 0.9766$ Hz):

$$k_x = 10\times0.00125 = 0.0125\ \text{cycles/m},\qquad
f = 14\times0.9766 = 13.672\ \text{Hz},$$

$$p = \frac{k_x}{f} = \frac{0.0125}{13.672} = 9.143\times10^{-4}\ \mathrm{s/m}
\;\Longrightarrow\; v = \boxed{1093.8\ \mathrm{m/s}} .$$

For the second event,

$$k_x = -24\times0.00125 = -0.03,\qquad
p = \frac{-0.03}{13.672} = -2.194\times10^{-3}\ \mathrm{s/m}
\;\Longrightarrow\; v = \boxed{-455.7\ \mathrm{m/s}} .$$

**(b)** The filter keeps $\lvert k_x/f\rvert < 1/800$, i.e. $\lvert p\rvert <
1.25\times10^{-3}$ s/m. Event A has $\lvert p\rvert = 9.14\times10^{-4}$ → kept;
event B has $\lvert p\rvert = 2.19\times10^{-3}$ → rejected. The measured
fractions surviving are

| event | fraction surviving its own RMS |
|---|---|
| A | $1.000\times10^{0}$ |
| B | $5.965\times10^{-15}$ |

and the filter output differs from event A alone by $6.4\times10^{-15}$ of A's
RMS. Both numbers are round-off. **Interpretation:** the algebra of f-k filtering
is exact when the events occupy isolated bins and the mask is a straight line
between them; nothing about the mathematics of the filter limits it. What limits
it in practice is Section 6 (packets).

**(c)** Rebuilt as finite wave packets of 0.12 s width, about **0.21 of B leaks
through** the filter and about **0.13 of A is lost**. The change is caused by the
packet's finite spatial extent, which broadens its f-k ridge in $k_x$ into a
Dirichlet-like spread; part of that spread falls on the wrong side of the mask,
and part of A's spread does the same. The algebra is unchanged; the *data* are no
longer a single line.

---

## ★★7 — Quadrant filtering

**(a)** For $p > 0$ the energy is at negative $k_x$ (Section 3.2 of the lesson),
so the kept half-plane is $\{f>0,\ k_x<0\}$. Its **conjugate half**
$\{f<0,\ k_x>0\}$ is also kept because the data are real: the two halves are
related by $Z(-f,-k_x) = \overline{Z(f,k_x)}$, and keeping only one of them
produces a complex output whose interpretation in terms of real amplitudes is
wrong. Keeping both makes the filter a real-valued operation.

**(b)** If only the positive-frequency half were kept, the output would be complex
— effectively a *spatial analytic signal* rather than a separated wavefield. Its
real part is the event at half amplitude with a $90^\circ$ phase rotation
relative to the input, and the envelope/phase interpretation changes. The visible
symptom is a section whose events are recognisable but whose wavelets have been
rotated in phase, which will invalidate any amplitude or polarity measurement.

**(c)** Both $2.0\times10^{-15}$ (leakage of B) and $1.6\times10^{-15}$ (loss of
A) are **round-off**. For events that occupy isolated bins on the correct side of
the origin, quadrant separation is exact, and these residuals are the only
evidence needed to say so.

**(d)** Every event's f-k line passes through the origin, so in the neighbourhood
of $(f,k_x) = (0,0)$ all events — up- and down-going, fast and slow — are
indistinguishable. A cone around the origin must therefore be left unmuted unless
one is prepared to remove legitimate signal along with the unwanted energy. How
large the cone must be is a judgement about the data, which is why the cone is
chosen per dataset and reported with the result.

---

## ★★8 — Wavenumber cuts and tapering

**(a)** A cut at 6 bins applied to an event centred at 10 bins does **not** remove
the event cleanly: because the event's spectrum is a spread ridge (its width set
by the array length), the cut removes the part of the ridge beyond 6 bins while
leaving the inner part, and it leaves a *sharp edge* in the effective transfer
function. That edge is the problem: a hard edge is a truncated series, and a
truncated series overshoots at a discontinuity
([01-10-03](../03-convolution.md)). So the answer to "what fraction is removed" is
not the whole story; the *shape* of what remains, and the ringing it carries, is
what limits interpretability.

**(b)** The measured numbers:

| version | edge RMS | middle RMS | edge/middle | energy removed by taper |
|---|---|---|---|---|
| no taper | $9.3625\times10^{-2}$ | $1.5011\times10^{-2}$ | 6.237 | — |
| 10% cosine taper | $5.6871\times10^{-2}$ | $1.3750\times10^{-2}$ | 4.136 | 0.1438 |

The taper cuts the edge amplitude by about 40% and removes 14.4% of the total
energy. Whether it is "worth it" depends on where the interpretation happens:
the energy it removes is concentrated in the edge zone (the taper zone itself),
while the artefact it suppresses is the ringing that would otherwise spread from
the edges into the interior. **If the array edges are inside the interpretable
area, the taper is clearly worth it; if they are discarded anyway, the taper's
main benefit is that it confines the remaining ringing to the zone you were going
to discard.**

**(c)** Two alternatives:

1. **Symmetric (mirror) padding before the transform.** Extending the record by
   reflecting it about its ends makes the periodic extension continuous to first
   order, so the wrap-around discontinuity that causes the ringing is largely
   removed. *Cost:* the padding fabricates samples; the processed interior is
   contaminated by the fabricated description at the edges, and the effect must be
   measured rather than assumed.
2. **A smooth mask** — for example a cosine taper of the mask edge rather than a
   hard cut — which suppresses the ringing by removing the sharp edge.
   *Cost:* a smooth mask passes some of the energy it was meant to reject, so the
   filter's rejection performance is traded for its ringing performance. (The
   lesson's own test of a tapered mask showed no improvement in the leakage
   metric, because the leakage there was dominated by the near-origin geometry
   rather than by the mask edge — a reminder that the fix must match the cause.)

---

## ★★★9 — Leakage versus packet length

**(a)** Measured leakage of event B and loss of event A:

| packet width (s) | B leaking | A lost |
|---|---|---|
| 0.06 | 0.2220 | 0.1274 |
| 0.12 | 0.2101 | 0.1254 |
| 0.24 | 0.1994 | 0.1266 |
| 0.48 | 0.1673 | 0.1049 |

**Trend:** both quantities fall slowly as the packet lengthens — leakage from
0.222 to 0.167 (a 25% reduction for an eightfold increase in length) and loss from
0.127 to 0.105. The approach to zero is slow, and neither is close to zero even
for a packet eight times longer than the first.

**(b)** The reason is that a wave packet's f-k ridge runs from the origin outward
along the line $\lvert k_x\rvert = \lvert p\rvert f$, while the mask boundary runs
along $\lvert k_x\rvert = f/v_{\text{cut}}$. The *gap* between them is
$\lvert p - 1/v_{\text{cut}}\rvert f$, which is **proportional to $f$** and
therefore shrinks to nothing as $f \to 0$. The ridge has a spread in $k_x$ of
order $1/L$ set by the *array length*, not by the packet; once
$\lvert p - 1/v_{\text{cut}}\rvert f \lesssim 1/L$, the ridge's spread crosses the
mask and energy leaks. Lengthening the packet narrows its *frequency* bandwidth
(it is, after all, a narrower band of frequencies that is present at low $f$), so
leakage falls — but the array length, not the packet, sets the resolution that
determines whether the low-frequency part can be separated at all. **The residual
leakage is a property of the array, and no processing on a given array can remove
it.**

**(c)** The test: keep $dx$ and the frequency content fixed, and vary the *array
length* $L$ (equivalently the number of traces, or equivalently the dip of the
event, which changes how many traces are lit within the record). Measure the
leakage as a function of the dimensionless ratio

$$\frac{\text{gap at the lowest frequency of interest}}{\text{wavenumber resolution}}
= \frac{\lvert p - 1/v_{\text{cut}}\rvert f_{\min}}{1/L} .$$

Plot leakage (fraction of B) against that ratio on log–log axes. A curved
collapse of the points from different $(p, v_{\text{cut}}, f_{\min}, L)$
combinations onto one curve is the signature that this ratio is the controlling
variable; its slope would give the sensitivity, and the point where leakage falls
below, say, 5% would give the design rule for the array length.

**(d)** Additional information required:

1. The mask's velocity bounds, and the taper (if any) on the mask and the data.
2. A quantitative measure of the removal — how much ground-roll energy was on the
   input and how much remains — not a visual "it looks gone".
3. The **distortion** of the wanted signal: the amplitude and phase change in a
   band where reflections are known to be present, measured before and after (the
   demonstration data are the ideal, but on real data a synthetic or a repeat
   shot serves).
4. The alias frequency and whether the ground roll was aliased. If it was, the
   aliased energy shares quadrants with legitimate signal, so removal also removed
   signal, and the affected frequency band must be named.
5. The spatial taper applied and the fraction of the array discarded, because
   amplitudes there are not interpretable.

A report that provides (1)–(5) can be checked; a report that provides only the
section cannot.

---

## ★★★10 — Aliasing, conventions and their consequences

**(a)** The phase step between neighbouring traces for an event of frequency $f$
and apparent velocity $v$ is $\Delta\phi = 2\pi f\,dx/v$. Unambiguous sampling
requires $\lvert\Delta\phi\rvert \le \pi$, so

$$f \le \frac{v}{2\,dx} \equiv f_a .$$

For $dx = 12.5$ m and $v = 850$ m/s:

$$f_a = \frac{850}{2\times12.5} = \boxed{34\ \mathrm{Hz}} .$$

**(b)** Folding the wavenumber axis with Nyquist wavenumber
$k_N = 1/(2\,dx) = 0.04$ cycles/m means adding or subtracting
$2k_N = 0.08$ cycles/m until the value lies in $[-0.04, +0.04]$:

$$k_x^{\text{true}}(52\ \mathrm{Hz}) = \frac{52}{1000} = 0.052
\;\longrightarrow\; 0.052 - 0.08 = \boxed{-0.028}\ \text{cycles/m},$$

so the sign flips and the magnitude is 0.028 — the lesson measures $+0.02875$,
which is this value quantised to the nearest bin ($0.00125$). The apparent
velocity is

$$v_{\text{app}} = \frac{f}{\lvert k_x\rvert} = \frac{52}{0.02875} = 1809\
\mathrm{m/s},$$

matching the lesson's measurement of 1809 m/s.

**(c)** For the 850 m/s event at 60 Hz:

$$k_x^{\text{true}} = \frac{60}{850} = 0.0706\ \text{cycles/m}
\;\longrightarrow\; 0.0706 - 0.08 = -0.0094\ \text{cycles/m},$$

$$v_{\text{app}} = \frac{60}{0.0094} = 6383\ \mathrm{m/s},$$

with the **opposite sign of dip**. So the filter designed to remove the event
(slower than 800 m/s) sees an apparent slowness of
$1/6383 = 1.57\times10^{-4}$ s/m, far *inside* its pass region — i.e. **the
filter keeps exactly the energy it was designed to remove, and the removed
energy appears as a fast event travelling the other way.** Quantitatively: a
850 m/s event at 60 Hz is aliased at this spacing, and its apparent velocity after
the wrap is 6383 m/s — a value no shallow event could have. Note the paradox to
report: the filter's *stated* criterion was met (it kept everything faster than
800 m/s), and the ground roll was nevertheless passed. The design criterion was
met on the wrapped data, not on the true data.

**(d)** A reversed convention swaps the mask from one half-plane to the other, so
the events intended for removal are kept and vice versa. From the output alone,
the detectible symptom is that the section's *character* is inverted: strong,
coherent, slow-looking energy remains while the reflections that should dominate
are attenuated. In the f-k panel (if one is produced) the mask is visibly on the
wrong side of the origin.

**Detection is not guaranteed.** If the events on either side of the origin are
similar in slowness and amplitude — for instance two reflections dipping in
opposite directions, or a filter whose mask is nearly symmetric — the mistaken
output is a plausible section that keeps the wrong events, and it will pass a
visual review. The only reliable precautions are: state the convention with the
mask, and check the mask against a synthetic plane wave of known slowness whose
expected position in the f-k plane is computed **from the same convention
statement**. This is why the convention is the first thing to check and the last
thing to assume.
