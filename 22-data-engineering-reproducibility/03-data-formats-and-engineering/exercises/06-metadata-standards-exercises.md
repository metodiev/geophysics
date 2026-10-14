# Exercises — 22-03-06 Metadata Standards and Controlled Vocabularies

Attempt these before reading the
[solutions](./06-metadata-standards-solutions.md). The lesson is
[06 Metadata Standards and Controlled Vocabularies](../06-metadata-standards.md). All
numbers refer to the **SYNTHETIC** catalogue of `code/metadata_standards_demo.py`:
200 records, 8 required fields, per-field omission rates as printed, a 9-term sensor
vocabulary mapping to 3 classes, and the unit table
{m/s^2, m/s2, gal, cm/s^2, nm/s^2}.

## ★ Foundational

**★1.** State what a reader can and cannot recover from a file that contains only the
numbers, and name the six metadata items of §2 of the file-format lesson that supply
the difference.

**★2.** For the demonstration's catalogue: (a) state the number of complete records and
the percentage; (b) compute the product of the per-field completeness probabilities
using the printed omission rates and compare it with the measured record completeness;
(c) explain in one sentence why the two differ.

**★3.** Convert $2.5\ \mathrm{gal}$ to $\mathrm{m/s^{2}}$, and $1500\
\mathrm{nm/s^{2}}$ to $\mathrm{m/s^{2}}$.

## ★★ Applied

**★★4.** A catalogue has six required fields, each missing in 4 % of records
independently.

(a) Compute the expected fraction of complete records. (b) Compute it for 12 fields.
(c) State what the figure becomes if two of the fields are missing together (a
provider that omits both), assuming the pair is missing in 8 % of records and the other
four are missing in 2 %.

**★★5.** A field declares `unit = "m/s2"` and contains the value $981$.

(a) State the two hypotheses about what the value means. (b) State the check that
distinguishes them, including the range you would test against for a strong-motion
channel. (c) State what the same check would do with a genuinely large
$0.98\ \mathrm{m/s^{2}}$ reading.

**★★6.** A colleague writes a duration parser that splits the string on `T`, reads the
digits and applies a single factor table with `M = 2\,592\,000` s (30 days).

(a) Compute what it returns for `P1Y2M3DT4H5M6S` and for `PT30M`, using
365.25 days for a year. (b) Compute the correct values. (c) State the general rule
about parsing that the example illustrates.

## ★★★ Research-oriented

**★★★7.** Design the metadata schema and validation gate for a national strong-motion
catalogue: state the required fields, the vocabularies (with their governance), the
units and their canonical forms, the time conventions, the checks performed, the
rejection policy, and what you would publish as the dictionary. State the one field
whose definition you would expect to cause the most disputes and why.

**★★★8.** The lesson's completeness model assumes independent omissions. Design a
measurement of the dependence between missing fields on a real catalogue: state the
statistic, the pattern that would show correlation, and the consequence for the
completeness estimate a consumer would compute from per-field rates alone. State what
the measurement cannot tell you about the records that are missing.

**★★★9.** A federation of five providers must present one queryable catalogue. Design
the vocabulary harmonisation: state the process for proposing, mapping and versioning
terms, the treatment of a term that maps ambiguously, the release process for a
mapping change, and the failure that would occur if the mapping were applied silently
and retroactively to old query results.
