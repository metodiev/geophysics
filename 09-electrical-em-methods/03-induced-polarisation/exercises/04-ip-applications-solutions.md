# Solutions — 09-03-04 IP for Sulphides, Clays, Contaminants and Permafrost

> **Read after attempting the exercises.** Lesson:
> [04 IP Applications](../04-ip-applications.md). All models **SYNTHETIC**;
> every number below is printed by
> [`code/ip_applications_demo.py`](../code/ip_applications_demo.py) or is
> arithmetic on a printed number.

---

## ★1 — The pathway arithmetic

1. $F = 6.617$, so $A = \sigma_w/F = 0.010/6.617 = 0.001511$ S/m.
2. $\sigma_{\text{bulk}} = A + B = 0.001511 + 0.002000 = 0.003511$ S/m.
3. $\rho_0 = 1/0.003511 = 284.80\ \Omega\,\mathrm{m}$.
4. $m_{\text{eff}} = \dfrac{0.30 \times 0.002000}
   {0.001511\times0.70 + 0.002000}
   = \dfrac{0.000600}{0.001058 + 0.002000} = \dfrac{0.000600}{0.003058}
   = 0.1962$.

Compare with the same ground at $\sigma_w = 0.05$ S/m, where $m_{\text{eff}} =
0.0823$ and $\rho_0 = 104.65\ \Omega\,\mathrm{m}$: **a fivefold fresher pore
fluid more than doubles the effective chargeability while tripling the
resistivity.** Both changes come from $A$, and neither required a change in the
mineral assemblage.

---

## ★2 — Extremes of the end-member table

Peak phase: **massive sulphide** at $197.611$ mrad; smallest **frozen ground** at
$3.282$ mrad. Ratio $= 197.611/3.282 = 60.21$.

Peak frequency: **clay-rich soil** at $88.227$ Hz; lowest **graphitic schist** at
$0.04558$ Hz. Ratio $= 88.227/0.04558 = 1935.7$.

For the pair frozen ground ($16.323$ Hz) and clean sand ($3.199$ Hz) the *phase*
is nearly identical ($3.282$ vs $5.025$ mrad, a factor $1.53$, below classification
reliability at $2$ mrad noise) while the *peak frequency* differs by a factor
$5.1$. The frequency — that is, the shape of the spectrum — is therefore the
discriminant, provided the survey band contains both peaks; a band ending at
$1$ Hz contains neither and sees two nearly phase-free grounds.

---

## ★3 — Reading the scenario table

**(a)** $\rho = 6.53\ \Omega\,\mathrm{m}$ with $1.156$ mrad is the **plume**
scenario (pore fluid raised to $1.0$ S/m).

**(b)** $\rho = 23.24\ \Omega\,\mathrm{m}$ with $69.268$ mrad is the
**clay-rich** scenario (surface conductance raised twentyfold).

**(c)** Resistivity alone would not confuse these two *in this table* (a factor
$3.6$ apart), but it would place them both in the same qualitative class of
"conductor", which is what the lesson means by a class ambiguity: a resistivity
survey of a site where the clay content is unknown cannot say whether a
conductive anomaly is a saline fluid or added clay. Phase alone would separate
them easily here (a factor $60$). The general statement is the reverse of the
table's convenience: near the base case, where the phase is only a few mrad,
*resistivity* separates clay from saline fluid; once the phase contrast is large,
phase separates them. The lesson's plume-versus-frozen comparison is the case
where phase alone fails.

---

## ★4 — Deriving the effective chargeability

Parallel conductances: $G_A = A$ (electrolyte, frequency independent) and
$G_B(\omega) = B\left[(1-m_0) + m_0/(1+i\omega\tau)\right]$ (polarisable).

DC: $G_A + G_B(0) = A + B$, so $\rho_0 = 1/(A+B)$.

High frequency: $G_B(\infty) = B(1-m_0)$, so
$\rho_{\infty} = 1/\left[A + B(1-m_0)\right]$.

$$m_{\text{eff}} = 1 - \frac{\rho_\infty}{\rho_0}
= 1 - \frac{A+B}{A + B/(1-m_0)}
= \frac{m_0B}{A(1-m_0) + B}.$$

**Limit $A = 0$:** $m_{\text{eff}} = m_0B/B = m_0$ — the intrinsic
polarisability, fully expressed, because the electrolyte no longer competes for
current.

**Limit $A \gg B$:** $m_{\text{eff}} \to \dfrac{m_0B}{A(1-m_0)}
= \dfrac{m_0}{1-m_0}\cdot\dfrac{B}{A}$ — small and falling as $1/A$, so doubling
the pore-fluid conductivity roughly halves the measured chargeability. For
$m_0 \ll 1$ this is simply $m_0$ times the current fraction $B/(A+B)$, which is
the "current split" reading used throughout the lesson.

---

## ★5 — Why adding $\lvert\rho\rvert$ changes the verdict

Clay-rich soil: $\rho_0 = 40\ \Omega\,\mathrm{m}$, $m_0 = 0.060$, $c = 0.30$,
$\tau = 0.002$ s — a modest peak phase ($7.427$ mrad) that lies mostly *above*
$1$ Hz.

Frozen ground: $\rho_0 = 3000\ \Omega\,\mathrm{m}$, $m_0 = 0.020$, $c = 0.40$,
$\tau = 0.010$ s — an even smaller peak phase ($3.282$ mrad) at $16.3$ Hz.

Their phase spectra differ by only $1.39$ noise units over $0.01$–$100$ Hz at
$2$ mrad noise, because both are small and broad in the measured band. Their
resistivities differ by a factor $75$ ($40$ against $3000\ \Omega\,\mathrm{m}$),
which is $305.9$ noise units at $1\%$ amplitude noise.

So the phase comparison is being asked to do a job it cannot do: distinguish two
weakly polarised grounds. The measurement doing the work after the amplitude is
included is the *magnitude* of $\rho$ — the survey that reported only phases
would have thrown away a factor $75$ signal. The lesson's practical rule follows:
always report $\rho_0$ with the phase, even when the interpretation is about
polarisation.

---

## ★6 — The frozen scenario

Fraction of base conductivity:

$$\frac{\sigma_{\text{frozen}}}{\sigma_{\text{base}}}
= \frac{4.1511\times10^{-5}}{0.009556} = 4.344\times10^{-3}
= 0.434\%.$$

Resistivity change:
$\rho_{\text{frozen}}/\rho_{\text{base}} = 24089.88/104.65 = 230.20$, so
$+22\,920\%$ — the printed value. Check it directly:
$1/4.1511\times10^{-5} = 24\,090\ \Omega\,\mathrm{m}$ against
$1/0.009556 = 104.65\ \Omega\,\mathrm{m}$, ratio $230.2$ ✓.

The same scenario's peak phase is $4.033$ mrad against the base case's
$17.787$ mrad, a change of $-13.754$ mrad — comfortably above the $2$ mrad
threshold. So in this model freezing is a *double* signal: a large resistivity
rise and a large phase fall. That is a property of the assumed parameter changes
(pore fluid to $10^{-5}$ S/m, surface pathway to $2\%$, and the intrinsic
$m_0$ to $0.02$), not a prediction about real permafrost.

---

## ★7 — Halving the surface conductance

**Arithmetic.** With $B' = 0.0010$ S/m, $\sigma_w = 0.05$ S/m,
$A = 0.05/6.617 = 0.007556$ S/m:

- $\sigma_{\text{bulk}}' = 0.007556 + 0.001000 = 0.008556$ S/m;
- $\rho_0' = 1/0.008556 = 116.87\ \Omega\,\mathrm{m}$ against the base
  $104.65\ \Omega\,\mathrm{m}$ — a **$+11.69\%$** change, above the $1\%$
  threshold and therefore detectable in principle;
- $m_{\text{eff}}' = \dfrac{0.30\times0.001000}{0.007556\times0.70 + 0.001000}
  = \dfrac{0.000300}{0.006289} = 0.04770$ against the base $0.0823$;
- the peak phase falls from $17.787$ to **$10.122$ mrad**, a change of
  $-7.665$ mrad, above the $2$ mrad threshold.

**Decision.** The phase moves by $-7.7$ mrad, nearly four times its threshold, so
the change is detectable by IP alone in this model; the resistivity moves by
$+11.7\%$, about twelve times its threshold, so it is also detectable by
resistivity alone. A survey with both measurements has a clear signal.

**What you would report.** "The surface polarisability of this ground has fallen
by about $42\%$ (from $m_{\text{eff}} = 0.082$ to $0.048$) with a $+11.7\%$
resistivity increase, consistent in this model with a loss of polarisable
surface area at constant pore-fluid conductivity."

**What you cannot exclude.** (i) A decrease in surface area *and* a small
increase in salinity can produce the same pair, because both act on
$m_{\text{eff}}$ through $B/A$ while pushing $\rho$ in opposite directions;
(ii) a change in $m_0$ (a change in the *intrinsic* polarisability of the
surface) has exactly the same signature as a change in $B$, since
$m_{\text{eff}} \propto m_0 B$ to first order when $B \ll A$; (iii) a change in
cementation exponent or porosity moves $A$ at constant $B$ and cannot be
separated from (i) with these two numbers alone. Separating them needs an
independent constraint — a porosity estimate, a temperature series, or a
frequency-resolved measurement of $\tau$.

---

## ★8 — Separating the two models

**Where the models differ.** The two fits are indistinguishable inside
$0.01$–$100$ Hz (residuals $2.054$ and $1.766$ mrad against $2.0$ mrad noise).
Outside the band they differ by $4.491$ mrad at $10^{-3}$ Hz, $6.603$ mrad at
$10^{3}$ Hz, and up to $1.8\%$ in amplitude at $10^{4}$ Hz.

**Band.** Extend to $10^{-3}$ Hz at the low end and $10^{3}$ Hz at the high end
— one decade beyond the fitted band on each side, which is where the difference
already amounts to $4$–$7$ mrad, i.e. two to three times the present noise.

**Noise level.** To make those differences decisive at $5\sigma$, the phase noise
must be about $6.6/5 = 1.3$ mrad, roughly a factor $1.5$ better than the present
$2.0$ mrad. The cheapest route is more stacks at the band edges, not more
frequencies in the middle, which the models already agree on.

**Decision criterion.** Fit both models to the extended data and compare
$\chi^2$: accept the two-component model only if the residual improvement is
significant for the two extra parameters (an $F$-test) *and* the fitted time
constants differ by more than a factor of three (here $2.257/0.021 = 107$, so the
second condition is easily met if the fit is stable). A single Cole-Cole whose
residual grows at the band edges, in a systematic pattern rather than randomly,
is the diagnostic of the mismatch.

**If the budget does not allow it.** Report both models as admissible, with their
in-band residuals and the statement that the band cannot distinguish them; report
the out-of-band difference that a future survey could measure. This is not a
failure of the analysis — it is a complete and checkable answer, and it is
strictly better than reporting one triple as though it were the structure.
