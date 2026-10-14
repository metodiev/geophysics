# Exercises — 21-05-02 Convolutional Networks for Seismic and Image Data

Attempt these before reading the
[solutions](./02-cnns-solutions.md). The lesson is
[02 Convolutional Networks](../02-cnns.md). All data are **SYNTHETIC**.

## ★ Foundational

**★1.** Write the output of a 2-D convolutional layer with $C$ input channels,
$F$ filters of size $k\times k$, and state the two operations that make it cheaper
than a fully connected layer.

**★2.** An $8\times8$ image with a horizontal band at rows $3$–$4$ is convolved
with the kernel $[[-1,-1,-1],[0,0,0],[1,1,1]]$. State which rows of the
$6\times6$ output carry the maximum response and why the interior gives zero.

**★3.** State the difference between translation **equivariance** and translation
**invariance**, and say which one a convolution provides.

## ★★ Applied

**★★4.** A $32\times32$ single-channel image with $16$ filters of $3\times3$ uses
$160$ convolutional parameters, while a fully connected layer to the same
$32\times32\times16$ output uses $16\,793\,600$. Verify both figures and compute
the ratio.

**★★5.** Compute the parameter count of the same convolutional layer if the filters
were $5\times5$ and there were $32$ of them, and compare with $160$.

**★★6.** $L$ layers of $3\times3$ stride-1 kernels give a receptive field of
$1+2L$ cells. Compute it for $L = 1, 2, 3, 6, 12$ and state the geological scale at
a $4\ \mathrm m$ sample interval for the six-layer case.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that measures whether a convolutional network's
accuracy **transfers across a lateral amplitude change** (an acquisition or gain
difference between two areas of a survey). State the design, the split, the metric,
the control and the outcome that would show the stationarity assumption has failed.

**★★★8.** Specify a study that determines whether **dilated** convolutions buy
context that a deeper stack of $3\times3$ layers cannot, at matched parameter
counts, on a target with a known long-range dependency.
