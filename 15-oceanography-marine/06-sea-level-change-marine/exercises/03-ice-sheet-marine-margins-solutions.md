# Solutions — Ice Sheet Marine Margins and Stability

Worked arithmetic for
[`03-ice-sheet-marine-margins-exercises.md`](03-ice-sheet-marine-margins-exercises.md). **All models
and data are SYNTHETIC.**

## ★ Foundational

**1.1** $h_g=1.1210469\times700=\mathbf{784.7\ m}$; freeboard
$=0.1079\times784.7=\mathbf{84.7\ m}$ (check: $784.7-700=84.7$ ✓).
A bathymetric survey measures $d$ directly; $h_g$ is *inferred* through the
flotation relation, so the density assumption enters every thickness.

**1.2** $q(900)=22032\times0.9^5=22032\times0.59049=\mathbf{13010\ m^2\,yr^{-1}}$;
$q(1100)=22032\times1.1^5=22032\times1.61051=\mathbf{35483\ m^2\,yr^{-1}}$.
A 10% increase in thickness raises the flux by $1.1^5-1=\mathbf{+61.1\%}$; a 10%
decrease lowers it by $1-0.9^5=\mathbf{-41.0\%}$. The response is asymmetric and
equals the exponent's power law, not the exponent itself.

**1.3** For $h=400$ m:
$\sigma_b=917\times9.81\times400\times(1-0.89198)/2=\mathbf{0.194\ MPa}$;
$\tau_d=917\times9.81\times400\times0.01=\mathbf{0.0360\ MPa}$;
ratio $=\mathbf{5.40}=(1-\rho_i/\rho_{\text{sw}})/(2\alpha)$, independent of $h$.

## ★★ Applied

**2.1** $aW=150000\times0.25=37500\ \mathrm{m^2\,yr^{-1}}$;
$h_{\text{eq}}=1000\times(37500/22032)^{0.2}=\mathbf{1112.2\ m}$;
$d=h/1.1210469=\mathbf{992.1\ m}$. Halving the accumulation to
$aW=18750\ \mathrm{m^2\,yr^{-1}}$ gives
$h=1000\times0.85103^{0.2}=1000\times e^{-0.161275/5}=\mathbf{968.3\ m}$, a change of
$\mathbf{-12.9\%}$ for a **50%** change in supply: the fifth root again.

**2.2** (a) $d=1090+6\times15=1180$ m; $h=1.1210469\times1180=\mathbf{1322.8\ m}$;
$q=22032\times1.3228^5=\mathbf{89245\ m^2\,yr^{-1}}$, an excess of
$\mathbf{29245\ m^2\,yr^{-1}}$.
(b) $\mathrm{d}q/\mathrm{d}x=5\,(q/h)\,(1.1210469)\,(0.015)
=5\times67.46\times1.121\times0.015=\mathbf{5.67\ m^2\,yr^{-1}}$ per metre, so the
disequilibrium distance is $29245/5.67=\mathbf{5156\ m\approx5.2\ km}$.
(c) No equilibrium exists: at 5.2 km the excess has not been corrected, and because
the excess itself grows with retreat the required distance grows with it. The honest
statement is the absence of a steady state, not a retreat distance.

**2.3** $h(\beta=0.5)=1221.9\times0.5^{-0.2}=1221.9\times1.14870=\mathbf{1403.6\ m}$;
$d=\mathbf{1252.0\ m}$; inland shift $=(1252.0-1090)/10=\mathbf{16.2\ km}$.
A 50% capacity loss (a 15% thickness change) moves the grounding line 16 km.

## ★★★ Research-oriented

**3.1** (a) Melt flux $=25\times80000=2.0\times10^6\ \mathrm{m^2\,yr^{-1}}$ against a
supply of $60000\ \mathrm{m^2\,yr^{-1}}$: a ratio of $\mathbf{33.3}$.
(b) Section per unit width $=500\times80000=4.0\times10^7\ \mathrm{m^2}$, so with no
inflow $t=4.0\times10^7/2.0\times10^6=\mathbf{20\ yr}$.
(c) It is a competition ratio, not a prediction: it assumes the melt rate persists,
that inflow is negligible (in reality the shelf is fed by the discharge the
buttressing sustains), and it ignores the flow speed-up that thinning itself
induces. A prediction requires a transient flow model with a melt boundary condition
and calving.

**3.2** $33061/1334=\mathbf{24.8\ m\,yr^{-1}}$.
The units are m²/yr ÷ m = m/yr, so the quantity is a **velocity** — but it is the
extra along-flow ice velocity required to carry the excess flux through the same
section, not the speed at which the grounding line migrates.
(b) Converting flux to a grounding-line migration rate requires a kinematic boundary
condition (the rate of thickness change at the grounding line, which depends on
surface slope, accumulation and the dynamic response) plus the transient
acceleration of the ice; a static balance cannot supply either.

**3.3** (a) With $q=q_0(h/h_0)^5$ and $h=1.1210469\,d$,
$q\propto d^5$ and
$\mathrm{d}q/\mathrm{d}x=5(q/d)\,\mathrm{d}d/\mathrm{d}x$. If the bed deepens inland
($\mathrm{d}d/\mathrm{d}x>0$, retrograde), moving inward increases $d$ and therefore
increases $q$: the excess grows and the retreat is self-sustaining. If the bed
shallows inland ($\mathrm{d}d/\mathrm{d}x<0$, prograde) the flux falls below the
supply, the imbalance reverses, and the margin is pushed back out — a restoring
feedback.
(b) A prograde bed removes only this one feedback. The supply $aW$ can still fall
(catchment shrinkage, surface melt), and shelf removal by melting (§3.6) can
eliminate the buttressing that the equilibrium assumed, both of which destabilise
the margin independently of the bed slope.
