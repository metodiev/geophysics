# Exercises — 05-08-03 Resistivity, Induction and Laterolog Tools

Attempt these **closed-book** before opening the
[solutions](./03-resistivity-logging-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/resistivity_demo.py`](../code/resistivity_demo.py) require you to run it
and report its actual output. **Name the tool family and the averaging rule for
every resistivity number.**

Constants: $\mu_0 = 4\pi\times10^{-7}$ H m⁻¹.

---

## ★ Foundational

**★1.** State the physical measurement, and the borehole-fluid requirement, of
(a) an induction tool, (b) a focused laterolog, (c) a pad micro-resistivity tool.

**★2.** Compute the skin depth at 20 kHz for 1, 10 and 100 Ω m using the
$503\sqrt{\rho/f}$ rule, and state which value matters for a deep-reading tool.

**★3.** Convert 250 mS m⁻¹ to Ω m and state the two units a conductivity log may be
plotted in.

---

## ★★ Applied

**★★4.** Run [`../code/resistivity_demo.py`](../code/resistivity_demo.py).

(a) Report both averaging rules at the shallow and the deep weighting length and the
ratio between them at each.
(b) Explain why a 21:1 contrast produces only a 1.5 ratio at the deep weighting.
(c) State the consequence for comparing an induction log with a laterolog log.

---

**★★5.** For $R_t = 50$ Ω m, $R_{xo} = 5$ Ω m, $\phi = 0.20$, $a = 1$, $m = 2$,
$n = 2$ and $R_w = 0.10$ Ω m:

(a) compute the true $S_w$;
(b) compute the $S_w$ from a deep reading that is 20 per cent low;
(c) state the direction of the error and what governs it.

---

**★★6.** A formation has $R_w = 0.1$ Ω m at 60 °C. Using a stated temperature
coefficient for ionic mobility, compute $R_w$ at 100 °C and state the effect on the
computed saturation.

---

## ★★★ Research-oriented

**★★★7.** Implement a radial forward model of a laterolog in an invaded bed with a
stated current-focusing geometry, and compute the apparent resistivity against
invasion radius. Compare with the two-reading inversion of the lesson and report
where the inversion fails.

---

**★★★8.** Design a logging programme for a well in an oil-based mud over a thinly
bedded, anisotropic reservoir: tools, acquisition parameters, processing chain and
interpretation workflow. State which measurement limits the final saturation
uncertainty.

---

## Reference list used in this problem set

- [05-08-03 lesson](../03-resistivity-logging.md)
- [09-06-03 Downhole EM Logging and Induction Tools](../../../09-electrical-em-methods/06-borehole-electrical/03-downhole-em-logging.md)
- [Solutions](./03-resistivity-logging-solutions.md)
