# Exercises — 20-03-03 Filter Selection for Geophysical Data

Attempt these before reading the
[solutions](./03-filter-applications-solutions.md). The lesson is
[03 Filter Selection](../03-filter-applications.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** A 220 Hz tone is sampled at 1000 Hz and the record is decimated to 200 Hz.
Compute its alias frequency.

**★2.** A notch at $f_0 = 60$ Hz has $Q = 40$. Compute its $-3$ dB bandwidth.

**★3.** State the ordered chain of filters for a record with both a narrowband
power line inside the signal band and broadband low-frequency ground roll, and
give the purpose of each stage.

## ★★ Applied

**★★4.** Using the demo's band-energy table, explain why a single band-pass cannot
remove both the 8 Hz ground roll and the 50 Hz line from the signal at 45 Hz.

**★★5.** The demo's crude SNR falls from $-3.36$ dB to $-15.57$ dB when the notches
are applied. Explain how a processing step that removes interference can make an
SNR metric worse, and propose a metric that does not have this problem.

**★★6.** A 1000 Hz record must be decimated by 4. Identify the frequency bands that
would alias onto 0–60 Hz, and state the lowest frequency at which the anti-alias
filter must have 60 dB of attenuation.

## ★★★ Research-oriented

**★★★7.** A mains-frequency line drifts between 49.8 and 50.2 Hz over a 10-minute
record. Design a filtering strategy that removes it without a 1 Hz-wide hole in
the signal band, and state the cost in resolution.

**★★★8.** The demo shows that a 150 Hz tone decimated from 500 Hz to 125 Hz appears
at 25 Hz. Construct a chain of two successive decimations (500 → 250 → 125 Hz) and
show which stage is responsible for preventing the alias, including the
attenuation the first stage must provide at 150 Hz.