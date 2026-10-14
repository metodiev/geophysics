# Exercises — 22-05-04 Research Data Management Plans and FAIR Principles

Attempt these before reading the
[solutions](./04-research-data-management-plan-solutions.md). The lesson is
[04 Research Data Management Plans and FAIR Principles](../04-research-data-management-plan.md).
Numbers refer to the **SYNTHETIC** model of
`code/research_data_management_plan_demo.py`: 8 TB/year raw, 3 TB/year derived with a
1.5× reprocessing factor, five-year project, ten-year retention, 0.02 per-copy annual
failure probability, 25 cost units per TB-year.

## ★ Foundational

**★1.** State what distinguishes a checkable data management plan from a prose one, and
give one example of each form for the retention section.

**★2.** For the demonstration's project: (a) compute the total volume after three years;
(b) compute the project total and the archived total given a ten-year retention;
(c) compute the multiplier the archive decision applies.

**★3.** Map each FAIR facet to one artefact a reviewer can open, and state the check the
reviewer performs.

## ★★ Applied

**★★4.** A project produces 20 TB/year of raw data and 8 TB/year of derived products for
three years, with a five-year retention at 25 cost units per TB-year.

(a) Compute the project total and the archived total, ignoring reprocessing.
(b) Compute the multiplier and the cost of the archive phase relative to the project
phase. (c) State which tier you would delete first if the budget were cut, and what the
deletion costs a future analysis.

**★★5.** A per-copy annual failure probability is 0.03.

(a) Compute the probability of losing an artefact in a year with one, two and three
independent copies. (b) State three pairs of copies that are *not* independent.
(c) State the test that is the only evidence a copy is usable.

**★★6.** A plan's FAIR items score 0.9 (identifier), 0.7 (metadata), 0.6 (licence),
0.8 (versioned releases), 0.4 (data dictionary), 0.3 (retention policy).

(a) Compute the mean. (b) State the two items to fix first and what each fix requires.
(c) State which facet of FAIR the two weakest items belong to, and why that is a coherent
finding rather than a coincidence.

## ★★★ Research-oriented

**★★★7.** Write the plan for a five-year project that will generate 40 TB of field data
and 15 TB/year of model output, with three institutions, one restricted dataset and a
funder requiring ten-year retention. State the inventory, standards, access and licence,
retention per tier, the failure domains and restore tests, the roles and the cost. State
the one commitment you would negotiate rather than accept.

**★★★8.** Design a measurement of whether a real archive is FAIR: state the artefacts you
inspect, the checks per facet, the scoring rule, and the two ways the measurement could
overstate compliance (metadata that exists but is wrong; a licence that is stated but not
applicable). State what the measurement cannot tell you.

**★★★9.** A group's retained raw archive is 200 TB and the budget covers 100 TB. Propose
three defensible policies (keep a subset, downsample, seek funding), state the scientific
consequence of each, and state the measurement that would let the group defend the choice
to a funder. State what the choice cannot be decided by.
