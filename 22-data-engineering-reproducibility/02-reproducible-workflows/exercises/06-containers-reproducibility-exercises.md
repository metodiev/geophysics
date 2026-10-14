# Exercises — 22-02-06 Containers for Computational Reproducibility

Attempt these before reading the
[solutions](./06-containers-reproducibility-solutions.md). The lesson is
[06 Containers for Computational Reproducibility](../06-containers-reproducibility.md).
Sizes, times and drift rates refer to the **SYNTHETIC** recipe of
`code/containers_reproducibility_demo.py`: base 120 MB/0.5 min, apt 340/4.0,
python 410/6.5, data 900/2.0, code 12/0.5; drift probabilities 0.15 (apt),
0.25 (python), 0.05 (data).

## ★ Foundational

**★1.** Explain in two sentences why an image is a stack of layers and why changing
one layer invalidates every layer after it.

**★2.** Using the demonstration's recipe: (a) compute the total image size and cold
build time; (b) compute the analysis code's share of each; (c) state what the two
shares imply about where a group's effort should go when it builds a container.

**★3.** State whether each of these is pinned by a base image referenced as
`python:3.11` and by one referenced as `python:3.11@sha256:...`, and give the reason:
(a) the interpreter's patch version; (b) the system libraries inside the base;
(c) a package installed by an unpinned `pip install`.

## ★★ Applied

**★★4.** The demonstration's rebuild cascade gives 1, 2, 3 and 4 rebuilt layers for a
change to code, data, python packages and apt packages, costing 0.5, 2.5, 9.0 and
13.0 minutes. (a) Reproduce the four times from the layer table. (b) State the
recipe order that produces this cascade. (c) A colleague puts the code layer second
and the apt layer fourth; compute the rebuild time for a code change and state the
penalty.

**★★5.** With drift probabilities 0.15 (apt), 0.25 (python) and 0.05 (data), the
demonstration computes $P(\text{bitwise identical}) = 0.606$ for an unpinned build.

(a) Reproduce the calculation. (b) Compute the probability if only the apt layer were
pinned. (c) Compute the floating payload in MB and its share of the image. (d) State
what the 0.606 figure does and does not say about the two builds' results.

**★★6.** A published image is 1.78 GB and includes a 900 MB reference dataset copied
in at build time. State (a) two reasons to move the dataset out and mount it instead,
(b) the change to the provenance record this requires, and (c) one case in which
baking the data in is the better choice.

## ★★★ Research-oriented

**★★★7.** Design a container strategy for a group that must run the same analysis on
a laptop, a campus cluster and a cloud instance, over five years. State the base
image policy, the pinning, the data mounting, the CI checks, the archival choice
(for example where the digest and the recipe live), and the failure the strategy does
not remove.

**★★★8.** The demonstration measures a relative difference of $1.04 \times 10^{-7}$
between float32 and float64 summation of a million samples. Design the tolerance
policy for a regression test that runs inside a pinned image: state how you would
measure the run-to-run variation on one machine, how you would choose the tolerance,
and how you would separate a genuine regression from a platform difference. State
what the tolerance cannot detect.

**★★★9.** A colleague argues that containers "only matter for big projects" and that
a lock file is always sufficient. Construct the two cases where a lock file cannot
substitute for a container, and one case where a container is the wrong tool. Support
each with a specific component of the environment from
[22-02-02](../02-environment-pinning.md) §2.
