# Exercises — 01-10-02 The Fourier Transform and Its Properties

Attempt these **closed-book** before opening the
[solutions](./02-fourier-transform-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Throughout, the convention is the one used in the lesson:

$$X(f) = \int_{-\infty}^{\infty} x(t)e^{-2\pi i f t}\,dt, \qquad
x(t) = \int_{-\infty}^{\infty} X(f)e^{+2\pi i f t}\,df .$$

---

## ★ Foundational

**★1.** State the forward kernel used here, and the values of
$\mathcal F\{e^{-\pi t^2}\}$, $\mathcal F\{e^{-\pi(t-3)^2}\}$ and
$\mathcal F\{e^{-\pi(2t)^2}\}$.

---

**★2.** A boxcar is $1$ for $|t| \le 1$ s and $0$ elsewhere, so $T = 2$ s.

(a) Write down $X(f)$ in closed form.
(b) Evaluate $X$ at $f = 0$, $0.25$, $0.5$, $0.75$ and $1.0$ Hz to three
significant figures.
(c) State where the zeros of $X$ are, and why they are where they are.

---

**★3.** For $x(t) = e^{-\pi t^2}$ write down, without recomputing any integral,
the transforms of

(a) $x(t) + 4x(t)$,
(b) $x(t)\cos(2\pi\cdot5t)$,
(c) $x(t - 0.25)$,
(d) $x(10t)$.

---

**★4.** Given a spectrum $X(f)$, write the spectra of $\dfrac{dx}{dt}$ and
$\dfrac{d^2x}{dt^2}$. Hence state the wavenumber-domain form of the second
derivative with respect to $x$ of a field $g(x)$.

---

## ★★ Applied

**★★5.** The central difference of a sampled function with step $h$ is
$D_h x = (x(t+h)-x(t-h))/(2h)$.

(a) Derive its transfer function and show that it is
$i\sin(2\pi f h)/h$ times the input spectrum.
(b) At which frequency is the response exactly zero?
(c) Compute the amplitude ratio $\lvert H\rvert/\lvert 2\pi f\rvert$ at
$f = 30$ Hz for $h = 2$ ms and $h = 4$ ms.
(d) A colleague computes a vertical derivative of a gravity grid with $h = 100$ m
and interprets the result as a derivative up to 1 Hz. Comment quantitatively.

---

**★★6.** For $x(t) = e^{-\lvert t\rvert}$ the transform is
$X(f) = \dfrac{2}{1+(2\pi f)^2}$.

(a) Compute $\int_{-\infty}^{\infty}\lvert x(t)\rvert^2dt$ exactly.
(b) Compute $\int_{-\infty}^{\infty}\lvert X(f)\rvert^2df$ exactly, using
$\int_{-\infty}^{\infty}\frac{du}{(1+u^2)^2} = \frac{\pi}{2}$.
(c) State which relation you have just verified.

---

**★★7.** A colleague transforms an hourly time series with $dt = 3600$ s and
$N = 24$ samples. The zeroth DFT bin is $12345.0$.

(a) What is the mean of the 24 samples?
(b) What is $\int x(t)\,dt$ over the record, to four significant figures?
(c) What is $X(0)$, the value of the *continuous* transform at zero frequency?
(d) The same colleague then reports $X(0) = 12345$. Which of the three has been
confused with which?

---

**★★8.** The forward difference has transfer function
$(e^{i\omega h}-1)/h$.

(a) Show that its modulus is $2\lvert\sin(\omega h/2)\rvert/h$.
(b) Show that this is strictly less than $\omega$ for all $\omega > 0$, so the
forward difference never matches the ideal derivative in amplitude.
(c) Evaluate the ratio at $\omega h = \pi/2$ and $\omega h = \pi$.
(d) State the phase error of the forward difference as a function of $\omega h$,
and explain why it matters more than the amplitude error for dipping events.

---

## ★★★ Research-oriented

**★★★9.** A potential field measured on a plane can be continued upward by
multiplying its wavenumber spectrum by $e^{-2\pi f h}$, where $h$ is the height
increased and $f$ the spatial frequency (cycles per metre). This is a standard
consequence of Laplace's equation.

(a) Derive the factor from the requirement that the continued field satisfy
Laplace's equation in the half-space above the observation plane and match the
observed field at $h = 0$.
(b) Tabulate the factor and its reciprocal for $h = 1$ km at wavelengths 100, 20,
10 and 5 km.
(c) Downward continuation by 5 km at 5 km wavelength: what is the amplification
factor?
(d) A gravity survey has noise at the 0.02 mGal level and a signal of 2 mGal at
20 km wavelength. Continuing downward 5 km, at what wavelength does the noise
reach the level of the signal, and what does that imply for interpretation?
(e) State the two engineering devices routinely used to keep downward
continuation usable.

---

**★★★10.** For a real signal $x(t)$ define

$$\sigma_t^2 = \frac{\int t^2\lvert x\rvert^2dt}{\int\lvert x\rvert^2dt},
\qquad
\sigma_f^2 = \frac{\int f^2\lvert X\rvert^2df}{\int\lvert X\rvert^2df}$$

(for signals with zero mean time and zero mean frequency, i.e. $\bar t = 0$ and
$\bar f = 0$).

(a) Compute $\sigma_t$ and $\sigma_f$ analytically for $x(t) = e^{-\pi t^2}$,
using $\int t^2e^{-2\pi t^2}dt = \frac{1}{4\pi}\sqrt{\frac{\pi}{2\pi}}$.
(b) Show that the product is $1/(4\pi)$ for any $x(t) = e^{-\pi(at)^2}$.
(c) The supplied script
[`code/fourier_transform_demo.py`](../code/fourier_transform_demo.py) measures
the same quantity numerically for $a = 0.5, 1, 2, 4$. Report its values and
compare with your analytical result.
(d) A textbook states $\Delta t\,\Delta f \ge 1/2$. Under what convention is
that statement equivalent to the one here?
