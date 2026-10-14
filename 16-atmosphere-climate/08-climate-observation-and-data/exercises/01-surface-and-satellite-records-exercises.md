# Exercises — 16-08-01 Surface, Radiosonde and Satellite Climate Records

Attempt these before reading the
[solutions](./01-surface-and-satellite-records-solutions.md). The lesson is
[01 Surface, Radiosonde and Satellite Records](../01-surface-and-satellite-records.md).
All models and numbers are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Ten annual anomalies (K, relative to a reference period) are
$0.0, 0.1, 0.2, 0.1, 0.3, 0.4, 0.3, 0.5, 0.6, 0.7$ for years $0$ to $9$. Compute
the ordinary-least-squares trend in K/yr with its standard error.

**★2.** A truth has a trend of $+0.015\ \mathrm{K\,yr^{-1}}$. Express it in
K/decade and as the total change over a 120-year record.

**★3.** Station X has a constant offset of $+1.5\ \mathrm{K}$ and station Y a
constant offset of $-0.5\ \mathrm{K}$, both relative to the same truth. Explain
why forming anomalies removes both offsets, and state what happens to the
*trend* of each station.

## ★★ Applied

**★★4.** A step adjustment of $\delta = 0.15\ \mathrm{K}$ is applied at year 60 of
a 120-year record. Using
$\sum_t(t-\bar t)^2 = 143{,}990$ and $\sum_{t\ge60}(t-\bar t) = 1800$, compute the
trend error the step contributes and compare it with a formal standard error of
$0.0005\ \mathrm{K\,yr^{-1}}$.

**★★5.** In the demonstration, the naive mean of the raw stations fits
$+0.0168\ \mathrm{K\,yr^{-1}}$ against a true $+0.0150\ \mathrm{K\,yr^{-1}}$.
Compute the error and express it as a percentage of the truth, and explain why
adding ten more unbiased stations would not fix it.

**★★6.** A network's composition changes in year 60, with new sites carrying a
$+0.8\ \mathrm{K}$ mean offset. The composite fits $+0.0246\
\mathrm{K\,yr^{-1}}$. Separate this into the true trend and the composition
artefact, and state one reason the artefact is not removed by anomaly formation
alone.

## ★★★ Research-oriented

**★★★7.** Design a synthetic experiment to determine how large a satellite
local-time drift must be before it changes a 30-year trend by $0.005\
\mathrm{K\,yr^{-1}}$. Specify the model, the parametrisation of the drift, the
metric, and the result you would report. State one way your design could
understate the sensitivity.

**★★★8.** Two products report trends of $+0.014$ and $+0.017\
\mathrm{K\,yr^{-1}}$ over the same period, each with a formal standard error of
$0.001$ and each with an adjustment-history uncertainty you must estimate as
$\pm 0.1\ \mathrm{K}$ in one mid-record step. A colleague calls the difference
"significant at 2 sigma". Write the response, using the step-lever arithmetic and
stating what additional information would be needed to make the comparison
meaningful.
