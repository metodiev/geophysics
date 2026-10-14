# Exercises — 25-03-03 Project: Seismic Reflection Processing Flow

Attempt these before reading the
[solutions](./03-seismic-processing-project-solutions.md). The project is
[03 Seismic Processing](../03-seismic-processing-project.md). Values printed by
[`code/seismic_processing_demo.py`](../code/seismic_processing_demo.py):

| Quantity | Value |
|---|---|
| gather | 81 traces, offsets 0–2000 m, $\Delta t = 2\ \mathrm{ms}$, 3 s |
| primaries | $t_0 = 1.000$ s, $v_\text{rms} = 2500\ \mathrm{m\,s^{-1}}$; $t_0 = 2.000$ s, $v_\text{rms} = 3200\ \mathrm{m\,s^{-1}}$ |
| wavelet / noise | 30 Hz Ricker (33 ms), noise rms 0.08 |
| $t(x=2000)$ | $1.2806$ s (21.9% stretch); $2.0954$ s (4.6%) |
| semblance picks | $2500$ ($\pm 60$), $3200$ ($\pm 240$)$\ \mathrm{m\,s^{-1}}$ |
| NMO $+5\%$ | residual $-23.45\ \mathrm{ms}$ = 0.70 period; far amplitude $-0.1338$ |
| mute at 20% | 5 of 81 traces, from 1900 m |
| noise rms | single $0.07836$, average $0.00882$, NMO stack $0.00702$ |
| gains | $8.88$ (average) vs $\sqrt{81} = 9.00$; $11.16$ (NMO stack) |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** For $t_0 = 1.2\ \mathrm{s}$ and $v_\text{rms} = 2800\
\mathrm{m\,s^{-1}}$, compute the reflection time and the NMO stretch at
$x = 1500\ \mathrm{m}$.

**★2.** Compute the residual moveout at $x = 2000\ \mathrm{m}$ for the
demonstration's first primary when NMO uses a velocity $2\%$ too low, in
milliseconds and in fractions of a 30 Hz wavelet period.

**★3.** State what semblance measures, and compute its value for a perfectly
coherent event across 81 traces and for purely incoherent noise (both
asymptotically). Explain the two values.

## ★★ Applied

**★★4.** The velocity pick's half-maximum band is $\pm 60\
\mathrm{m\,s^{-1}}$ at $t_0 = 1$ s and $\pm 240\ \mathrm{m\,s^{-1}}$ at
$t_0 = 2$ s. Compute the moveout $t(x)-t_0$ at 2000 m for both reflectors, and
show that the ratio of the bandwidths scales as the inverse of the moveout.

**★★5.** The $20\%$ stretch mute removes 5 of 81 traces. Compute the offset at
which the stretch equals exactly $20\%$ for the first primary, state how many
traces that mutes if the threshold is tightened to $15\%$, and state the
trade-off in one sentence.

**★★6.** The simple trace average reduces the noise rms from $0.07836$ to
$0.00882$, and the NMO stack to $0.00702$. Compute both gain factors, compare with
$\sqrt{81}$, and account for the difference between the two measured gains.

## ★★★ Research-oriented

**★★★7.** You must resolve $v_\text{rms}$ to $\pm 1\%$ for a target at
$t_0 = 2.5\ \mathrm{s}$ in a survey with a maximum offset of 3000 m. Estimate the
moveout available at the far offset, the velocity resolution implied by the
semblance band, and the acquisition change (offset range, wavelet bandwidth, or
trace count) that would deliver the requirement. Then state the test on the real
data that would show the requirement is not met before a velocity is reported. A
design without that test is a failed answer.
