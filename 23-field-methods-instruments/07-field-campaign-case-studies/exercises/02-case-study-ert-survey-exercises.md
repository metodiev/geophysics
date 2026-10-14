# Exercises — 23-07-02 Case Study: An ERT Survey from Design to Report

Attempt these before reading the
[solutions](./02-case-study-ert-survey-solutions.md). The lesson is
[02 Case Study: An ERT Survey](../02-case-study-ert-survey.md). All values are
**SYNTHETIC**.

## ★ Foundational

**★1.** A target depth of 30 m with the modelling choice $\mathrm{DOI} = L_{\max}/5$.
Compute the minimum spread, then the line length, the maximum spread and the DOI for 48
electrodes at 4 m spacing, and state whether that line reaches the target.

**★2.** Compute the number of possible four-electrode configurations for 32 electrodes, and
the count of a skip-1 α/β/γ protocol with skip levels $n = 1\ldots10$.

## ★★ Applied

**★★3.** With $\rho = 30$ Ω·m, Wenner spacing $a = 20$ m, a 200 V transmitter and 3 kΩ per
contact, compute the injected current, the potential-pair voltage, and the signal-to-noise
against a 0.3 mV per-measurement noise level. Then state which of the following you would
change first and why: the transmitter voltage, the contacts, or the number of stacks.

**★★4.** Compute the acquisition time for 2 000 measurements at 5 stacks of 0.5 s each, the
relative noise factor it buys, and the time and factor at 20 stacks.

**★★5.** For 2 000 data and meshes of 200, 2 000 and 20 000 cells, state the cells/data ratio,
whether each problem is over- or under-determined, and what the resolution claim can and
cannot say in each case.

## ★★★ Research-oriented

**★★★6.** You must map a 15 m deep, 10 m wide conductive body (a leachate plume) over a
200 m line, with the requirement that a 2× resistivity contrast be *resolvable* at the target
depth and that the survey be repeatable for time-lapse monitoring at 6-month intervals.

Design the survey: the electrode configuration with the arithmetic for depth and resolution;
the protocol and its data count; the contact requirement you would specify and the current and
voltage you expect; the stacking and the total field time; the mesh and the error model for the
inversion; the repeatability requirement with the QC that measures it; and the two things the
survey will not be able to establish.
