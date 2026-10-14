# Exercises — 20-03-04 Phase Response, Zero-Phase Filtering and Distortion

Attempt these before reading the
[solutions](./04-phase-and-zero-phase-solutions.md). The lesson is
[04 Phase Response and Zero-Phase Filtering](../04-phase-and-zero-phase.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A 201-tap symmetric FIR filter runs at $f_s = 400$ Hz. State its group
delay in samples and in milliseconds.

**★2.** Write the group-delay definition and state the condition on the phase
response for a filter to be dispersionless.

**★3.** State what forward-backward (`filtfilt`) filtering does to the phase and
to the magnitude of a filter, in one sentence each.

## ★★ Applied

**★★4.** From the lesson's group-delay table, compute the differential delay
between 5 Hz and 55 Hz in samples and in milliseconds at $f_s = 1000$ Hz, and
state what it does to a broadband wavelet.

**★★5.** A causal filter produces $-3.01$ dB at its cutoff. State the attenuation
at the same frequency after `filtfilt`, and give the amplitude ratio in each case.

**★★6.** The lesson measures envelope asymmetry growing from 0.0092 to 0.0233
after causal filtering. Explain why a constant time shift cannot correct this.

## ★★★ Research-oriented

**★★★7.** A forward-backward filter uses two different filters $H_1$ (forward) and
$H_2$ (backward). Derive the total response and state the condition under which the
result is zero-phase.

**★★★8.** Zero-phase filtering smears energy before the first arrival. Design a
practical remedy for picking an onset that must be accurate to a few milliseconds,
and state the artifact your remedy introduces.