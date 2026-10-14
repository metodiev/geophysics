# Exercises — 05-02-02 Units and Conventions

Difficulty: ★ · ★★ · ★★★.

---

## ★ Foundational

**★1.** Derive, from the definition of the Gal, the conversion of 1 mGal to
m/s². Then convert 30 mGal to SI and to µm/s².

**★2.** Convert: (a) 1200 nT to T; (b) 0.005 S/m to mS/m; (c) 2670 kg/m³ to
g/cm³; (d) 3500 m/s to km/s. State which are exact.

**★3.** State the sign convention for gravity and the negative in
$\mathbf{g} = -\nabla\Phi$, and explain why the negative is there.

**★4.** Explain why susceptibility in SI and in cgs differ by a factor $4\pi$,
and what a factor-of-12.6 error would do to an estimated magnetisation.

---

## ★★ Applied

**★★5.** A magnetometer resolves 1 nT. What magnetic moment at 200 m produces a
1 nT axial anomaly? Express the answer in A·m², and compute the corresponding
magnetisation of a cube 20 m on a side.

**★★6.** An IP survey reports 8 mV/V. Express this as a percentage and explain
why it has no unit.

**★★7.** A magnetotelluric apparent resistivity of 120 Ω·m is reported. State
its unit, what the quantity is (measured or derived), and what would need to be
known to convert it into a true formation resistivity.

**★★8.** An anomaly of 400 nT is measured over a 48 000 nT main field. Compute
the second-order term in the $\Delta T$ approximation and state whether it
matters at the 1 nT level.

---

## ★★★ Research-oriented

**★★★9.** Write a conversion checker. Given a dictionary of quantities and
units (mGal, µm/s², nT, γ, Ω·m, mS/m, km/s, g/cm³), convert any input to SI,
verify dimensional consistency of a stated formula, and flag any mixing of SI
and cgs susceptibility. Test it on at least five formulas from this module, and
report any formula you could not check and why.

**★★★10.** Investigate a convention trap empirically: take a synthetic
susceptibility of $5\times10^{-3}$ (SI), compute the induced magnetisation in a
50 000 nT field, and then recompute treating the same number as a cgs
susceptibility. Report the ratio of the two answers, state which is larger, and
explain how you would detect the mistake in a real data set without knowing
which convention the original interpreter used.
