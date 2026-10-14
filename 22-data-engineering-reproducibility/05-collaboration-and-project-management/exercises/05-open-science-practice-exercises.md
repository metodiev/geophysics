# Exercises — 22-05-05 Open Science Practice in the Geosciences

Attempt these before reading the
[solutions](./05-open-science-practice-solutions.md). The lesson is
[05 Open Science Practice in the Geosciences](../05-open-science-practice.md). Numbers
refer to the **SYNTHETIC** model of `code/open_science_practice_demo.py`: 200 groups,
logistic adoption with midpoint year 5, a reuse rate of 0.08 works per group-year, a
citation multiplier of 1.25 and an effort table totalling 109 hours.

## ★ Foundational

**★1.** List five practices that "open" can name, with the artefact each releases, and
state what a reader can check with code open but data closed.

**★2.** State the share of groups releasing openly at years 0, 6 and 12 in the
demonstration's model, and explain what the shape implies for evaluating a policy after
two years.

**★3.** State the four effort items of the release model and their hours, the total, and
the item most often forgotten.

## ★★ Applied

**★★4.** A community of 400 groups adopts an open-code policy with the same logistic shape
(midpoint year 5, steepness 0.35).

(a) Compute the adopting share at years 3 and 9 using
$N/(1 + e^{-r(t-t_0)})$. (b) State when half the community has adopted. (c) State what
the two years 3 and 9 tell a funder evaluating the policy.

**★★5.** Each adopting group produces 0.10 downstream works per year.

(a) Using the demonstration's adoption curve (29.6, 66.4, 117.3, 160.4, 184.1, 194.1 at
years 0, 3, 6, 9, 12, 15), estimate the cumulative reuse over 15 years. (b) State the
assumption the estimate rests on. (c) State two changes to the group's *release practice*
that would raise the realised reuse without changing the model.

**★★6.** A group releases a dataset under a licence that permits academic use only.

(a) State the reuse this forbids and the reuse it permits. (b) State the licence change
that would remove the restriction and the risk it introduces. (c) State how the licence
should be recorded for a reviewer to find.

## ★★★ Research-oriented

**★★★7.** Design the open-science practice for a five-year observational project with
three partner institutions, one restricted dataset, and a community that shares some of
the data under a stewardship agreement. State the access level and mechanism per dataset,
the artefacts released, the maintenance commitments, the effort budget, and the governance
decision that is not the researchers' to make. State what your practice cannot guarantee.

**★★★8.** Design a measurement of the *reuse* of a released dataset: state the data
(download counts, citation records, correspondence, derivative datasets), the statistic,
the confounders (bulk downloads, mirrors, one heavy user), and the two ways the
measurement could overstate reuse. State what the measurement cannot tell you about the
release's scientific value.

**★★★9.** A group must argue for or against an open-data policy in a proposal, using the
citation-multiplier argument. State the evidence needed to make the argument honestly, the
confounders in the literature (field, data type, journal policy, age), and the argument
you would make if the evidence were ambiguous. State what the proposal should promise
instead of a citation effect.
