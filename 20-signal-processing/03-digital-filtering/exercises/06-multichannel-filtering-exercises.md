# Exercises — 20-03-06 Multichannel and Array Filtering (f-k, Radon)

Attempt these before reading the
[solutions](./06-multichannel-filtering-solutions.md). The lesson is
[06 Multichannel and Array Filtering](../06-multichannel-filtering.md). All models
are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** An event has $p = 3$ samples/trace on an array with $\Delta x = 50$ m and
$\Delta t = 1$ ms. Compute its apparent velocity.

**★2.** State the spatial Nyquist condition for an event with slowness $p$ at
temporal frequency $f$, in cycles/sample.

**★3.** Explain in one sentence why a linear event becomes a line (not a blob) in
the f-k plane.

## ★★ Applied

**★★4.** Derive the f-k locus of a linear event $g[n,m] = w(n - pm)$ and state
what happens when the wavelet has finite bandwidth rather than being a delta.

**★★5.** From the lesson's retention table, choose a fan half-width for a survey
that must retain at least 98% of the signal and state the resulting leakage.

**★★6.** The demo retains 94.9% of an event with $p = 8.25$ samples/trace through
a filter designed to reject it. Explain this result and state what acquisition
change would prevent it.

## ★★★ Research-oriented

**★★★7.** Construct a two-event gather in which f-k filtering cannot separate the
events, and explain why a $\tau$–$p$ (Radon) transform also fails or succeeds.

**★★★8.** Derive the condition on trace spacing $\Delta x$ for an unaliased
recording of dips up to $p_{\max}$ at frequencies up to $f_{\max}$, and apply it
to a 25 Hz signal with dips up to 10 samples/trace at $\Delta t = 4$ ms.