# Exercises — 06-06-03 Resolution, Null Space and Model Covariance

Worked answers are in
[03-resolution-and-nullspace-solutions.md](03-resolution-and-nullspace-solutions.md).
The lesson is
[03-resolution-and-nullspace.md](../03-resolution-and-nullspace.md) and the
demonstration is
[../code/resolution_and_nullspace_demo.py](../code/resolution_and_nullspace_demo.py).

## ★ Foundational

1. On a 192-parameter grid the crossing acquisition has rank 141. Compute the
   null-space dimension and the fraction of the model space it occupies.
2. The median diagonal of $R$ is 0.618. State in one sentence what happens to a
   single-cell spike when it is imaged, and give the fraction of the estimate
   that comes from other cells.
3. A cell's model standard deviation is $8.9\times10^{-3}$ in $v/v_0$ on a
   3000 m/s reference. Convert it to metres per second and to a percentage.

## ★★ Applied

4. Using $\operatorname{tr}R = 109.3$ for 192 parameters, state the effective
   parameter count and by what factor a naive per-cell error would be
   underestimated if the count were ignored.
5. Two cells have a covariance correlation of $-0.098$ and are 7.4 km apart.
   A colleague computes the uncertainty of the *mean* of the two by adding their
   standard deviations in quadrature, each 0.9 per cent. Compute what they get,
   and what the correlation implies about the true value.
6. The known-model test gives $R^2 = 0.656$ for a one-cell checkerboard and
   $0.534$ for a 4 km one, with predicted datum rms of 24.8 ms and 51.4 ms.
   Explain why the smaller- $R^2$ pattern is the one with the *larger* data
   signature.

## ★★★ Research-oriented

7. The median point-spread length is 4.73 km in $x$ and 1.34 km in $z$ for this
   cross-hole survey. Design a second acquisition that would reduce the $x$ value
   without changing the number of rays, and predict the effect on $\operatorname{tr}R$.
8. The null-space vector of §3.2 has $\max|v|/\mathrm{rms}(v) = 3.44$ and a
   correlation of $-0.302$ with the ray count. Propose a quantitative diagnostic
   that would let a reader decide whether a *feature* in a published image is
   likely to be an image of the null space, and state what data you would need.
