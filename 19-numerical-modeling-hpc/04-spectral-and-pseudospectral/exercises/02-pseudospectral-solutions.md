# Solutions — 19-04-02 Pseudospectral Methods, Transforms and Aliasing

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [02 Pseudospectral Methods, Transforms and Aliasing](../02-pseudospectral.md).

---

## ★1 — The alias of 80 Hz at 100 samples/s

$$f_{\rm alias} = \left|80 - \mathrm{round}(0.8)\cdot100\right|
= |80 - 100| = 20\ \text{Hz}.$$

**No processing can recover 80 Hz.** The samples of a 20 Hz cosine and an 80 Hz
cosine at 100 samples/s are identical sequences, so the information distinguishing
them was never recorded. The lesson measures exactly this pattern
(110 Hz appearing at 10 Hz, 210 Hz at 10 Hz, 60 Hz at 40 Hz); an anti-alias
filter before sampling is the only remedy, because afterwards there is nothing to
unfold.

---

## ★2 — Products on 32 modes

Input at $m = 24$ on $N = 64$: the product needs $2m = 48$. The grid's Nyquist is
$N/2 = 32$, so mode 48 is not representable; the fold map sends
$48 \to 64 - 48 = 16$. The product therefore appears at **mode 16**, inside the
resolved band — an error of the full amplitude of the lost mode, landing where
every subsequent operation will treat it as physical.

Two consistency checks: (i) $m = 24 \le 32$, so the input itself is a
well-defined grid mode; (ii) the fold 16 lies below $N/3 = 21.3$, so the 2/3 rule
would *not* protect this band — its premise is violated by the input, exactly as
in the lesson's $k=12$ row.

---

## ★3 — The 2/3 rule and its premise

**The rule:** zero all modes with $|m| > \lfloor N/3\rfloor$ before forming each
product, then discard the product modes above the retained band.

**The premise:** the input spectrum must satisfy $|m| \le N/3$. Then every
product satisfies $|m_1 + m_2| \le 2N/3$, and the aliases of those modes (which
land at $N - m \ge N/3$) fall at or above $N/3$ — precisely the band the rule
discards. So the retained modes are computed exactly: the lesson measures
$3.8\times10^{-16}$ in the retained band for a $k = 9$ input on 32 points, and
$5.0\times10^{-1}$ for a $k = 12$ input that violates the premise.

---

## ★4 — Decide the policy for $N = 64$, power up to $m = 20$

- **Does the naive product alias?** The highest product mode is $2(20) = 40 > 32$,
  which is the Nyquist of a 64-point grid, so yes.
- **The 2/3 band:** $\lfloor N/3\rfloor = \lfloor 21.33\rfloor = 21$. The
  solution's power stops at $m = 20 \le 21$, so the premise holds — with one mode
  of margin.
- **Where does the alias land?** $64 - 40 = 24 > 21$, outside the retained band.
  So the naive product is already exact in the 2/3 band; the contamination is in
  modes 22–32.
- **Minimum padded grid:** $M \ge 4K = 4(21) = 84$; the conventional choice is
  $M = 3N/2 = 96$, which satisfies it with room to spare.

**Decision.** Because the alias lands outside the band the physics occupies, the
2/3 rule is safe *here*, at the cost of discarding modes 22–32 (which carry no
power today). The code must record the premise it depends on, and it must check
the spectrum at run time if the margin is only one mode. 3/2 padding makes the
same computation exact in all representable modes without relying on the margin,
which is the safer default for a code that will be applied to other spectra.

---

## ★5 — Verifying the measured aliasing outcomes

**Case $k_1 = 10$, $k_2 = 12$ on $N = 32$:** the sum mode is $22 > 16$, so it
folds to $32 - 22 = 10$, *inside* the resolved band. The naive product therefore
corrupts a low mode by the full amplitude of the lost interaction, and the
measured relative error is 874% — eight times the signal. ✔

**Case $k_1 = 6$, $k_2 = 7$:** the sum mode is $13 < 16$, representable, so no
fold occurs and the naive product is exact. Measured relative error 0.000%. ✔

**Prediction for $k_1 = 11$, $k_2 = 13$:** the sum mode is $24 > 16$, folding to
$32 - 24 = 8$, inside the resolved band. The prediction is therefore a large
relative error of the same order as the 874% and 367% cases — i.e. $O(1)$ and
far above any acceptable tolerance.

The three cases together are the point of the exercise: **the outcome depends on
the spectrum, not on the code.** The same un-de-aliased routine is exact in one
case and wrong by a factor 8 in another, and no test built on the safe case can
certify it.

---

## ★6 — Why a smaller timestep does not fix aliasing

Aliasing is not a truncation error in the time derivative; it is an error in the
*evaluation of the spatial nonlinear term* at a single instant. Each evaluation
returns a value for a low mode that is too large by a definite amount, and the
time integrator then advances that erroneous mode. Making $\Delta t$ smaller
makes each step smaller but multiplies the number of steps, so the injected error
is integrated — its total remains of the same order, and for a conservative
scheme in particular the injected energy is not damped. A truncation error, by
contrast, is proportional to a power of $\Delta t$ and vanishes as $\Delta t \to
0$. The measured evidence in the lesson is that one RHS evaluation already
differs from the de-aliased reference by 874% of the signal: the defect is in the
spatial operator, and no choice of time step touches it.

---

## ★7 — A cubic nonlinearity at $N = 512$

**Products.** A product of three factors with input modes bounded by $K$ reaches
$3K$.

**Padding requirement.** A real transform on $M$ points carries modes up to
$M/2$, so exactness requires $M/2 \ge 3K$, i.e. $M \ge 6K$.

**With the third-band convention** $K = \lfloor N/3\rfloor = 170$:

$$M \ge 6(170) = 1020 \;\Longrightarrow\; M = 1024 = 2N .$$

So a cubic term needs **2x padding**, against the 1.5x that sufficed for a
quadratic term — the rule is $M \ge 2qK$ for a term of polynomial degree $q$ when
the input band is $K$: for $q = 2$ and $K = N/3$ that is $M \ge 4N/3 \approx 1.33N$
(satisfied by $1.5N$), and for $q = 3$ it is $M \ge 2N$.

**Cost comparison.** Per evaluation: one forward transform and one inverse
transform, of size $N$ and $M$ respectively. At $N = 512$ the quadratic case uses
$M = 768$ and the cubic case $M = 1024$, so the transform cost grows by
$(1024/768)\log(1024)/\log(768) \approx 1.4$ — the extra factor is mild, which is
why production codes pad rather than hope. A "2/3-type" shortcut for a cubic term
would be worse: the natural analogue zeroes inputs above $N/4$, discarding half
the grid's bandwidth.

---

## ★8 — Detecting an un-de-aliased quadratic term in a safe code

**The difficulty.** A code whose spectrum is genuinely narrow produces correct
answers with no de-aliasing, so the production run cannot test it. The test must
*temporarily widen the spectrum* without changing the code under test.

**Test.**

1. Take the code's production configuration — same $N$, same time step, same
   boundary conditions — and replace the initial condition with
   $u_0(x) = \sin(2\pi kx) + \sin(2\pi k'x)$ where $k + k' > N/2$ and
   $k + k' < N$ (so the sum mode is not representable and folds into the resolved
   band). At $N = 64$ take $k = 20$, $k' = 22$: the sum $42$ folds to $64-42 = 22$
   — squarely inside the band.
2. Run exactly one RHS evaluation (or one step) with two builds of the same code:
   (a) the production build, and (b) the same build with the padding disabled.
3. Metric: the relative difference between the two results, in the $\mathrm{L}^2$
   norm of the nonlinear term.

**Expected outcomes.**

- **Code is correct:** the naive build differs from the padded build by an $O(1)$
  relative error on this input (the lesson measures 874% for a comparable case),
  while the padded build matches the fine-grid reference to round-off. The
  test therefore *demonstrates* that de-aliasing is active and correct.
- **Code has no de-aliasing at all:** the two builds are identical (there is
  nothing to disable), and both differ from the fine-grid reference by $O(1)$.
  The identical-builds outcome is the signature to look for.
- **Code de-aliases incorrectly** (a wrong band, a wrong padded size): the padded
  build differs from the fine-grid reference, and the run fails even in the
  production configuration. The sweep of $k'$ across the fold boundary
  ($k' = N/2 - k + 1$ to $N - k$) then maps out which band is mishandled.

**Why the design works.** It engineers a spectrum that *does* alias while leaving
the production code path untouched, exactly as the lesson's three-row table does.
The fine-grid reference is what makes it a verification rather than a comparison
of two builds.
