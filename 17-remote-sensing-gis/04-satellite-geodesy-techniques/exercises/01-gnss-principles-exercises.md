# Exercises — 17-04-01 GNSS Principles and Signal Structure

Attempt these before reading the
[solutions](./01-gnss-principles-solutions.md). The lesson is
[01 GNSS Principles](../01-gnss-principles.md). All models are **SYNTHETIC**
teaching values.

Constants: $c = 299\,792\,458\ \mathrm{m\,s^{-1}}$,
$f_1 = 1575.42\ \mathrm{MHz}$, $f_2 = 1227.60\ \mathrm{MHz}$,
first-order ionospheric coefficient $40.308\ \mathrm{m^{3}\,s^{-2}}$,
1 TECU $= 10^{16}$ electrons m$^{-2}$.

## ★ Foundational

**★1.** Write the pseudorange observation equation and list (a) the four
quantities solved for, (b) the three signals that must be *modelled or measured*
rather than solved for.

**★2.** Compute the ionospheric delay at $f_1$ and $f_2$ for 45 TECU, and verify
that their ratio equals $(f_2/f_1)^{2}$.

**★3.** A receiver has HDOP $= 1.4$ and its range noise is
$\sigma = 0.25\ \mathrm{m}$. Give the expected horizontal position scatter, and
state in one sentence why VDOP is usually larger than HDOP.

## ★★ Applied

**★★4.** Two satellites are at the same azimuth and elevation. **(a)** Write the
two rows of the design matrix and show that the geometry is singular. **(b)** State
what that implies for the DOP, and what a receiver does in practice when the
visible constellation is poor.

**★★5.** **(a)** Verify symbolically that
$a/f_1^{2} + b/f_2^{2} = 0$ for
$a = f_1^{2}/(f_1^{2}-f_2^{2})$ and $b = -f_2^{2}/(f_1^{2}-f_2^{2})$. **(b)** For
$\sigma_1 = 0.30\ \mathrm{m}$ and $\sigma_2 = 0.40\ \mathrm{m}$, compute the
ionosphere-free range noise.

**★★6.** **(a)** A solution uses six satellites and four unknowns; how many
redundant observations are there, and what do they buy? **(b)** If the range noise
is $0.5\ \mathrm{m}$ and GDOP $= 6$, give the expected 3-D position scatter.

## ★★★ Research-oriented

**★★★7.** Design an observing session to determine a monument's position to
$1\ \mathrm{cm}$ in the horizontal and $3\ \mathrm{cm}$ in the vertical. Specify:
the observation type and duration, the frequency combination, the DOP you would
insist on, the corrections you would apply, and the validation you would run.
Justify each number from the lesson. A specification that could not be executed is
a failed answer.

**★★★8.** A common delay of $5\ \mathrm{m}$ is absorbed by the clock, yet a
delay that differs between satellites moves the position. **(a)** Explain the
distinction in terms of the column of the design matrix that the delay projects
onto. **(b)** Give the general condition for a delay pattern $I_k$ to be
completely absorbed. **(c)** Relate the answer to the ionosphere-free combination:
why must $a+b=1$ hold for the combination to be usable for positioning rather than
only for ionospheric estimation?
