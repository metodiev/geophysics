# Exercises — 22-01-02 Version Control with Git: Branching, Rebasing, Conflicts

Attempt these before reading the
[solutions](./02-version-control-git-solutions.md). The lesson is
[02 Version Control with Git](../02-version-control-git.md). Conflict numbers
refer to the **SYNTHETIC** simulation in
`code/version_control_git_demo.py`: edit length 20 lines, merge context 3 lines,
20 000 trials per row.

## ★ Foundational

**★1.** Using the demonstration's conflict table, state the conflict probability
for two edits whose starting lines are 15, 30 and 60 lines apart, and say between
which two of those separations the risk falls by the largest factor.

**★2.** The demonstration models a wait of $W$ days as $5W$ upstream edits, each
conflicting with probability $p = 0.03$.

(a) Write the probability of at least one conflict as a function of $W$.
(b) Compute it for $W = 1$, $W = 10$ and $W = 30$ days and compare with the
printed values.

**★3.** State what each of the following is — a pointer, an object or both — and
what moves when you run `git commit`: a branch, a tag, `HEAD`, a commit.

## ★★ Applied

**★★4.** Two edits are 30 lines apart in a 900-line file. (a) Read the conflict
probability from the demonstration's table. (b) The project switches to a merge
configuration with one line of context; estimate the conflict probability by
interpolating the context table. (c) State which direction of change is safer,
and what the other direction buys.

**★★5.** A synthetic history reports 40 branches, mean lifetime
$6.9 \pm 7.3$ days, and 56 of 780 branch pairs (7.2 %) overlapping. (a) Compute
the expected number of overlapping pairs for a mean lifetime of 2 days by scaling
the observed fraction with lifetime. (b) State the assumption this scaling makes
and one way it can fail. (c) Give the daily-integration conflict probability from
the model and compare it with the 7.2 % observed.

**★★6.** You are asked to choose between two histories for a paper's software:
(A) a linear rebased history with 12 tidy commits, and (B) a merge history with
31 commits and 6 merges recording the actual order of work. For a paper's
software, argue for one and state exactly what information the other preserves
that your choice loses.

## ★★★ Research-oriented

**★★★7.** Design a measurement of the real conflict rate of a laboratory's
repository: state the population (merges), the inclusion rule, the operational
definition of a conflict, and the two confounders you would have to control
(file size and branch lifetime). Then say what the demonstration's uniform model
would predict for the same population and how the comparison would be reported.

**★★★8.** The demonstration models each upstream edit as conflicting
independently with $p = 0.03$. Specify an experiment that measures $p$ from
history and estimates its uncertainty, and state the observable that would show
independence is wrong.

**★★★9.** Semantic conflicts occur when a clean textual merge is wrong — for
example, one branch changes a constant and another changes the units of the
quantity it multiplies. Specify a test-based detection scheme, state its false
negative mode, and say what it cannot detect.
