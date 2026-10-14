# Exercises — 23-06-02 Ultrasonic Velocity Measurement and Pressure Dependence

Attempt these before reading the
[solutions](./02-ultrasonic-velocity-solutions.md). The lesson is
[02 Ultrasonic Velocity](../02-ultrasonic-velocity.md). All values are **SYNTHETIC**.

## ★ Foundational

**★1.** A 30.0 mm specimen gives a transit time of 9.20 µs; a 50.0 mm specimen of the
same material gives 13.40 µs. Compute the naive velocity from the first specimen, then
the velocity and the transducer delay from the pair, and state the error the naive
velocity carries.

**★2.** Compute the minimum transducer frequency for a 25 mm specimen at 3800 m/s under
the $L \ge 5\lambda$ criterion, and the wavelength at that frequency.

## ★★ Applied

**★★3.** With $\rho = 2400$ kg/m³, $V_P = 3800$ m/s and $V_S = 2100$ m/s, compute $M$,
$G$, $K$, $\nu$, $E$ and $V_P/V_S$. Then state which of the five is most sensitive to a
1 % error in $V_S$ and give that sensitivity.

**★★4.** Using $V_P(P) = 4.50 + 5.0\times10^{-3}P - 1.2\times10^{-5}P^{2}$ [km/s, MPa],
compute $V_P$ and $\mathrm{d}V_P/\mathrm{d}P$ at 0, 75 and 150 MPa, then state what the
changing slope means physically.

**★★5.** A 40.0 mm specimen gives a net travel time of 10.53 µs, with $\delta L = 0.01$ mm
and $\delta t = 0.01$ µs. Compute the relative contributions of the length and timing
terms, the combined uncertainty in percent, and the velocity uncertainty in m/s. Then
compute the velocity error caused by a 0.15 µs delay error and state whether it is
systematic or random.

## ★★★ Research-oriented

**★★★6.** You must produce a $V_P$–$V_S$–pressure dataset for a tight sandstone at
effective pressures of 5, 20, 50 and 100 MPa, in both the loading and unloading
directions, on four plugs, with a target relative velocity uncertainty of 0.5 % and a
target $K$ uncertainty of 2 %.

Design the measurement: the specimen geometry and aspect ratio; the transducer
frequencies; the delay-calibration procedure and its frequency; the pressure sequence and
what is held constant; the number of repeats; the uncertainty budget showing that 0.5 % is
achievable; and the *checks* that would reveal a mistake. State one quantity that the
programme will not be able to defend.
