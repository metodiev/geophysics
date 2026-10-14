# Exercises — 20-07-03 Sparse Representations for Seismic Data

Attempt these before reading the
[solutions](./03-sparsity-seismic-solutions.md). The lesson is
[03 Sparse Representations for Seismic Data](../03-sparsity-seismic.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State, in one sentence each, the difference between a *sparse
representation* claim and a *sparse inversion* claim about a seismic trace.

**★2.** A dictionary has $p = 1130$ atoms for $n = 256$ samples. Compute the
redundancy and explain why a dictionary with more atoms than samples cannot have
orthogonal columns.

**★3.** Using the coherence table (Fourier $1.7\times10^{-14}$, Haar
$9.0\times10^{-17}$, Gabor 0.9610, random 0.2861), state which dictionary you
would choose to recover a trace from 50 % of its samples and which you would
choose to denoise a complete trace. Justify each from the coherence and from the
approximation table.

## ★★ Applied

**★★4.** From the rate-distortion table, compute the reduction in relative error
obtained by doubling $k$ from 16 to 32 for Fourier (0.5436 $\to$ 0.3750), Haar
(0.5865 $\to$ 0.3990) and random (0.8095 $\to$ 0.6769). Compare with Gabor
(0.0000 $\to$ 0.0000) and state what the comparison measures.

**★★5.** In the denoising experiment the random dictionary was stopped by a
residual criterion that never fired inside 64 iterations, so it used the whole
budget and returned 6.78 dB against a 20.00 dB input. Explain how a fixed-$k$
stopping rule would obscure this, and state the diagnostic you would report
instead.

**★★6.** In the generator table the 15 Hz Ricker train is not in the dictionary,
yet Gabor wins at $k = 32$ with error 0.057 against 0.155 for Fourier. Explain
the mechanism and state one generator for which Gabor would lose.

## ★★★ Research-oriented

**★★★7.** Specify a held-out evaluation of dictionary choice for a synthetic
seismic data set with three generators, including the split, the metric, the
trial count and the way you would report an ambiguous outcome. State what the
result of the demonstration's §2 table would be under your procedure, and why
the number would differ.

**★★★8.** The lesson reports that a dictionary matched to the generator reaches
error 0.000 at $k = 16$ and that the step is exactly 8 Haar coefficients. Design
an experiment to measure how far this exactness survives a *slightly* wrong
generator: vary the generator's frequency in 1 Hz steps away from a dictionary
frequency and plot the $k = 16$ error. Predict the shape of the curve and name
the parameter that sets its width.
