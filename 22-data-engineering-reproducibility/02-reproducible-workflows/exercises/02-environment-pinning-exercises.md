# Exercises — 22-02-02 Pinning Environments and Managing Dependencies

Attempt these before reading the
[solutions](./02-environment-pinning-solutions.md). The lesson is
[02 Pinning Environments and Managing Dependencies](../02-environment-pinning.md).
All environment numbers use the **SYNTHETIC** model of
`code/environment_pinning_demo.py`: 40 dependencies, 3–9 admissible releases each
(mean 6.2), 60 artefacts, 2 % silent re-uploads.

## ★ Foundational

**★1.** List the six components of an environment from the lesson, and state which
of them is invisible in a `requirements.txt` file that names only direct
dependencies.

**★2.** For the demonstration's environment, the mean number of admissible
releases per dependency is 6.2 and there are 40 dependencies.

(a) Compute $\log_{10}V$ using $40\log_{10}6.2$ and compare with the printed
30.9. (b) State the probability that two unpinned installs resolve to the same
combination. (c) Explain in one sentence why the real probability of agreement is
larger than this value.

**★3.** Name the four levels of pinning and state, for each, whether it detects a
silently re-uploaded artefact at an unchanged version string.

## ★★ Applied

**★★4.** A project records hashes for 45 of its 180 artefacts, and 3 % of
artefacts are silently re-uploaded at the same version.

(a) Compute the coverage and the probability that a single silent change is
detected. (b) Compute the expected number of silent changes and the expected
number detected. (c) State what coverage the project would need to detect at least
half of them.

**★★5.** The demonstration's closure model has a branching factor of 2.2 per depth
level with a cap of 400 new packages per level, starting from 6 root packages.

(a) Reproduce the cumulative closure after 3 levels (111 packages). (b) Compute
the cumulative closure after 8 levels. (c) State the two ways this model differs
from a real dependency closure and the direction of each error.

**★★6.** A reviewer reports: "the code runs for me, but figure 3 differs in the
fourth significant digit." Name the two most likely components of the environment
responsible, and state the single change to the release that would let you decide
which one it is.

## ★★★ Research-oriented

**★★★7.** Design a release policy for a group that must reproduce its figures for
ten years: state the pinning level, the per-platform handling, the CI check, the
upgrade procedure, and the one component of the environment that no policy can
freeze. State what the policy cannot guarantee.

**★★★8.** Two of a project's dependencies are incompatible at their newest
versions, so the solver cannot satisfy all constraints. Describe how a lock-based
workflow surfaces this failure, how you would quantify the size of the infeasible
region, and why "upgrade everything" is not a solution when the offending
dependency is one you do not control.

**★★★9.** The lesson's hash table assumes the changed artefact's hash coverage is
a uniform sample. Design a measurement of *real* detection performance for a
group's lock files: state the data, the statistic, and the two ways the
measurement could overstate protection.
