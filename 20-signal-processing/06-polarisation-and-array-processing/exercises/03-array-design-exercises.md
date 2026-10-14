# Exercises — 20-06-03 Seismic Array Design and Resolution

Attempt these before reading the
[solutions](./03-array-design-solutions.md). The lesson is
[03 Array Design](../03-array-design.md). All models are **SYNTHETIC** teaching
values.

## ★ Foundational

**★1.** A uniform linear array has 24 sensors with 2 km spacing and records 3 Hz
waves. State the aperture, the resolution $1/(fL)$, the aliasing-free slowness
range and the expected peak sidelobe level.

**★2.** The array of ★1 is retapered with Hann weights. State the new sidelobe
level and the new half-power width (relative to uniform), and compute how many
sensors would be needed to restore the original resolution without changing the
spacing.

**★3.** A grating lobe appears at a slowness the science case requires. Name the
design change that removes it, and state the two costs that change buys.

## ★★ Applied

**★★4.** A colleague reports that a single random layout achieves $-30\ \mathrm{dB}$
sidelobes. Give two reasons to distrust the number, and state the measurement that
would settle it.

**★★5.** Design a uniform linear array for a resolution of
$0.004\ \mathrm{s\,km^{-1}}$ at 4 Hz and an aliasing-free range of
$\pm0.05\ \mathrm{s\,km^{-1}}$. Report the aperture, spacing and sensor count.

**★★6.** From the lesson's taper table, state which taper you would choose for a
study that must suppress a strong coherent source $0.02\ \mathrm{s\,km^{-1}}$ away
from the target, and justify the choice with the two numbers the table gives.

## ★★★ Research-oriented

**★★★7.** A study needs resolution $0.003\ \mathrm{s\,km^{-1}}$ at 3 Hz, no
grating lobe within $|s| < 0.15\ \mathrm{s\,km^{-1}}$, peak sidelobes below
$-25\ \mathrm{dB}$, and at most 40 sensors. Either produce a design or prove the
requirements cannot be met together, stating which must be relaxed and by how
much. A design that could not be executed is a failed answer.

**★★★8.** Using the lesson's aperture table, explain quantitatively why adding
sensors at a fixed aperture cannot improve resolution, and state what it *does*
improve. Give the numbers for going from 16 to 64 sensors at a 30 km aperture.
