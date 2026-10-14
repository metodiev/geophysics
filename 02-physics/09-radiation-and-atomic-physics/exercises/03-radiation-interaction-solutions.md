# Solutions — 02-09-03 Interaction of Radiation with Matter

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Every attenuation coefficient below is labelled either **computed** (from the
Klein–Nishina cross section) or **tabulated** (from a photon cross-section
compilation, in which case the compilation and the energy must be cited). A
report that does not make that distinction cannot be checked.

---

## ★1 — Attenuation arithmetic

**(a)** $\mathrm{HVL} = \ln 2/\mu = 0.693\,147/1.25 = \mathbf{0.5545}$ cm.

**(b)** $\ln 10/\mu = 2.302\,585/1.25 = \mathbf{1.842}$ cm.

**(c)** $x = \ln 100/\mu = 4.605\,170/1.25 = \mathbf{3.684}$ cm.

**(d)** $\phi/\phi_0 = e^{-1.25 \times 2.0} = e^{-2.5} = \mathbf{0.0821}$, so
8.2 per cent is transmitted. The exponential law assumes each interaction
removes the photon from the beam, i.e. a narrow beam with no scattering back
into it. In a broad geometry, scattered photons still arrive at the detector and
the true transmission is *higher*; the correction is the build-up factor, which
for a thick shield can exceed 2. The exponential is therefore a lower bound on
transmission and an under-estimate of the required thickness.

---

## ★2 — Compton kinematics

**(a)** $\alpha = 1.3325/0.510\,998\,95 = \mathbf{2.6077}$.

**(b)** $E' = E/[1 + \alpha(1 - \cos\theta)]$ with $\cos\theta = -1$:
$E' = 1.3325/(1 + 2 \times 2.6077) = 1.3325/6.2154 = \mathbf{0.2144}$ MeV =
214.4 keV.

**(c)** The deposited energy is $E - E' = 1.3325 - 0.2144 =
\mathbf{1.1181}$ MeV. This is the **Compton edge** for that line.

**(d)** At $90^\circ$, $\cos\theta = 0$ and
$E' = 1.3325/(1 + 2.6077) = \mathbf{0.3691}$ MeV. The Compton edge is the
*maximum* deposited energy because the deposition is largest when the photon
recoils straight back, i.e. at $\theta = 180^\circ$; every other angle deposits
less, so the continuum has a sharp upper terminus there.

---

## ★3 — Compton attenuation in water

**(a)** $\mu/\rho = (Z/A)N_A\sigma$. With $Z/A = 0.5551$,
$N_A = 6.022\,140\,76 \times 10^{23}$ mol⁻¹ and
$\sigma = 0.25614 \times 10^{-24}$ cm²:
$\mu/\rho = 0.5551 \times 6.022\,14 \times 10^{23} \times 0.25614 \times 10^{-24}
= \mathbf{0.08562}$ cm² g⁻¹. The demo prints 0.085554 using its own $Z/A$ and a
tiny difference in the cross section; agreement to 0.1 per cent.

**(b)** $\mu = 0.085\,62 \times 0.998 = 0.085\,45$ cm⁻¹. (The demo's table gives
0.08538 cm⁻¹ from its slightly different $\mu/\rho$.)

**(c)** $\mathrm{HVL} = \ln 2/0.085\,45 = \mathbf{8.11}$ cm. The demo's
illustrative table used $\mu = 0.0870$ cm⁻¹ for water and got 7.97 cm, so the
two agree to 2 per cent — which is the point: the illustrative value is a
reasonable stand-in, and the *difference* between the two is the size of the
input uncertainty in a real calculation.

**(d)** For water at 662 keV the Compton process is dominant, so the computed
value is close to the measured total: the photoelectric term is negligible
because $Z$ is low and the photon energy is well above the K edge of oxygen. For
lead, $Z$ is 82 and the photoelectric term is *not* negligible even at 662 keV,
so the Compton-only value (0.69225 cm⁻¹ from the demo) underestimates the true
total — the compilation's $\mu/\rho$ of order 0.1 cm² g⁻¹, times 11.34 g cm⁻³,
is about a factor of 1.6 larger.

---

## ★★4 — Photoelectric scaling

**(a)** $(Z_\mathrm{Pb}/Z_\mathrm{Fe})^n = (82/26)^n$: for $n = 4$,
$3.1538^4 = \mathbf{98.9}$; for $n = 4.5$,
$3.1538^{4.5} = \mathbf{175.7}$.

**(b)** $(90/30)^3 = 3^3 = \mathbf{27}$. The cross section falls by a factor of
27 for a factor of three in energy, which is why low-energy photons are used for
thin specimens and why the contrast collapses at high energy.

**(c)** Contrast comes from the difference in attenuation between the two
materials, and that difference is dominated by the photoelectric term, which
scales as $Z^n$ with $n \approx 4$ to 5. At 30 keV, calcium ($Z = 20$) and water
(a low effective $Z$) differ by a large factor in $\sigma_\mathrm{pe}$. At
300 keV the photoelectric term has fallen by $(300/30)^3 = 1000$ relative to the
Compton term, so both materials attenuate by nearly the same Compton
coefficient and the contrast collapses. This is why radiography uses the lowest
energy that will penetrate the specimen.

**(d)** The scalings give the *trend* and the *ratios* and not the absolute
cross section, because the constants in front were absorbed; and they say nothing
about the K edges, where the cross section jumps by a factor of five to ten over
a few keV. A calculation within a factor of two of an edge must use tabulated
values at the actual energy.

---

## ★★5 — Alpha ranges

**(a)** $R\rho = 3.6688\ \mathrm{cm} \times 1.205 \times 10^{-3}\
\mathrm{g\,cm^{-3}} = \mathbf{4.421 \times 10^{-3}}$ g cm⁻².

**(b)** $R = 4.421 \times 10^{-3}/2.65 = 1.668 \times 10^{-3}$ cm =
**16.7 µm**. So an alpha from a mineral grain of a few tens of micrometres cannot
escape it, which is why alpha spectrometry of rocks requires either a very thin
source or chemical separation.

**(c)** $3.6688/3.10 = \mathbf{1.183}$ cm.

**(d)** The range ratio for a factor of two in energy is 3.1, not 2, because the
stopping power falls as the particle speeds up: $-\mathrm{d}E/\mathrm{d}x
\propto 1/E$ at non-relativistic energies, so the range grows faster than the
energy. The implication for spectrometry is that alphas of different energies
are separated by a *stretching* of the track, which is why a thin source gives
sharp lines (each alpha emerges with its full energy) and a thick source gives a
featureless continuum of degraded energies (each alpha emerges having lost a
variable amount of energy in the source).

---

## ★★6 — Beta energy deposition

**(a)** From the demo's table: for $Q = 0.156$ MeV, mean $T/Q = 0.34752$; for
$Q = 2.280$ MeV, 0.43101. (The corresponding modal values are 0.22510 and
0.40910.)

**(b)** Mean energy per decay: $0.156 \times 0.34752 = \mathbf{0.0542}$ MeV;
$2.280 \times 0.43101 = \mathbf{0.9827}$ MeV.

**(c)** $10^6$ decays at 0.0542 MeV: $10^6 \times 0.0542 \times 1.602\,176\,634
\times 10^{-13}$ = $\mathbf{8.69 \times 10^{-9}}$ J. At 0.9827 MeV:
$10^6 \times 0.9827 \times 1.602\,176\,634 \times 10^{-13} =
\mathbf{1.574 \times 10^{-7}}$ J. The ratio is 18.1, i.e. more than the ratio of
end points (14.6), because the mean-to-end-point ratio rises with energy.

**(d)** Because the emitted electron shares the available energy with an
antineutrino, so the *spectrum* is continuous and a single number must be a
convention. The convention is the end point $Q$, which is a nuclear quantity. The
top 1 per cent of the energy range carries about $5.15 \times 10^{-4}$ per cent of
the decays for a 1.311 MeV emitter (the demo's figure), i.e. about five parts per
million — which is why beta end points are fitted by extrapolating a Kurie plot
rather than read from the last channel.

---

## ★★★7 — Running the demo

**(a)** Smallest relative difference $6.02 \times 10^{-16}$ at 2 MeV; largest
$4.91 \times 10^{-9}$ at 0.001 MeV. The larger residual at the lowest energy is
the quadrature at work on a nearly isotropic integrand with 400 000 intervals;
even so it is nine significant figures of agreement.

**(b)** Computed Thomson limit $8\pi r_e^2/3 = 0.6652459$ barn; tabulated value
0.6652459 barn; relative difference $7.55 \times 10^{-12}$. Two independently
obtained numbers agreeing to twelve figures is the strongest kind of check
available here.

**(c)** Compton-only $\mu = 0.69225$ cm⁻¹, giving an HVL of
$\ln 2/0.69225 = 1.0013$ cm. The total measured value is smaller because of the
photoelectric contribution.

**(d)** $3.66876$ cm against the commonly tabulated $\approx 4$ cm: a ratio of
0.92, i.e. 8 per cent low. The stated reason is that the Bethe bracket changes
sign below about 0.16 MeV for an alpha in air, so the integral is truncated at a
0.30 MeV cutoff, which omits a few millimetres of track.

**(e)** 3.10.

**(f)** Exact: the Klein–Nishina cross section, the Compton kinematics, the
pair-production threshold, the exponential attenuation law, and the specific
activity relations. Model results with a stated cutoff or a declared input: the
alpha stopping power and range (truncated integral, tabulated $I$), the
Compton-only attenuation coefficient quoted as if it were the total, and the beta
spectrum shape (allowed shape without the Coulomb factor).

---

## ★★★8 — A lead shield

**(a)** $x = \ln(1000)/0.69225 = 6.9078/0.69225 = \mathbf{9.98}$ cm.

**(b)** $\mu = 0.1 \times 11.34 = 1.134$ cm⁻¹ (taking $\mu/\rho = 0.1$ cm² g⁻¹ and
$\rho = 11.34$ g cm⁻³), so
$x = 6.9078/1.134 = \mathbf{6.09}$ cm.

**(c)** The ratio is $9.98/6.09 = 1.64$, so the Compton-only calculation
overestimates the thickness by 64 per cent. The direction follows from $x \propto
1/\mu$: a smaller $\mu$ means less attenuation per centimetre, so more
centimetres are needed for the same attenuation factor, and the Compton-only
answer is the **larger** one. It is therefore *conservative* for a shielding
design — the shield will be thicker than necessary — and it is still wrong by 64
per cent, which is decisive for the cost, the mass and whether the shield fits
into the geometry at all. State the direction explicitly in your own answer; an
error that happens to be safe is not thereby a defensible calculation.

**(d)** The omission is systematic because the photoelectric contribution is
always present and always positive for a high-$Z$ material at this energy, and it
does not average out over several lines, several energies or several absorbers
the way a random error would. Its size grows as $Z^4$ to $Z^5$, so the
underestimate is worst for exactly the materials a designer reaches for. Any
calculation that depends on the difference between the Compton-only and the total
coefficient for a heavy element must take the total from a compilation, cite the
compilation and the edition, and state the photon energy at which it was
evaluated.
