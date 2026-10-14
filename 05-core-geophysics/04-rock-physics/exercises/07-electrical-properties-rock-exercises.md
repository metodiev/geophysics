# Exercises — 05-04-07 Electrical Properties, Archie's Law and Clay Effects

Difficulty: ★ · ★★ · ★★★.

---

## ★ Foundational

**★1.** Write Archie's law in both forms and check the dimensions.

**★2.** Derive the scaling form $R_t = R_w L_r^2/\phi$ from a tortuous-path
argument, and identify what $a$ and $m$ absorb.

**★3.** List six assumptions of Archie's law and a rock type that violates each.

---

## ★★ Applied

**★★4.** With $a = 1$, $\phi = 0.20$, $m = 2$, $R_w = 0.5$ Ω·m and
$S_w = 0.5$, $n = 2$, compute $R_t$ by forward modelling.

**★★5.** Invert the same formula to find $S_w$ from $R_t = 12$ Ω·m with
$\phi = 0.20$. Then repeat with $R_t = 30$ Ω·m and state whether the second
result is physically admissible.

**★★6.** Using the module demonstration's clay term of 0.02 S/m, compute the
total conductivity and the inferred $R_t$ at $\phi = 0.10$, $S_w = 0.4$,
$a = 1$, $m = 2$, $n = 2$, $R_w = 0.5$ Ω·m. Compare with the Archie-only $R_t$.

**★★7.** Explain physically why the clay-induced bias is always *positive* in
$S_w$.

---

## ★★★ Research-oriented

**★★★8.** Forward-model a shaly sand with an explicit clay term, then invert
with (i) Archie and (ii) a two-term model in which the clay conduction is
estimated independently. Compare the recovered saturations with the truth for a
grid of porosities and clay contents. Report the region of the grid where Archie
returns $S_w>1$, the region where it is accurate to 5%, and the sensitivity of
the conclusion to the assumed clay conductivity.

**★★★9.** Uncertainty analysis. Propagate stated uncertainties in $m$ (±0.1),
$n$ (±0.1), $R_w$ (±10%) and $R_t$ (±2%) into $S_w$ at $\phi = 0.15$ and
$\phi = 0.35$. Report which term dominates in each case, the resulting $S_w$
uncertainty, and whether an observed saturation change of 0.05 is resolvable.
