# Solutions — 04-03-01 The Geologic Time Scale and Deep Time

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. The anchor age is a commonly tabulated value,
> not a fact of nature: cite the compilation.

---

## ★1 — Linear-axis resolution

Throughout, $T = 4.54 \times 10^9$ a and the length representing it is $\ell$.

**(a)** A 1 m bar is 1000 mm, so 1 mm represents

$$T \times \frac{1 \text{ mm}}{1000 \text{ mm}} = 4.54 \times 10^6 \text{ a} =
4.54 \text{ Ma}.$$

**(b)** A 100 m bar is $10^5$ mm, so 1 mm represents
$4.54 \times 10^9/10^5 = 4.54 \times 10^4$ a $= 45.4$ ka.

**(c)** A 24 h clock is 86 400 s, so 1 s represents
$4.54 \times 10^9/86\,400 = 5.25 \times 10^4$ a $= 52.5$ ka. The demo prints
`1 s of that clock is 5.255e+04 a`, which agrees.

**(d)** A figure 200 mm wide is 2000 line widths, so one line represents
$4.54 \times 10^9/2000 = 2.27 \times 10^6$ a $= 2.27$ Ma.

The last answer is the important one: on a printed linear axis for the age of the
Earth, **nothing shorter than about two million years can be drawn at all.**

---

## ★2 — Compression and ratios

**(a)** 1 Ma is 19.03 s on the 24 h clock (the demo prints this directly), so
100 Ma is $100 \times 19.03 = 1903$ s $= 31.7$ min.

**(b)** $4.54 \times 10^9 / 10^8 = 45.4$, and $\log_{10} 45.4 = 1.657$. So 100 Ma
is 1.657 orders of magnitude below the anchor.

**(c)** 1 Ga is $1000 \times 19.03 = 19\,030$ s $= 5.29$ h — more than a fifth of
the clock for a fifth of the anchor, as it must be.

**(d)** 1 per cent of $4.54 \times 10^9$ a is $4.54 \times 10^7$ a $= 45.4$ Ma.
This is the answer that matters for the interpretation of any quoted anchor:
**the tolerance you accept by not carrying the uncertainty is 45 Ma.**

---

## ★3 — The hierarchy of names

**(a)** Hadean, Archean, Proterozoic, Phanerozoic.

**(b)** Paleozoic, Mesozoic, Cenozoic.

**(c)** Cambrian, Ordovician, Silurian, Devonian, Carboniferous, Permian.

**(d)** Mesozoic: Triassic, Jurassic, Cretaceous. Cenozoic: Paleogene, Neogene,
Quaternary.

These are **names of intervals**, internationally agreed and stable. What changes
between versions of the chart is the set of ages attached to their boundaries.
A boundary in the upper part of the time scale is defined by a physical reference
point in a rock section (a GSSP); in the older part, where no suitable section
exists, by an agreed number (a GSSA). Either way the *name* is the stable object
and the *age* is a measurement that is revised.

---

## ★4 — The uncertainty of a duration

The propagation formula is
$\sigma_{\Delta}^2 = \sigma_1^2 + \sigma_2^2 - 2\rho\sigma_1\sigma_2$ with
$\sigma_1 = \sigma_2 = 5$ Ma and a duration of 100 Ma.

**(a)** $\rho = 0$: $\sigma_\Delta = \sqrt{25 + 25} = 7.071$ Ma $= 7.07$ per cent
of the duration.

**(b)** $\rho = 0.5$: $\sigma_\Delta = \sqrt{25 + 25 - 25} = 5.000$ Ma
$= 5.00$ per cent.

**(c)** $\rho = 0.9$: $\sigma_\Delta = \sqrt{50 - 45} = 2.236$ Ma
$= 2.24$ per cent.

**(d)** $\rho = 1$: the errors cancel exactly and $\sigma_\Delta = 0$.

The four answers differ because the *data* do not determine whether the two age
errors are independent. Each boundary age carries 1 per cent relative
uncertainty, yet the duration carries between 0 and 7.07 per cent, and the
statement "the duration is 100 Ma" is incomplete without the correlation
assumption. The demo's output for the same problem agrees:
`independent (rho = 0) 7.0711e+06 7.07%`.

---

## ★5 — The demo

**(a)** On the 24 h clock, 1 Ma of Earth history is 19.03 s
(`On the 24 h clock, 1 Ma of Earth history is 19.03 s.`). On the calendar-year
compression (`On the calendar-year compression, 1 Ma of Earth history is 6951.01
s`), 1 Ma is 6951 s $\approx 1.93$ h.

**(b)** `1 day of that calendar is 12.43 Ma of Earth history.`

**(c)** The demo prints

```text
anchor                                        age (a)      +/- (a)   rel. unc.
Earth (oldest Solar System solids)         4.5670e+09     1.00e+06       0.02%
Earth (accretion/age of the planet)        4.5400e+09     5.00e+07       1.10%
Universe (cosmic microwave background)     1.3800e+10     2.00e+07       0.14%
```

**(d)** The meteorite anchor's uncertainty is a measurement uncertainty on a
radiogenic isochron; it is a laboratory number with a stated analytical error.
The accretion anchor's is a range spanned by models of how a planet assembled —
a different kind of quantity, derived from a different kind of argument. The
factor of 55 between them is not a difference in measurement quality, it is a
difference in what is being estimated.

---

## ★6 — A 100 m bar

**(a)** A 100 m bar is $10^5$ mm, so recorded history of 5000 a occupies
$5000 \times 10^5/(4.54 \times 10^9) = 0.110$ mm.

**(b)** 1 mm represents $4.54 \times 10^4$ a $= 45.4$ ka, from ★1(b).

**(c)** Recorded history is 0.11 mm and the resolution is 45.4 ka, so the whole
of written history is about twice the smallest feature representable. A map at
this scale cannot show anything archaeological or historical; the youngest
geological features it can show are of order 45 ka, which is late Quaternary and
sits at the boundary of the glacially driven record
([04-05-02 Glacial and Periglacial Landforms and Sediments](../../05-geomorphology-and-quaternary/02-glacial-landforms.md)).

---

## ★7 — Displaying a short interval

**(a)** 2 Ma on a 200 mm axis for $4.54 \times 10^9$ a is
$200 \times 2 \times 10^6/(4.54 \times 10^9) = 8.81 \times 10^{-5}$ mm
$= 0.088$ µm.

**(b)** A printed line is about 0.2 mm wide, so 2 Ma is smaller than a line by a
factor of about 2300. **The claim cannot be displayed on such an axis**, not
because it is unsure but because it is invisible.

**(c)** One printed line of 0.2 mm represents
$4.54 \times 10^9 \times 0.2/200 = 4.54 \times 10^6$ a $= 4.54$ Ma. So the
shortest interval displayable at this resolution is about 4.5 Ma.

---

## ★8 — A rate and its uncertainty

**(a)** $r = 100 \text{ m}/1 \text{ Ma} = 100$ m/Ma. With independent errors,

$$\frac{\sigma_r}{r} = \sqrt{\left(\frac{5}{100}\right)^2 +
\left(\frac{0.2}{1}\right)^2} = \sqrt{0.0025 + 0.04} = 0.206,$$

so $r = 100 \pm 21$ m/Ma.

**(b)** With $\sigma(\Delta t) = 0.5$ Ma:
$\sqrt{0.0025 + 0.25} = 0.503$, so $r = 100 \pm 50$ m/Ma. The duration term
dominates entirely: the thickness is known to 5 per cent and the duration to 50
per cent, and the rate is known to 50 per cent.

**(c)** Setting the duration-only relative uncertainty to 0.5 gives
$\sigma(\Delta t) = 0.5$ Ma. Beyond that the rate is uninformative on this
definition, and the remedy is not more arithmetic — it is a better constraint on
the duration, which means the time scale rather than the tape measure.

**(d)** If the same laboratory dated both boundaries with the same standard, the
errors are positively correlated, and the correlation term subtracts. From the
formula, $\sigma_\Delta^2 = 2\sigma^2(1 - \rho)$: at $\rho = 0.9$ the duration
uncertainty falls by a factor of $\sqrt{10} = 3.16$ relative to the independent
case, at which point the thickness term in (a) dominates the rate. **The
correlation structure, not the size of the individual errors, decides which
measurement limits the result.**

---

## ★9 — Communicating deep time

**(a)** The "24 hours" compression is defensible as a teaching device and
indefensible as a quantitative one. Its numbers, computed: 1 Ma is 19.03 s;
recorded history of 5000 a is 0.095 s; and the whole of the Phanerozoic — the
only part of the record with a well-constrained boundary hierarchy — occupies a
few hours of the clock at most. The compression is honest about the *ratio* and
misleading about *where the evidence is*, because it flattens the part of the
record that is best constrained into a small fraction of the drawing.

**(b)** A quantitative alternative: a logarithmic axis with the anchor ages
labelled with their uncertainties and their compilations, plus a table of
durations in years. It sacrifices the immediate, visceral sense of scale — which
is what the compression graphic is for — and gains the property that every number
on it can be checked. The two presentations answer different questions and a
good figure says which it is answering.

**(c)** To show both $4.54 \times 10^9$ a and $10^5$ a at one printed line of
0.2 mm, the axis must be

$$\ell = 0.2 \text{ mm} \times \frac{4.54 \times 10^9}{10^5} = 9080 \text{ mm}
\approx 9.1 \text{ m}.$$

A 9-metre-wide figure is not a figure; this is the arithmetic form of the
statement that no single linear axis can carry both scales.

**(d)** The provenance. A compression graphic carries no uncertainty, no
compilation and no version of the chart, so a reader cannot tell a
radiogenically pinned boundary from a widely quoted estimate. **The one thing
that must travel with every age is where it came from**, and that is the
discipline the lesson imposes.
