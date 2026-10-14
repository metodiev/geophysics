# Exercises — 13-07-03 Tectonic-Climate Feedbacks on Geological Timescales

Attempt these before reading the
[solutions](./03-tectonics-climate-feedback-solutions.md). The lesson is
[03 Tectonic-Climate Feedbacks](../03-tectonics-climate-feedback.md) and its
numbers come from
[`code/tectonics_climate_feedback_demo.py`](../code/tectonics_climate_feedback_demo.py).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the box model $\mathrm{d}N/\mathrm{d}t = F_{\text{out}} - F_w$ with
$F_w = u(N/N_0)^ae^{\beta(T-T_0)}$ and $T = T_0+S\log_2(N/N_0)$, and state the
physical meaning of $u$, $a$, $\beta$ and $S$.

**★2.** Derive the steady-state sensitivity
$\mathrm{d}\ln N/\mathrm{d}\ln F_{\text{out}} = 1/(a+\beta S/\ln 2)$ by implicit
differentiation.

**★3.** Compute $a+\beta S/\ln 2$ and the exponent for $a = 0.4$, $\beta = 0.05$
K$^{-1}$, $S = 3$ K per doubling.

## ★★ Applied

**★★4.** For those parameters, compute the temperature change for a doubling of
outgassing using the small-signal closed form, and compare with the exact
steady-state value you obtain by solving for $N$ numerically or by iterating.

**★★5.** Compute the equilibration time in units of $t^* = N_0/F_{\text{out}}$
for those parameters, and convert to years for $N_0 = 4\times10^{18}$ mol C and
$F_{\text{out}} = 1.0\times10^{13}$ mol C/yr.

**★★6.** Two parameter sets both reproduce the present state: $(a,\beta) =
(0.05,0.05)$ and $(0.80,0.20)$. Compute $a+\beta S/\ln 2$ for each and predict
the ratio of their temperature responses to the same increase in outgassing.
Compare with the lesson's measured 11.261 K and 1.801 K.

**★★7.** A weathering-efficiency ramp doubles $u$ over 10 Myr. Using the
equilibration time from ★5, decide whether the climate response is complete by the
end of the ramp, and state what observable would reveal a lag if it were not.

## ★★★ Research-oriented

**★★★8.** Write the validation statement a study would need to make before
claiming that Cenozoic cooling was caused by mountain building. Name the
observation that would discriminate it from a climate-feedback explanation, and
say what that observation would have to look like in time and in space.

**★★★9.** Design a synthetic recovery test for $a$ and $\beta$ from a synthetic
dataset consisting of (i) a temperature record and (ii) an outgassing proxy of
stated uncertainty. State the metric, the expected degeneracy, and the precision
in the outgassing proxy required to break it.

**★★★10.** The model has no ocean buffering, no organic carbon and no carbonate
weathering. Rank these three omissions by the size of the error you expect in
(a) the equilibration time and (b) the steady-state sensitivity, and justify the
ranking with an argument about timescales rather than with numbers.
