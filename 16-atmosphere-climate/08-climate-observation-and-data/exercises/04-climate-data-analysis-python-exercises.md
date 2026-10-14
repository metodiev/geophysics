# Exercises — 16-08-04 Analysing Climate Data in Python: xarray and CDO

Attempt these before reading the
[solutions](./04-climate-data-analysis-python-solutions.md). The lesson is
[04 Analysing Climate Data in Python](../04-climate-data-analysis-python.md). All
models and numbers are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Three latitude bands have area weights $\cos(\mathrm{lat})$ of $0.50$,
$1.00$ and $0.50$ and temperature values $250$, $290$ and $275\ \mathrm{K}$.
Compute the area-weighted mean and the unweighted mean, and give the difference.

**★2.** Write the area element on a sphere in spherical coordinates and explain in
one sentence why a regular latitude–longitude grid cell's area is proportional to
$\cos(\mathrm{lat})$.

**★3.** A monthly series begins in March of year 1 and is annualised with
`resample(time="YE")`. How many months does the first bin contain, and why is that
bin not an annual mean?

## ★★ Applied

**★★4.** A synthetic field warms at $0.020\ \mathrm{K\,yr^{-1}}$ over 70% of the
Earth's area and at $0.060\ \mathrm{K\,yr^{-1}}$ over the other 30%. Compute the
area-weighted global trend, the unweighted trend (assuming equal numbers of grid
points per band) and the fractional difference.

**★★5.** Two latitude bands have area weights $0.10$ and $0.90$, contain $40\%$
and $60\%$ of the grid points, and hold temperatures $270\ \mathrm{K}$ and
$280\ \mathrm{K}$. Compute (i) the correct area-weighted global mean, (ii) the
mean weighted by point count, and (iii) both means after band A is removed with
weights renormalised. Explain which method is more sensitive to the removal.

**★★6.** A $3\times 3$ block contains two contributing cell groups with areas
(relative) $1.0$ and $0.2$ and values $280\ \mathrm{K}$ and $265\ \mathrm{K}$.
Compute the plain block mean, the conservative (area-weighted) block mean, and the
difference.

## ★★★ Research-oriented

**★★★7.** Design a reproducibility test that verifies a Python (`xarray`) analysis
path and a `CDO` command-line path agree on the same synthetic NetCDF-like file.
Specify the operations to compare, the tolerance, and the two most likely causes
of a genuine disagreement (as opposed to a tolerance issue).

**★★★8.** A colleague computes the **variance** of a set of regional means by
taking the unweighted variance across grid points. Design an experiment on a
synthetic field that quantifies the resulting error as a function of the regional
area distribution, and state the general rule for which statistics require area
weighting.
