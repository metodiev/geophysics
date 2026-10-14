# Exercises — 24-06-02 DOIs, ORCID, Persistent Identifiers and Data Repositories

Attempt these before reading the
[solutions](./02-persistent-identifiers-solutions.md). The lesson is
[02 Persistent Identifiers](../02-persistent-identifiers.md). All identifiers are
**SYNTHETIC**; nothing is resolved.

## ★ Foundational

**★1.** Compute the MOD 11-2 check character for the 15-digit string
`000000021825009` by hand, and state the resulting 16-character identifier
formatted in four blocks.

**★2.** State the difference between a DOI and the URL that is often written to point
at it, and explain which one belongs in a reference list.

**★3.** A DOI prefix must be `10.NNNN` with $4$–$9$ digits, followed by a slash and a
non-empty suffix without whitespace. Decide whether each string is structurally valid:
`10.1000/abc`, `10.12/abc`, `10.1234567/`, `10.5555/data set 12`.

## ★★ Applied

**★★4.** A check-character scheme detects all single-digit substitutions. Compute how
many of $10^{6}$ identifiers are flagged at error rates of $1$ per $1000$, $1$ per
$10000$ and $1$ per $100000$, and contrast with a scheme that has no redundancy.

**★★5.** A transposition of two equal adjacent digits does not change the string at
all. Compute what fraction of digit pairs in a uniform random 16-digit identifier are
equal, and explain why the detection rate for transpositions is slightly below
$100\%$ if such cases are not excluded.

**★★6.** A structural validator rejects $66.3\%$ of a malformed corpus. Compute the
number and share accepted, and state which of the accepted strings could still be
wrong.

## ★★★ Research-oriented

**★★★7.** Design a study estimating the rate of unresolved identifiers in published
reference lists. State the corpus, the sampling, the resolution protocol with its rate
limits, the outcome definitions (dead link versus wrong target), and the reason a
resolution failure rate is a lower bound on citation error.

**★★★8.** Specify an experiment measuring whether requiring software citation in a
journal's author guidelines increases the fraction of papers citing the software they
use. State the unit, the outcome, the design, and how you would detect the software
actually used without asking the authors.
