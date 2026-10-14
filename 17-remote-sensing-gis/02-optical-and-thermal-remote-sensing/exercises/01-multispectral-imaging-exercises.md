# Exercises — 17-02-01 Multispectral Imaging, Band Ratios and Indices

Attempt these before reading the
[solutions](./01-multispectral-imaging-solutions.md). The lesson is
[01 Multispectral Imaging, Band Ratios and Indices](../01-multispectral-imaging.md).
All spectra are **SYNTHETIC** teaching values.

Useful synthetic values from the lesson: soil-like $(\rho_{\rm red}, \rho_{\rm NIR})
= (0.42, 0.45)$; vegetation-like $(0.04, 0.48)$; water-like $(0.04, 0.02)$;
bright-like $(0.55, 0.58)$; soil line $a = 1.15$, $b = 0.06$; NDVI–LAI relation
$I_\infty = 0.90$, $I_0 = 0.10$, $k = 0.70$; alteration ratio
$R(A) = 1 + 0.8A/(A+1.5)$.

## ★ Foundational

**★1.** Compute the normalised difference index for
$\rho_{\rm red} = 0.10$, $\rho_{\rm NIR} = 0.35$. State its range in general.

**★2.** Repeat ★1 with an additive haze offset $h = 0.03$ in both bands, and
compute the absolute and relative change in the index.

**★3.** Compute the simple ratio $\rho_{\rm NIR}/\rho_{\rm red}$ for both the
vegetation-like and the water-like synthetic endmembers, and state which is
numerically unstable and why.

## ★★ Applied

**★★4.** Derive $\mathrm{d}I/\mathrm{d}x$ along a soil line of slope $a$ and
intercept $b$, where $x = \rho_{\rm red}$. Evaluate it for $a = 1.2$, $b = 0.08$,
$x = 0.25$, and estimate the index change for a soil-brightness change of
$\Delta x = 0.02$.

**★★5.** Propagate a per-band uncertainty of $\sigma = 0.015$ into the index for
the soil-like spectrum $(0.42, 0.45)$ and for the vegetation-like spectrum
$(0.04, 0.48)$. State which delivers the larger index uncertainty and explain,
using the sensitivities, why contrast alone does not determine the answer.

**★★6.** Compute the perpendicular vegetation index for a pixel with
$\rho_{\rm red} = 0.15$, $\rho_{\rm NIR} = 0.40$ using the soil line
$a = 1.15$, $b = 0.06$. Is this pixel more consistent with soil or with
vegetation? Justify with a number.

**★★7.** For the synthetic alteration ratio $R(A) = 1 + 0.8A/(A+1.5)$, invert
$R = 1.40$ for $A$, and compute $\mathrm{d}A/\mathrm{d}R$ at that point. What
abundance error does an index error of $\pm0.01$ produce?

## ★★★ Research-oriented

**★★★8.** A study reports leaf area index from a normalised difference index over
a dense canopy. Using the synthetic relation of Section 3.4, construct a
quantitative argument that the claim is unsupportable above a stated LAI, and
state the two measurements that would restore the claim.

**★★★9.** Design a two- or three-band index intended to map a notional surface
property in a scene containing both bright and dark soils. State the bands'
wavelength regions (not real sensor bands), the algebra, the error you expect from
soil-brightness variation, and the noise amplification you accept. A specification
that could not be executed is a failed answer.
