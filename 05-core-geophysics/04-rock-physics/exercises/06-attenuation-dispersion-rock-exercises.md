# Exercises — 05-04-06 Attenuation and Velocity Dispersion in Rocks

Difficulty: ★ · ★★ · ★★★.

---

## ★ Foundational

**★1.** Define $Q$ and relate it to the attenuation coefficient $\alpha$, with
units checked.

**★2.** State the Kramers–Kronig constraint and one practical consequence.

**★3.** Write the Zener $1/Q(\omega)$ and state where it peaks.

---

## ★★ Applied

**★★4.** A wave of 30 Hz travels at 3000 m/s in a rock with $Q = 80$. Compute
$\alpha$ in np/m and the amplitude remaining after 1 km.

**★★5.** Compute the fractional loss per wavelength, $2\pi/Q$, and interpret it.

**★★6.** For $\tau = 2\times10^{-3}$ s and $\Delta = 0.06$, compute the peak
frequency of $1/Q$, the value of $1/Q$ at the peak, and the total velocity
dispersion between the limits.

**★★7.** Explain why a code that applies frequency-dependent attenuation but a
frequency-independent velocity is physically inconsistent.

---

## ★★★ Research-oriented

**★★★8.** Numerically verify the Kramers–Kronig relation for the Zener element.
Compute $1/Q(\omega)$ on a logarithmic frequency grid, then compute its Hilbert
transform numerically (or the corresponding dispersion integral) and compare
with the analytically known $V(\omega)$. Report the measured agreement, the grid
range needed to avoid truncation error, and the sensitivity of the result to the
integration limits.

**★★★9.** Build a resolution-versus-depth budget. Assuming a constant $Q$ of a
stated value and a velocity of a stated value, compute the maximum frequency
that survives to depths of 500 m, 1 km, 2 km and 4 km for a stated initial
bandwidth. Convert each to a vertical resolution via $v/(4B)$ and plot (or
tabulate) resolution against depth. State the assumptions and identify the one
that would most change your conclusion.
---

**★★★10.** Derive the frequency separation between the two half-maximum points of
a single Zener element's $1/Q$ spectrum. Show that it is a fixed number of decades
*independent of the relaxation strength* $\Delta$, evaluate it, and use it as a
falsifiable test of the single-mechanism model. Then explain what a measured
$Q^{-1}$ spectrum that is nearly flat over three decades implies about the
underlying mechanism, and name two formulations that can represent such a
spectrum. State what additional measurement you would need to distinguish them.
