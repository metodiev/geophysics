# Exercises — 05-04-02 Effective-Medium Theories

Difficulty: ★ · ★★ · ★★★. Use $G_s = 44$ GPa, $K_s = 37$ GPa, $K_f = 2.2$ GPa
unless told otherwise.

---

## ★ Foundational

**★1.** Write the Voigt and Reuss averages and state the physical assumption
behind each.

**★2.** State the Hashin–Shtrikman formulas for bulk and shear modulus, naming
the host phase.

**★3.** Explain why the HS bounds are tighter than Voigt–Reuss without using any
extra information.

---

## ★★ Applied

**★★4.** Compute Voigt, Reuss and Hill $K$ and $G$ for $\phi = 0.25$ with the
stated moduli and $G_f = 0$.

**★★5.** Show that the Reuss shear modulus is zero for any $\phi>0$ when
$G_f = 0$, and state what this implies for reporting.

**★★6.** Compute the HS upper $K$ at $\phi = 0.25$ by hand from the formula and
compare with the HS lower bound.

**★★7.** Demonstrate algebraically that with $G_f = 0$ the HS lower bulk bound
equals the Reuss bound.

---

## ★★★ Research-oriented

**★★★8.** Verify the averages numerically. Assemble 200 elements with moduli
drawn from the mixture statistics in a series bar and a parallel spring bank,
solve both linear systems, and compare with the harmonic and arithmetic means.
Report the measured relative differences and state exactly what the test does and
does not prove.

**★★★9.** Write a diagnostic tool that takes measured $K$, $G$, $\phi$ and
constituent moduli and reports whether the measurement lies inside the HS
bounds. Test it on a case inside and a case outside, and state what a violation
would imply physically. Discuss why a violation is more likely to indicate bad
inputs than a new physical mechanism.
