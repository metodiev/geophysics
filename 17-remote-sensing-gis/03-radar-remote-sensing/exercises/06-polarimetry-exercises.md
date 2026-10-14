# Exercises — 17-03-06 SAR Polarimetry and Polarimetric Decomposition

Attempt these before reading the
[solutions](./06-polarimetry-solutions.md). The lesson is
[06 Polarimetry](../06-polarimetry.md). All models are **SYNTHETIC** teaching
values.

Constants: $\lambda = 5.6565\ \mathrm{cm}$,
$\Lambda_B = \lambda/(2\sin\theta)$, teaching dielectric constant
$\epsilon = 6.0$.

## ★ Foundational

**★1.** Write the $2\times2$ scattering matrix of (a) a trihedral reflector,
(b) a dihedral reflector, (c) a $30^\circ$-oriented dipole. Give the Pauli vector
of each and state which canonical mechanism it represents.

**★2.** Verify the Pauli norm identity for a target with
$S_{HH} = 2$, $S_{VV} = 1$, $S_{HV} = 0.5$: compute
$|\mathbf{k}|^{2}$ from the Pauli vector and compare it with
$|S_{HH}|^{2}+|S_{VV}|^{2}+2|S_{HV}|^{2}$.

**★3.** Compute the Bragg resonant surface wavelength for $\theta = 20^\circ$,
$35^\circ$ and $50^\circ$ at $\lambda = 5.6565\ \mathrm{cm}$, and state in one
sentence which physical surface features each corresponds to.

## ★★ Applied

**★★4.** A 16-look coherency matrix has eigenvalues $(1.60,\ 0.30,\ 0.10)$ in the
same units. **(a)** Compute the probabilities, the entropy $H$ and the anisotropy
$A$. **(b)** The eigenvector magnitudes are $|u_{i,1}| = (0.95,\ 0.45,\ 0.20)$;
compute the mean alpha and interpret the pixel. **(c)** State whether the
degeneracy caution applies strongly to this pixel and why.

**★★5.** Using the demonstration's Bragg table, a bare-soil pixel at
$\theta = 35^\circ$ has $\sigma^{0}_{HH}/\sigma^{0}_{VV} = -3.0\ \mathrm{dB}$. At
$\theta = 45^\circ$ it is $-4.8\ \mathrm{dB}$. **(a)** Compute the linear ratios.
**(b)** Explain whether the change is consistent with the same dielectric
constant, and what the correct interpretation of the pair is.

**★★6.** The demonstration's entropy convergence table gives mean $H = 0.0878$
(2 looks), $0.1380$ (4), $0.1743$ (16) and $0.1831$ (64) for a deterministic
target. Fit the form $H(N) = H_\infty\,(1 - a/N)$ roughly to the last three
points and state what the value of $H_\infty$ implies for a threshold chosen at
$H > 0.20$.

## ★★★ Research-oriented

**★★★7.** Design a polarimetric survey to distinguish a flooded forest from a dry
forest. State: the acquisition geometry and polarisation channels you need, the
decomposition parameters you would compute, the expected values for each
mechanism, the look count you would require and why, and the confounder you
cannot remove. Justify each choice with a number from the lesson. A specification
that could not be executed is a failed answer.

**★★★8.** Section 3.5 shows that a degenerate coherency matrix gives a mean alpha
that depends on the eigenvector convention. **(a)** Explain why $H$ and $A$ are
invariant while $\alpha$ is not, referring to what each parameter depends on.
**(b)** Construct a degenerate example in which the ambiguity in mean alpha is
larger than the $3.50^\circ$ measured in the lesson, and state how large it can
become in the limit. **(c)** State the practical reporting rule you would adopt.
