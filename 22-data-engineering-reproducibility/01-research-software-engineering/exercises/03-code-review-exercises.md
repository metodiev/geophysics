# Exercises — 22-01-03 Code Review and Collaborative Development

Attempt these before reading the
[solutions](./03-code-review-solutions.md). The lesson is
[03 Code Review and Collaborative Development](../03-code-review.md). All
detection numbers use the **SYNTHETIC** model in `code/code_review_demo.py`:
density $\rho = 8$ defects/kLOC, inspection rate $R = 200$ lines/h,
$p_{\text{det}} = 1 - e^{-0.90\,t}$ with $t$ in hours.

## ★ Foundational

**★1.** A change is 50 lines long. Compute the inspection time $t$ in
person-hours, the detection probability $p_{\text{det}}$, and the escaped defects
per kLOC. Compare with the demonstration's row for 50 lines.

**★2.** For a detection probability $p = 0.593$ (a 200-line change), compute the
detection probability of two independent reviewers and the escaped defects per
kLOC for one and for two reviewers. Compare with the demonstration's 3.25 and
1.32.

**★3.** Explain in two sentences why the *total* defects found in review rise with
change size while the escaped defects *per kLOC* also rise with size for small
changes and fall for large ones.

## ★★ Applied

**★★4.** Find the change size at which the escape rate falls to 2 defects per kLOC
by solving $8\,e^{-0.9L/200} = 2$, and check the answer against the
demonstration's table (3.25 at 200 lines, 1.32 at 400 lines).

**★★5.** A 800-line change is reviewed in 40 minutes instead of the 4.0 hours the
model allocates. Compute $t$, $p_{\text{det}}$ and the escape rate, and express the
escape rate as a multiple of the fully-inspected value.

**★★6.** Review this function and list every defect you can find, with the
consequence of each:

```python
def normalise(x, scale):
    y = x * scale            # x is float32, scale is float64
    z = y - y.mean()         # y.mean() over the whole array
    return z / y.std()       # population standard deviation
```

Then state which of the identified items a unit test could catch and which it
could not.

## ★★★ Research-oriented

**★★★7.** Design an experiment that estimates $p_{\text{det}}(L)$ empirically in a
research group: state the treatment, the unit of analysis, the
defect-identification method, and how you would avoid circularity (the reviewer's
own opinion of what a defect is). State the sample size you would need to
distinguish a 30 % detection rate from a 50 % one at 95 % confidence.

**★★★8.** Two reviewers are not independent: they share the same reading order
and the same misconceptions. Propose a model that adds a dependence parameter,
state its mathematical form, and describe the measurable quantity that would
estimate it.

**★★★9.** A defect that escapes review costs a fixed $C$ person-hours to fix
later, and review costs $R$ person-hours per kLOC. Using the model of §3, write
the expected total cost as a function of review effort per kLOC and find the
effort that minimises it. State the two assumptions that make the answer
unreliable, and what a laboratory should measure before using it.
