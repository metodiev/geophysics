# Exercises — 25-03-05 Project: GNSS Strain Rate Estimation

Attempt these before reading the
[solutions](./05-gnss-strain-project-solutions.md). The project is
[05 GNSS Strain Rate](../05-gnss-strain-project.md). Values printed by
[`code/gnss_strain_demo.py`](../code/gnss_strain_demo.py):

| Quantity | Value |
|---|---|
| network | 12 stations, $200\times200$ km box, noise 0.5 mm yr⁻¹ |
| imposed strain | $e_{xx} = +25$, $e_{yy} = -15$, $e_{xy} = +10$; rotation $+5$ |
| imposed principal | $+27.361$, $-17.361$ nanostrain yr⁻¹ at $+13.28°$ |
| fitted gradient | $+23.636 \pm 3.147$, $+5.579 \pm 2.753$, $+9.576 \pm 3.147$, $-20.913 \pm 2.753$ |
| fitted strain | $e_{xx} = +23.636$, $e_{yy} = -20.913$, $e_{xy} = +7.577$ |
| rotation / dilatation | $+1.999$ / $+2.723$ nanostrain yr⁻¹ |
| fitted principal | $e_1 = +24.889$, $e_2 = -22.166$ at azimuth $+9.39°$ |
| residual variance factor | $s^{2} = 0.2118$ (input 0.2500) |
| inner half (6 stns) | $e_1 = +20.714$, azimuth $+16.2°$, mean 1σ $7.283$ |
| outlier $+10$ mm yr⁻¹ | $e_1 = +38.245$ ($+13.355$), residual sd $0.4603 \to 2.2185$ |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Convert $3\ \mathrm{mm\,yr^{-1}}$ of differential velocity over a 50 km
baseline to a strain rate in nanostrain per year, showing the unit algebra.

**★2.** For $e_{xx} = +20$, $e_{yy} = -5$ and $e_{xy} = +12\
\mathrm{nanostrain\,yr^{-1}}$, compute $e_1$, $e_2$, the azimuth of $e_1$, and the
dilatation rate.

**★3.** Verify the demonstration's $e_{xy} = +7.577\ \mathrm{nanostrain\,yr^{-1}}$
from the fitted coefficients $+5.579$ and $+9.576$, and state why the rotation is
$(9.576 - 5.579)/2$ rather than the negative of that.

## ★★ Applied

**★★4.** Verify the demonstration's rotation rate and dilatation from the fitted
gradient components, and compute the misfit between the fitted and imposed values
in units of the formal errors. State which component is worst determined.

**★★5.** The inner half-network has a mean formal error of
$7.283\ \mathrm{nanostrain\,yr^{-1}}$ and the whole network $2.950$. Compute the
ratio, and estimate the aperture of the inner half by assuming the 12 stations are
distributed over the 200 km box and the nearest half occupy the inner 70% of the
area. State the resolution–precision trade in one sentence.

**★★6.** The outlier test moves $e_1$ by $+13.355\ \mathrm{nanostrain\,yr^{-1}}$
and the residual sd from $0.4603$ to $2.2185\ \mathrm{mm\,yr^{-1}}$. Compute the
factor by which the residual sd inflated, compare it with the factor by which the
formal error inflated ($2.950 \to 14.218$), and state the diagnostic a practitioner
should use.

## ★★★ Research-oriented

**★★★7.** Design a GNSS network to determine the strain rate across a
100 km-wide deforming zone to a precision of $2\ \mathrm{nanostrain\,yr^{-1}}$ in
each principal rate, given single-station velocity uncertainties of
$0.5\ \mathrm{mm\,yr^{-1}}$ in each component. State the station count, the
aperture and station distribution you need, the propagation from velocity
uncertainty to strain-rate uncertainty that justifies the design, the noise-model
assumption you are making about correlation between stations, and the test that
would show the requirement is not met. A design without the covariance assumption
is a failed answer.
