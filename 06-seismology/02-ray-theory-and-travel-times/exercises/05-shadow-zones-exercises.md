# Exercises — 06-02-05 Shadow Zones, Triplications and the Low-Velocity Zone

Attempt these before reading the
[solutions](./05-shadow-zones-solutions.md). The lesson is
[05 Shadow Zones, Triplications and the Low-Velocity Zone](../05-shadow-zones.md).
All models are **SYNTHETIC** teaching values; the global tables are printed by
`code/shadow_zones_demo.py` from the standard reference model it uses.

## ★ Foundational

**★1.** A model has a boundary at 2889 km depth below a 6371 km radius where the
P velocity falls from $13.70$ to $8.05\ \mathrm{km\,s^{-1}}$. Compute the ratio,
the percentage slowdown, and the ray parameter of a ray that grazes the boundary,
in $\mathrm{s\,rad^{-1}}$ and $\mathrm{s\,deg^{-1}}$.

**★2.** From the demo, the last direct $P$ at a 10 km source is at $98.378^\circ$
and the first core phase at $113.75^\circ$. Compute the width of the shadow in
degrees and in kilometres of surface distance (use $1^\circ = 111.195$ km).

**★3.** A stack has $v = 6.20$, then $5.80$, then $6.80\ \mathrm{km\,s^{-1}}$.
State, with the criterion, which interfaces can produce head waves and which
cannot.

## ★★ Applied

**★★4.** For the demonstration's synthetic stack ($6.00\ \mathrm{km\,s^{-1}}$
for 10 km, $5.70\ \mathrm{km\,s^{-1}}$ for 10 km, $6.50\ \mathrm{km\,s^{-1}}$ for
10 km, over a $7.50\ \mathrm{km\,s^{-1}}$ half space), compute the intercept time
and critical offset of interface 3 by hand and compare with the demo's
$\tau = 5.815471$ s and $X_c = 84.7980$ km.

**★★5.** From the demo, the numbers of $P$ arrivals at 15°, 16°, 17°, 18°, 20°,
22° and 25° are 5, 7, 5, 7, 5, 3 and 3. Explain what "7 arrivals" means
physically, state where the caustics are, and say what an inversion that assumes
one arrival per distance would do with a station at 16°.

**★★6.** In the Monte Carlo of the lesson, a head wave exists in 6.7 % of
realisations. Given a detected head wave with $\tau = 0.50$ s in a 10 km thick
layer with $v_1 = 6.00\ \mathrm{km\,s^{-1}}$ above it, invert for $v_2$. Repeat
for $\tau = 0.25$ s and state what the comparison implies about how much the
intercept tells you about the velocity near the detection threshold.

## ★★★ Research-oriented

**★★★7.** A candidate low-velocity zone (LVZ) is reported at 100–200 km depth.
Design a test that distinguishes a genuine LVZ from a hidden layer of the kind
Section 5 of the lesson builds, using only observables (arrival times *and*
amplitudes). State the prediction of each hypothesis for the first-arrival curve,
and the prediction each makes for amplitudes at the offsets where the curve is
ambiguous.

**★★★8.** From the demo, the last direct $P$ at a 10 km source is
$98.378^\circ$ and the model's velocity just above the core–mantle boundary is
$13.6906\ \mathrm{km\,s^{-1}}$. Recover the core radius and the core–mantle
boundary depth from those two numbers, state the extra assumption the recovery
needs, and say in one sentence why the recovery is a consistency argument rather
than an independent measurement.
