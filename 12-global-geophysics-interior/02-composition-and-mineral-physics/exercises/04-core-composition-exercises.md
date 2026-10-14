# Exercises — 12-02-04 Core Composition, Light Elements and the Geodynamo

Attempt these before reading the
[solutions](./04-core-composition-solutions.md). The lesson is
[04 Core Composition, Light Elements and the Geodynamo](../04-core-composition.md).
All models are **SYNTHETIC**. Unless stated otherwise use the model's printed values:

- CMB at $R_c = 3480$ km ($g = 10.559$ m s$^{-2}$), ICB at
  $R_\text{ICB} = 1221.5$ km ($g = 4.456$ m s$^{-2}$), $P_\text{CMB} = 126.2$ GPa,
  $P_\text{ICB} = 315.0$ GPa;
- outer-core density 9.90 g cm$^{-3}$ at the CMB to 12.15 g cm$^{-3}$ at the ICB;
- pure iron at core conditions $\rho_\text{Fe} = 10.794$ (CMB) and
  $12.874$ g cm$^{-3}$ (ICB); solid iron at the ICB 13.260 g cm$^{-3}$;
- $C_p = 800$ J kg$^{-1}$ K$^{-1}$, $\alpha = 10^{-5}$ K$^{-1}$, core mass
  $1.90\times10^{24}$ kg, core heat capacity $1.53\times10^{27}$ J K$^{-1}$;
- adiabatic gradient at the CMB $5.28\times10^{-4}$ K m$^{-1}$;
- latent-heat coefficient $L\rho_\text{ICB}4\pi R_\text{ICB}^{2}/D
  = 4.74\times10^{26}$ J K$^{-1}$ for $D = 1.26\times10^{-4}$ K m$^{-1}$.

## ★ Foundational

**★1.** Integrate $dP/dr = -\rho g$ through the outer core by hand, treating both
$\rho$ and $g$ as linear in $r$, and compare the result with
$P_\text{ICB} - P_\text{CMB}$. State why the hand result is 1 % low.

**★2.** At the ICB the model density is 12.150 g cm$^{-3}$ and pure liquid iron is
12.874 g cm$^{-3}$. With an assumed light-element density of 6.0 g cm$^{-3}$, compute
the light-element mass fraction and the density deficit in per cent.

**★3.** Using $\alpha = 10^{-5}$ K$^{-1}$, $g = 4.456$ m s$^{-2}$, $T = 4963$ K and
$C_p = 800$ J kg$^{-1}$ K$^{-1}$, compute the adiabatic gradient at the ICB in
K km$^{-1}$. Then multiply it by the outer-core thickness to predict the temperature
rise, and explain why the answer differs from the model's 963 K.

## ★★ Applied

**★★4.** Compute the conducted heat flow $Q_\text{ad}$ at the CMB for
$k = 75$ W m$^{-1}$ K$^{-1}$. With an assumed total CMB heat flow of 10 TW, find the
cooling rate in K Myr$^{-1}$ and the inner-core age in Gyr, with and without latent
heat. State how much of the budget is left for the dynamo.

**★★5.** The model's ICB density jump is 0.60 g cm$^{-3}$, of which 0.39 g cm$^{-3}$
comes from melting pure iron. Compute the inner-core density that would follow if
there were *no* compositional change across the ICB, evaluate the resulting deficit
against the solid-iron reference, and explain what the difference from the model's
12.750 g cm$^{-3}$ implies.

**★★6.** Take the CMB light-element fraction (7.8 mass %) as uniform through the
outer core and compute the ICB density that the mixing model predicts with
$\rho_\text{L} = 6.0$ g cm$^{-3}$. Compare with the model's 12.150 g cm$^{-3}$,
express the mismatch in per cent, and list two physical ways to remove it.

**★★7.** A dynamo model uses $\sigma = 5\times10^{5}$ S m$^{-1}$,
$U = 8\times10^{-4}$ m s$^{-1}$ and $L = 2258$ km. Compute the magnetic diffusivity,
the magnetic Reynolds number and the magnetic diffusion time. Is dynamo action
plausible?

## ★★★ Research-oriented

**★★★8.** Design a workflow that would distinguish oxygen from silicon as the
dominant light element. List the observations and calculations in order, state the
discriminating quantity at each step, and include at least one step that uses no
seismological data and one step that is a consistency check rather than a
measurement.

**★★★9.** Find the conductivity $k^{*}$ at which the conducted heat flow equals the
CMB heat flow, for assumed CMB heat flows of 8, 12 and 16 TW. Then invert the
problem: how large would the CMB heat flow have to be to make a core with
$k = 200$ W m$^{-1}$ K$^{-1}$ viable, and what else would have to change in the
model for that to be acceptable?

**★★★10.** Compute the inner-core age at $k = 100$ and at
$k = 118$ W m$^{-1}$ K$^{-1}$ (10 TW, latent heat included) and comment on the
sensitivity. Then show analytically, from
$\text{age} = D R_\text{ICB}(C_\text{core} + \Lambda_L)/(Q_\text{CMB} - Q_\text{ad})$,
what happens to $d(\text{age})/dk$ as $Q_\text{ad} \to Q_\text{CMB}$, and explain
why no measurement of the inner-core age can settle the conductivity question on its
own.
