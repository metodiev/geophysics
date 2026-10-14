# Exercises — 17-06-04 Spatial Statistics, Autocorrelation and Hotspot Analysis

Attempt these before reading the
[solutions](./04-spatial-statistics-solutions.md). The lesson is
[04 Spatial Statistics](../04-spatial-statistics.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Three cells in a row have values 1, 2, 3 and rook contiguity weights. Write
the 3 × 3 weights matrix (binary), then its row-standardised form, and state
$E[I]$ for $n = 3$.

**★2.** A grid has 2 500 cells. State the number of cells expected to pass an
uncorrected two-sided 5 % test under the null.

**★3.** A permutation test uses 199 relabellings and no relabelling exceeds the
observed statistic. State the smallest p-value the test can report, and what you
would report instead of zero.

## ★★ Applied

**★★4.** A field has a lag-1 autocorrelation of 0.85 and 10 000 cells. Compute the
effective sample size and the factor by which a naive confidence interval is too
narrow.

**★★5.** A local statistic flags 900 of 10 000 cells at an uncorrected 5 % level.
Compute the expected count under the null, state what you conclude, and give the
number of cells you would expect to survive a Benjamini–Hochberg correction if the
field is pure noise.

**★★6.** Moran's I is 0.85 with rook weights and 0.78 with a distance band of radius
2. State which number you would report and what you must include with it.

## ★★★ Research-oriented

**★★★7.** Design a hotspot study for a synthetic geochemical survey that reports
the local statistic, a corrected significance class, the null model, and the
expected false-positive count. Specify the number of permutations and justify it.

**★★★8.** A study reports a significant positive spatial autocorrelation in a
mineral-occurrence dataset and concludes that occurrences cluster. Write the
critique, including the two alternative explanations that the statistic does not
exclude, and the additional analysis you would require.
