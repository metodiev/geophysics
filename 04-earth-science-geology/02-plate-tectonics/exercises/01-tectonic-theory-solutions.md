# Solutions — 04-02-01 Continental Drift to Plate Tectonics: The Evidence Trail

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — Stripe widths

**(a)** With the unit equality 1 mm/a = 1 km/Ma, the stripe is
$0.70 \times 25 = 17.5$ km wide.

**(b)** $2.2 \times 25 = 55.0$ km from the ridge.

**(c)** Because both flanks are created at the same ridge from the same
spreading centre, so both record the same polarity sequence at the same
distances. That symmetry is the prediction the Vine–Matthews–Morley hypothesis
makes, and it is the observation the demo tests.

**(d)** The stripes created after the change would be proportionally wider (or
narrower) than the ones before it, so the pattern would still be identifiable but
the inversion would have to fit two rates rather than one — and the boundary
between them would locate the time of the change.

---

## ★2 — Subsidence

**(a)**
$$C = \frac{2\times3300\times3\times10^{-5}\times1300}{2300}
\sqrt{\frac{10^{-6}}{\pi}} = 0.1119 \times 5.642\times10^{-4}
= 6.314\times10^{-5}\ \text{m}/\sqrt{\text{s}} .$$

**(b)** At 50 Ma, $t = 1.578\times10^{15}$ s and
$\sqrt{t} = 3.972\times10^7$, so the subsidence is
$6.314\times10^{-5} \times 3.972\times10^7 = 2508$ m.

**(c)** The empirical form gives $350\sqrt{50} = 2475$ m, against the computed
2508 m — a difference of 1.3 per cent.

**(d)** From thermal contraction: a column of rock cooled by $\Delta T$ contracts
by a fraction $\alpha\Delta T$ of its height, so the total subsidence scales as
$\alpha\Delta T$ times the thickness of the cooled layer, which grows as
$\sqrt{\kappa t}$. The density difference that drives the subsidence also involves
the contrast with seawater, which is the $\rho_m-\rho_w$ factor.

---

## ★3 — Heat flow

**(a)** $t = 25\times10^6\times3.15576\times10^7 = 7.889\times10^{14}$ s, so
$\sqrt{\pi\kappa t} = 4.978\times10^4$ and
$q = 3.2\times1300/4.978\times10^4 = 8.36\times10^{-2}$ W/m² $= 83.6$ mW/m².

**(b)** At 100 Ma, $\sqrt{t}$ doubles, so $q = 41.8$ mW/m².

**(c)** The value halves, because the law is $1/\sqrt{t}$. And the *validity*
differs: at 25 Ma the half-space model is a good description, while at 100 Ma the
real ocean floor has flattened and the measured heat flow is well below the
prediction, because the lithosphere has reached a finite thickness and because
hydrothermal circulation has removed heat.

---

## ★★4 — Inversion

**(a)** The rate is the width divided by the duration:
$40/0.90 = 44.4$ km/Ma $= 44.4$ mm/a.

**(b)** The full spreading rate is twice the half rate: 88.9 mm/a. That is a fast
ridge, comparable to the fastest spreading centres on Earth.

**(c)** The stripe's own far edge is 40 km from the ridge axis; the crust
beyond it was created later and is younger. To date the *oldest* crust in a
surveyed profile you need the furthest distance, not the widest stripe.

**(d)** The duration comes from **magnetostratigraphy**, dated independently by
radiometric ages on lavas that record reversals. That independence is what makes
the match a test rather than a circularity: if the timescale were derived from
the stripes, matching the stripes to it would prove nothing.

---

## ★★5 — Symmetry

**(a)** 15, 27, 45 and 80 km on the west flank as well, mirrored about the axis.

**(b)** The demo reports `correlation = 1.000000` for its synthetic profile.

**(c)** A correlation of about 0.2 would mean the two flanks do not carry the same
sequence. Possible causes: a non-ridge-parallel spreading direction so that the
two flanks sample different flowlines; a survey artefact; or, if the magnetisation
were genuinely unrelated on the two sides, a falsification of the hypothesis.

---

## ★★6 — Age limit

**(a)** $9000/60 = 150$ Ma.

**(b)** $9000/30 = 300$ Ma.

**(c)** Because a finite maximum age requires *destruction*: creation alone
would produce ocean floor spanning the age of the Earth, exactly as continental
crust does. The precise value of the maximum age depends on plate speeds and
ocean widths, which vary; the fact that it is finite does not, and it is the
observation that forces the existence of subduction.

---

## ★★★7 — A rate change within the pattern

**(a)** During the first 5 Ma the half-width is $5 \times 25 = 125$ km.

**(b)** From 125 to 240 km is 115 km of crust created at 40 mm/a, taking
$115/40 = 2.875$ Ma, so the crust at 240 km is $5 + 2.875 = 7.9$ Ma old.

**(c)** Stripes within the first 125 km have widths set by 25 mm/a; beyond that
they are set by 40 mm/a, so the later stripes are 60 per cent wider.

**(d)** A constant-rate inversion would recover a rate between 25 and 40,
weighted toward the part of the profile with more stripes, and it would report a
poor fit with a systematic pattern in the residuals — the signature of a model
that is too simple rather than of noisy data.

---

## ★★★8 — The demo's output

**(a)** `21 polarity intervals` spanning `27.90 Ma`.

**(b)** At 24 mm/a the misfit is `0.3021`, at 25 mm/a `0.0000` and at 26 mm/a
`0.3009`. The recovered rate is `25.0 mm/a`, matching the input.

**(c)** `correlation = 1.000000`.

**(d)** The coefficient is `6.314e-05 m per sqrt(s)`; the subsidence at 100 Ma is
`3547 m` against the empirical `3500 m`, agreeing to `+1.3 per cent`.

**(e)** Computed against empirical: 1 Ma `417.8` against `510.0`; 20 Ma `93.4`
against `114.0`; 150 Ma `34.1` against `41.6` mW/m².

**(f)** `160 Ma` at 50 mm/a over 8000 km; `143 Ma` at 70 mm/a over 10 000 km;
`200 Ma` at 30 mm/a over 6000 km.

**(g)** The bathymetry, the spreading rate and the reversal sequence are inputs —
the spreading rate is the quantity the inversion is asked to recover, and its
recovery is a check on the method rather than on the Earth. The subsidence and
heat-flow coefficients, the depths, the heat flows and the maximum ages are
computed. The thermal constants, the empirical coefficients, the Earth radius and
the densities are tabulated. The demo labels them accordingly.

---

## ★★★9 — Observation, inference and assumption

| Statement | Kind | What could falsify it |
|---|---|---|
| (a) Coastlines fit together | Observation (with a judgement about which coastline to use) | Nothing — but it is compatible with a land bridge, so it is weak evidence |
| (b) Flanks carry mirror-image stripes | Observation | A survey that found a non-symmetric pattern on a well-constrained ridge |
| (c) Reversals are globally synchronous | Inference (from the physics of a core-generated field) | Two records of the same reversal differing by more than their dating uncertainty |
| (d) Ocean floor is destroyed at trenches | Inference (from the finite age, the seismic zone and the arc volcanism) | Discovery of ocean floor older than a few hundred million years, or a demonstration that trench seismicity is unrelated to consumption |
| (e) Half-space cooling describes young ocean floor | Assumption with a stated range of validity | It already fails beyond about 70 Ma, which is why it is stated as a young-crust model |

The pattern worth noticing is that the *strongest* evidence is inference supported
by several independent observations — the finite age, the seismicity and the arc
volcanism all point to subduction — while the item that textbooks lead with, the
continental fit, is the weakest.
