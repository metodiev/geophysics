# Solutions — 15-01-05 Sea Level, Tides and Harmonic Analysis

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed.

Lesson: [05 Sea Level and Tides](../05-sea-level-and-tides.md).

Constants: $G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$R = 6.371\times10^{6}\ \mathrm{m}$, $g = 9.81\ \mathrm{m\,s^{-2}}$.

---

## ★1 — Twice the lunar mass at the lunar distance

$$\zeta_{\max} = \frac{GMR^{2}}{gd^{3}}
= \frac{(6.674\times10^{-11})(1.4684\times10^{23})(6.371\times10^{6})^{2}}
{9.81\,(3.844\times10^{8})^{3}}
= 0.71388\ \mathrm{m}.$$

**Scaling law.** $\zeta_{\max} \propto M\,d^{-3}$ at fixed $R$ and $g$: the
tide-generating term is the *gradient* of the body's potential, in which one
power of $d$ has been differentiated away. Doubling $M$ therefore doubles
$\zeta_{\max}$ exactly (from $0.35694$ to $0.71388\ \mathrm{m}$), and the unit is
metres because $\zeta = -\Omega_2/g$ is a potential divided by an acceleration.

---

## ★2 — The $d^{-3}$ against $d^{-2}$ falloff

Direct attraction: $a = GM/d^{2}$. Tide-generating potential gradient: the degree-2
term is $\Omega_2 = -(GMR^{2}/d^{3})P_2(\cos\psi)$, and $\zeta = -\Omega_2/g$, so
$\zeta \propto M d^{-3}$.

$$\frac{\zeta_{\text{Sun}}}{\zeta_{\text{Moon}}}
= \frac{M_{\text{Sun}}}{M_{\text{Moon}}}
\left(\frac{d_{\text{Moon}}}{d_{\text{Sun}}}\right)^{3}
= \frac{1.989\times10^{30}}{7.342\times10^{22}}
\left(\frac{3.844\times10^{8}}{1.496\times10^{11}}\right)^{3}$$
$$= (2.709\times10^{7})(1.6979\times10^{-5}) = 0.4596,$$

matching the demonstration's $0.16405/0.35694 = 0.4596$. **The Sun's mass
advantage is a factor $2.7\times10^{7}$; its distance penalty is a factor
$5.9\times10^{4}$; the net is 0.46.** With a $d^{-2}$ law the Sun would dominate
by a factor $2.7\times10^{7}\times(3.844\times10^{8}/1.496\times10^{11})^{2}
= 1.79\times10^{4}$. The tides are lunar because the tide is a *differential*
force.

---

## ★3 — The design matrix

Model: $\eta(t_k) = a_0 + \sum_{j=1}^{3}[a_j\cos(\omega_j t_k)
+ b_j\sin(\omega_j t_k)]$.

$$\mathbf{d} = \mathbf{G}\mathbf{m}, \qquad
\mathbf{G} = \begin{pmatrix}
1 & \cos\omega_1t_1 & \sin\omega_1t_1 & \cdots & \sin\omega_3t_1\\
1 & \cos\omega_1t_2 & \sin\omega_1t_2 & \cdots & \sin\omega_3t_2\\
\vdots & & & & \vdots\\
1 & \cos\omega_1t_N & \sin\omega_1t_N & \cdots & \sin\omega_3t_N
\end{pmatrix},$$

with $\mathbf{m} = (a_0, a_1,b_1,a_2,b_2,a_3,b_3)^{\mathsf{T}}$.

Dimensions: $2J+1 = 7$ columns; $N = 30 \times 24 = 720$ rows. So $\mathbf{G}$ is
$720\times7$, $\mathbf{d}$ is $720\times1$ and $\mathbf{m}$ is $7\times1$. The
system is **overdetermined** by a factor of about 100, which is what makes least
squares appropriate; the interesting question is not whether there are enough
data but whether the columns are *distinguishable* — Sections 4 and 5 of the
lesson.

---

## ★★4 — Rayleigh periods

**(a)** K1 against O1:

$$\Delta f = 15.0411 - 13.9430 = 1.0981\ \mathrm{deg\,hour^{-1}}
= \frac{1.0981}{360} = 3.0503\times10^{-3}\ \mathrm{cycles\,hour^{-1}},$$

$$T_{\text{Rayleigh}} = \frac{1}{3.0503\times10^{-3}} = 327.84\
\mathrm{h} = 13.66\ \mathrm{days}.$$

**(b)** A 20-day record exceeds $13.66$ days, so **yes**, K1 and O1 are separable
there — by a margin of $46\,\%$.

**(c)** With $f_{N2} = 1/12.6583 = 0.0789995\ \mathrm{cycles\,h^{-1}}$:

$$f_{M2} = \frac{1}{12.4206012} = 0.0805114\ \mathrm{cycles\,h^{-1}},$$

$$\Delta f = 0.0805114 - 0.0789995 = 1.5119\times10^{-3}\
\mathrm{cycles\,h^{-1}},$$

$$T_{\text{Rayleigh}} = \frac{1}{1.5119\times10^{-3}} = 661.4\
\mathrm{h} = 27.56\ \mathrm{days}.$$

So M2 and N2 need a **27.6-day** record. This is a useful contrast: the M2/S2
pair needs $14.77$ days, the M2/N2 pair needs $27.56$ days, and a record of
$20$ days therefore separates the first pair but not the second. **Quoting an N2
amplitude from a 20-day record is exactly the error Section 4 of the lesson
quantifies.**

---

## ★★5 — Aliasing a $12.66\ \mathrm{h}$ constituent

True frequency $f = 1/12.66 = 0.0789889\ \mathrm{cycles\,hour^{-1}}$.

**(a)** $\Delta t = 6\ \mathrm{h}$, $f_s = 1/6 = 0.166667\ \mathrm{cycles\,h^{-1}}$:

$$\frac{f}{f_s} = 0.47393 \;\Rightarrow\; \mathrm{round}(0.47393) = 0
\;\Rightarrow\; f_{\text{alias}} = f = 0.0789889\ \mathrm{cycles\,h^{-1}},$$

alias period $12.66\ \mathrm{h}$ — **the constituent is resolved**, because its
frequency lies below the Nyquist frequency $f_s/2 = 0.083333\ \mathrm{cycles\,h^{-1}}$.

**(b)** $\Delta t = 12.4\ \mathrm{h}$, $f_s = 1/12.4 = 0.0806452\ \mathrm{cycles\,h^{-1}}$:

$$\frac{f}{f_s} = 0.97946 \;\Rightarrow\; \mathrm{round} = 1
\;\Rightarrow\; f_{\text{alias}} = 0.0789889 - 0.0806452
= -1.6562\times10^{-3}\ \mathrm{cycles\,h^{-1}},$$

alias period $|1/f_{\text{alias}}| = 603.8\ \mathrm{h} = 25.16\ \mathrm{days}$.

**The constituent is destroyed.** A 12.66 h oscillation sampled every 12.4 h is
indistinguishable from a 25-day oscillation — a signal 48 times slower than the
physics. This is the aliasing mechanism in its purest form: the sampling interval
was chosen close to the constituent's own period, which is the worst possible
choice.

---

## ★★6 — Trend uncertainty

**(a)** With $N = 240$, $t_k = k/12$ years,

$$\sum_k (t_k - \bar t)^{2} = \frac{1}{12^{2}}\cdot\frac{N(N^{2}-1)}{12}
= \frac{240(57599)}{1728} = \frac{1.38238\times10^{7}}{1728}
= 8000.0\ \mathrm{yr^{2}},$$

$$\mathrm{Var}(\hat b) = \frac{\sigma^{2}}{\sum(t_k-\bar t)^{2}}
= \frac{(0.025)^{2}}{8000} = \frac{6.25\times10^{-4}}{8000}
= 7.8125\times10^{-8}\ \mathrm{m^{2}\,yr^{-2}},$$

$$\sigma_{\hat b} = 2.795\times10^{-4}\ \mathrm{m\,yr^{-1}}
= 0.280\ \mathrm{mm\,yr^{-1}}.$$

**(b)** $N = 120$:

$$\sum_k (t_k-\bar t)^{2} = \frac{120(14399)}{1728} = 1000.0\ \mathrm{yr^{2}},
\qquad
\sigma_{\hat b} = \frac{0.025}{\sqrt{1000}} = 7.906\times10^{-4}\
\mathrm{m\,yr^{-1}} = 0.791\ \mathrm{mm\,yr^{-1}}.$$

**(c)** Halving the record multiplies the error by
$0.791/0.280 = 2.83 \approx 2^{3/2}$. The scaling is

$$\sigma_{\hat b} \propto N^{-3/2},$$

because $\sum(t_k-\bar t)^{2}$ grows as $N^{3}$ while $\sigma$ is fixed. Equivalently
$\sigma_{\hat b}\propto T^{-3/2}$ for a record of duration $T$: **quadrupling the
record length halves the trend error** (four times the data, $4^{3/2} = 8$ times
the precision per unit length... precisely, it reduces the error by a factor
$4^{3/2} = 8$). This is a much faster return than the $N^{-1/2}$ of a mean, and it
is why trend detection is worth waiting decades for.

---

## ★★7 — Equal errors, unequal relative errors

**(a)** In a nearly orthogonal design, $\mathbf{G}^{\mathsf{T}}\mathbf{G}$ is
close to diagonal and all its diagonal entries are approximately equal (each is
about $N/2$ for a cosine or sine column). The covariance is
$\sigma^{2}(\mathbf{G}^{\mathsf{T}}\mathbf{G})^{-1}$, so every coefficient's
variance is approximately $\sigma^{2}/(N/2)$ — **independent of the
constituent's amplitude**. The amplitude enters only through the signal, not
through the design.

**(b)** Relative error on O1: $0.0013/0.098 = 1.33\,\%$. On M2:
$0.0013/1.201 = 0.108\,\%$. **M2 is better determined in relative terms by a
factor of about 12**, which is the amplitude ratio.

**(c)** Nothing in the *estimator* can be changed to help O1: the precision on
every coefficient is already the noise floor $\sigma/\sqrt{N/2}$, so the only
routes are (i) more data — a longer record, or combining several instruments —
which reduces all errors together, or (ii) lower noise. It is a useful negative
result: you cannot weight a small constituent into a better estimate, and the
form ratio $(K1+O1)/(M2+S2)$ therefore carries a much larger relative error in
its numerator than in its denominator — which is worth stating when the ratio is
used to classify a site.

---

## ★★★8 — Designing a $2\ \mathrm{mm\,yr^{-1}}$ trend measurement

**(a) Sampling.** Hourly (or half-hourly) to avoid the aliasing of Section 5, with
the analysis reduced to monthly means or to a harmonic-plus-trend fit. Hourly
sampling costs nothing in precision once the record is long, and it removes the
M2 alias entirely.

**(b) Record length implied.** The requirement is
$\sigma_{\hat b}\lesssim 1\ \mathrm{mm\,yr^{-1}}$. From
$\sigma_{\hat b} = \sigma/\sqrt{N(N^{2}-1)/1728}$ and monthly means: with
$\sigma = 20\ \mathrm{mm}$ we need
$N(N^{2}-1)/1728 \ge (0.020/0.001)^{2} = 400$, i.e.
$N^{3} \gtrsim 691200$, so $N\gtrsim88$ months, about **8 years** — if the noise
is white. Real monthly sea-level anomalies have low-frequency correlations
(ENSO-like, multi-year), which inflate the effective $\sigma$ at long periods and
push the requirement to several decades. The defensible answer states the
assumption.

**(c) Controllable terms.** The tidal fit (Section 3), the sampling interval, the
record length, and the treatment of gaps. All are design choices, and all can be
verified before the analysis.

**(d) Uncontrollable terms.** Land motion at the gauge (glacial isostatic
adjustment, subsidence, tectonics), which enters the trend identically to a real
sea-level change and cannot be separated from a single gauge. Vertical land
motion must be measured independently — by continuous GNSS at the site, or by
differencing against a nearby absolute-gravity site. Secondary uncontrollable
terms: changes in the datum (bench-mark re-levelling), instrument drift and
change of sensor, and the non-stationarity of surge statistics. The honest
statement in the report is "relative sea level at this site changed by
$x\ \mathrm{mm\,yr^{-1}}$, of which $y\ \mathrm{mm\,yr^{-1}}$ is land motion
measured by GNSS, leaving $x-y$".

---

## ★★★9 — Adjudicating the two reports

**Which is defensible.** The 60-day report. Reasons, in order of weight:

1. **60 days exceeds the M2/S2 Rayleigh period of 14.77 days; 10 days does not.**
   The 10-day fit is asking the data a question they cannot answer. It is not
   wrong in the least-squares sense — the residual will be small — but M2 and S2
   are *trading off*, so neither amplitude is separately determined.
2. **The reported pair has the trade-off's signature.** The sum
   $1.31 + 0.28 = 1.59\ \mathrm{m}$ is nearly unchanged from the 60-day result's
   $1.20 + 0.40 = 1.60\ \mathrm{m}$: amplitude has moved from S2 to M2, exactly
   the direction expected when two nearly identical frequencies are fitted over
   less than one beat.
3. **The demonstration's own numbers quantify the problem.** At 10 days the
   condition number is 1.85 and the fitted errors are $+0.004\ \mathrm{m}$ on
   both constituents; at 1 day the condition number is 834.7 and S2 comes out
   $+1.017\ \mathrm{m}$ wrong. A discrepancy of $+0.11/-0.12\ \mathrm{m}$ at the
   *stated* 10 days is therefore **too large to be explained by the design alone**
   with 50 mm noise: it points to a shorter or gappier record than claimed, a much
   larger noise level, or an analysis error.

**The quantifying number.** The condition number of the design matrix
(1.85 at 10 days against 1.466 at 60 days) together with the Rayleigh period
(14.77 days). Reporting either would have prevented the problem.

**What would settle it.** The record's actual sampling and gap structure — or,
equivalently, the condition number of the design the second analyst used. If the
10-day record is in fact 10 complete days at 30-minute sampling, the second
report is simply an analysis error; if it is 10 *elapsed* days with large gaps, the
effective record may be shorter than the Rayleigh period and neither pair should
have been quoted separately. Asking for the design matrix resolves the dispute;
asking for the amplitudes again does not.
