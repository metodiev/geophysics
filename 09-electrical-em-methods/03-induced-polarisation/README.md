# Module 09-03 — Induced Polarisation

**Stages:** graduate → doctoral · **Prerequisites:** modules 09-01 and 09-02;
the Fourier transform.

This module is about a measurement that is always reported as a ratio and almost
never reported with enough of its conventions. Induced polarisation measures the
part of the ground's response that *lingers* — the charge that accumulates at
blocking interfaces while a current flows and drains away when it is switched
off. Three different numbers are used to report it (a window-integral
chargeability in ms, a window-average chargeability in mV/V, and a phase in mrad),
and they are related to one another only through a model. The module treats that
relation as the object of study rather than as a conversion table: every lesson
either derives a conversion and measures its residual, or measures how much the
answer moves when the convention changes.

The second organising idea is that a polarisable ground is a **current split**.
Two conduction pathways run in parallel — an electrolyte path that polarises
weakly and a surface or electronic path that polarises strongly — and the
measured chargeability is the intrinsic polarisability of the second path
weighted by the fraction of current it carries. That single sentence explains why
clays polarise in fresh water and not in brine, why a saline plume lowers the
phase while raising the conductivity, and why two very different grounds can
produce the same spectrum. The module derives the relation and then measures its
consequences, including the cases where the data cannot settle the question.

The honesty point of the module is **non-uniqueness at three levels**: the window
(the same ground gives $23.028$ or $149.997$ ms depending on the integration
window), the model family (a single Cole-Cole and a two-component mixture are
equally admissible in a band, and differ by up to $6.6$ mrad outside it), and the
parameter set (a fitted $\tau$ moves by a factor $3.13$ when the window set
changes, with noise unchanged). No lesson presents a fitted number without the
band, the window, the model family and the residual that produced it.

**All models and data in this module are SYNTHETIC.** No sample, ore body, site,
instrument or published laboratory value is used; every number in every lesson
is printed by the demonstration in `code/`, or is an exact mathematical or
standard constant.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the step-off decay of a single-relaxation polarisable element and
   its exact window chargeability, and **convert** between the two chargeability
   conventions and the phase, stating where the conversion stops being valid.
2. **Derive** the phase of the Cole-Cole response, locate its maximum, and show
   that the Debye element is the $c = 1$ member of the family.
3. **Verify** a fitted spectrum against the Kramers-Kronig gain-phase relation,
   and **explain** why the amplitude and the phase are one measurement rather
   than two.
4. **Measure** the phase-noise law of a stacked IP measurement and **compute**
   the acquisition time a target phase resolution costs.
5. **Quantify** the bias from an incomplete charging time, from the integration
   window and from a linear drift, and state which correction removes each.
6. **Derive** the effective chargeability of a two-pathway ground and use it to
   explain the sign of the conductivity–polarisability trade-off.
7. **Report** an IP result as an admitted range with its window, band, model
   family and residual, rather than as a single fitted triple.

## Prerequisites

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md) —
  resistivity, Archie's law, surface conduction.
- [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md) —
  the four-electrode arrangement, the geometric factor and apparent resistivity.
- [01-10-02 The Fourier Transform and Its Properties](../../01-mathematics/10-fourier-analysis/02-fourier-transform.md) —
  the transform between the time and frequency domains.
- [01-11-06 Dispersion Relations and Causality in Wave Physics](../../01-mathematics/11-complex-analysis/06-dispersion-relations.md) —
  optional but recommended before lesson 02.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [IP Principle: Time-Domain and Frequency-Domain Measurement](01-ip-principle.md) | graduate | The decay is $mV_pe^{-t/\tau}$; every chargeability number is window-dependent, and the two domains are not interchangeable |
| 02 | [IP Models: Cole-Cole, Debye, Constant-Phase Element](02-ip-models.md) | doctoral | The Debye is the $c=1$ member of a family; causality makes phase and amplitude one measurement; a band's exponent is not the model's $c$ |
| 03 | [IP Acquisition, Chargeability and Phase Units](03-ip-acquisition.md) | graduate | IP is a small-signal measurement: the noise law, the cost in time, and the fact that the window set changes the answer |
| 04 | [IP for Sulphides, Clays, Contaminants and Permafrost](04-ip-applications.md) | graduate | A polarisable ground is a current split; the discriminant is the pair $(\rho_0, \varphi)$, not the phase alone |

## Suggested path

**If you are new to IP:** lessons 01 and 03 in order, running both
demonstrations. Lesson 03 is where the numbers become survey decisions.

**If you already use IP:** read 01 §3.2 (the phase peak), then 02 §3.5 (causality)
and 02 §6 (the parameter spread), then 04 §3.3 (the confusion matrices).

**If you are preparing a research project:** 02 §3.6 (band exponent against model
exponent), 03 §3.5 (window-dependent parameters), 04 §3.4 (models that are
indistinguishable in a band), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-ip-principle.md`](01-ip-principle.md) | Lesson 01 |
| [`02-ip-models.md`](02-ip-models.md) | Lesson 02 |
| [`03-ip-acquisition.md`](03-ip-acquisition.md) | Lesson 03 |
| [`04-ip-applications.md`](04-ip-applications.md) | Lesson 04 |
| [`code/`](code) | Four runnable demonstrations |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 09-electrical-em-methods/03-induced-polarisation/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_principle_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_models_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_acquisition_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_applications_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, and exits 0. None
of them opens a plot window.

## Mastery checkpoint

Complete this without notes:

> A synthetic ground has $\rho_0 = 100\ \Omega\,\mathrm{m}$, $m = 0.10$,
> $\tau = 1.5$ s and a Debye spectrum. **(a)** Compute the window-integral
> chargeability for $T = 0.5$ s and for $T = 8$ s, and state the unit of each.
> **(b)** Compute the peak phase and the peak frequency from the closed forms.
> **(c)** A survey used a $1$ s charging time; what fraction of the fully charged
> chargeability does it measure, and by what factor does a linear drift of
> $2$ mV/s over a $1$ s window change the answer? **(d)** State two models that
> would produce the same $72.987$ ms window chargeability but different phases at
> $1$ Hz, with their phases.

Worked versions of all four parts appear in the lesson
[solutions](exercises/01-ip-principle-solutions.md) and in the demonstration
`code/ip_principle_demo.py`.

## Common pitfalls across this module

1. **Quoting a chargeability without a window and a convention.** The same ground
   gives $23.028$ ms at $T = 0.25$ s and $149.997$ ms at $T = 16$ s.
2. **Treating mV/V and ms as always equal.** They coincide only for a
   one-second window.
3. **Applying a conversion factor between domains without a model.** The measured
   spread of $M/\varphi$ over eighteen synthetic models is a factor $12.25$.
4. **Inverting a phase peak height for $m$ without stating $c$.** The same
   $10$ mrad peak spans $m$ from $0.02$ to $0.10$ across the measured table.
5. **Claiming independent support from amplitude and phase agreement.** The
   Kramers-Kronig relation makes them one measurement.
6. **Fixing the charging time by habit.** It silently sets the longest
   measurable time constant; one second of charging lost $51.3\%$ of the signal
   when $\tau = 1.5$ s.
7. **Reading a phase as a mineralogy.** A phase is a current split; the same
   mineral gives different phases in different pore fluids.

## Related modules

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md) —
  the material properties that set $\rho_0$, $m$ and $\tau$.
- [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md) —
  the resistivity measurement that always accompanies IP.
- [09-04 Self-Potential and Related Methods](../04-self-potential-and-mise-a-la-masse/README.md) —
  the other electrical methods that share the electrode geometry.
- [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md) —
  the induced responses that must be separated from the IP phase.
- [08-05 Controlled-Source Electromagnetics](../../08-geomagnetism-electromagnetism/05-controlled-source-em/README.md) —
  the frequency- and time-domain induction responses.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of the non-uniqueness this module measures.
