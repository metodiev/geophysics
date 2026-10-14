# Exercises — 25-04-02 Project: 1-D and 2-D Magnetotelluric Inversion

Attempt these before reading the
[solutions](./02-mt-1d-2d-inversion-solutions.md). The project is
[02 MT Inversion](../02-mt-1d-2d-inversion.md). Values printed by
[`code/mt_inversion_demo.py`](../code/mt_inversion_demo.py):

| Quantity | Value |
|---|---|
| model | 30 layers, 100 Ωm to 300 m, 5 Ωm to 3 km, 1000 Ωm below |
| band | 20 frequencies, 0.001–100 Hz; 2% on $\log_{10}\rho_a$, 1° on phase |
| skin depth | 5.0 km at 1 Hz in 100 Ωm |
| response | 217.429 Ωm at 0.001 Hz → 5.913 at 0.43 Hz → 81.844 at 100 Hz |
| penalties | $\alpha = 0.02, 0.2, 2.0$: $\chi^2 = 0.7150, 0.7366, 0.8033$ |
| model spread | up to 1.259 in $\log_{10}\rho$ (factor 18.2) |
| fixed-conductance scan | $\chi^2 = 106.6, 50.4, 1.12, 42.8, 179.0$ for 600–10800 m |
| distortion | $\lvert D\rvert = 1.25$, $\phi_D = 8°$ → $\chi^2 = 916.0$ |
| amplitude-only bias | $+0.194$ decade |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the skin depth in a $100\ \Omega\,\mathrm{m}$ half-space at 0.01,
0.1, 1 and 10 Hz, and state the depth range of a band spanning those frequencies.

**★2.** Verify the half-space limit of the recursion: show that a single layer
above a half-space of the same resistivity returns $Z = \sqrt{i\omega\mu_0\rho}$
and hence $\rho_a = \rho$ and $\phi = 45°$.

**★3.** The amplitude of the distortion is $\lvert D\rvert = 1.25$. Compute the
bias it produces in apparent resistivity, in decades and as a percentage, and
state why the phase part ($8°$) cannot be absorbed by any layered model.

## ★★ Applied

**★★4.** Three penalties give $\chi^{2} = 0.7150$, $0.7366$ and $0.8033$ per datum
with model spreads of up to $1.259$ in $\log_{10}\rho$. Compute the ratio of the
largest to the smallest misfit, and state in two sentences why the small misfit
difference does not license choosing the smoothest model.

**★★5.** Holding the conductance at $540\ \mathrm{S}$, compute the resistivity
required for thicknesses of 600, 2700 and 10800 m, and the misfits the demonstration
reports. Explain why the 2700 m model is the only accepted one, using the skin depth
at 0.3 Hz ($2.05\ \mathrm{km}$) in your answer.

**★★6.** A 1-D inversion of a field sounding converges to $\chi^{2} = 916$ per
datum. State the diagnosis, the two dimensionality indicators you would check, and
the inversion you would run next.

## ★★★ Research-oriented

**★★★7.** Design a dimensionality test for an MT dataset before any model is
chosen: state the quantities you would compute (including the mode split and the
tipper), the thresholds you would apply, the field-acquisition choices that make
the test possible, and the model parameterisation each outcome implies. State what
your test *cannot* detect. A design that cannot distinguish distortion from
genuine 1-D structure is a failed answer.
