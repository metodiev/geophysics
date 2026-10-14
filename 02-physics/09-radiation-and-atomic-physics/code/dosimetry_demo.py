"""Dosimetry, radiation safety and regulatory limits.

Run:  python3 dosimetry_demo.py
Requires: Python standard library only.

Companion to lesson 02-09-06.

The single most important design decision in this script is what it does NOT
print. It does not print a dose limit. Occupational and public dose limits are
jurisdiction specific and are revised; a number copied from a textbook or from
this script would be exactly the kind of unverifiable citation this curriculum
forbids. Where a limit is needed, the script keeps it symbolic: it prints
t = L / dose-rate, so that the reader substitutes the value from the current
IAEA or ICRP publication and the national regulation that applies, and can see
that the *arithmetic* is trivial and that the *number* is the part that must be
sourced.

The script:

1. Activity, atoms and mass: the conversions between becquerel, curie and
   disintegrations per minute, and the mass of an active deposit.
2. Point-source fluence and the inverse-square law, including the factor-of-two
   distance rule.
3. Shielding and half-value layers, with an explicit sensitivity analysis so
   that the tabulated attenuation coefficient is seen to be the input that
   matters.
4. Bremsstrahlung and beta shielding: why low-Z absorbers go first.
5. Counting statistics: Poisson errors, the 3-sigma detection limit, and the
   Curie minimum detectable activity for a gamma-ray spectrometer. This part is
   exact and needs no tabulated input at all.
6. Time, distance and shielding as a design calculation, with every limit kept
   symbolic.
"""

import math

# --------------------------------------------------------------------------
# Exact and tabulated inputs
# --------------------------------------------------------------------------

YEAR = 3.15576e7
DAY = 86400.0
AVOGADRO = 6.02214076e23
E_CHARGE = 1.602176634e-19
M_E_MEV = 0.51099895000
R_E = 2.8179403262e-15
BARN = 1.0e-28

T_HALF_A = {"Cs-137": 30.08, "Co-60": 5.2711, "Sr-90": 28.79,
            "Ir-192": 73.827 / 365.25, "Am-241": 432.6, "Ra-226": 1600.0}
MOLAR_MASS = {"Cs-137": 136.907090, "Co-60": 59.933822, "Sr-90": 89.907738,
              "Ir-192": 191.962605, "Am-241": 241.056829,
              "Ra-226": 226.025410}

# Illustrative attenuation coefficients, in cm^-1.  TABULATED values must be
# read from a photon cross-section compilation; these are given so that the
# sensitivity analysis has a starting point, and they are not to be quoted.
MU_ILLUSTRATIVE = {"water": 0.0870, "concrete": 0.1800, "iron": 0.5770,
                   "lead": 1.2500}

# Illustrative fluence-to-dose conversion for a 662 keV photon, in
# pSv per photon per cm^2.  This is the kind of coefficient that must come
# from the current ICRP/IAEA tables; the value here is declared as a model
# input and the script shows how much the answer moves if it is wrong.
H_STAR_ILLUSTRATIVE_PSV_CM2 = 4.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def lam(half_life_s):
    return math.log(2.0) / half_life_s


# --------------------------------------------------------------------------
# 1. Activity and mass
# --------------------------------------------------------------------------

def part1_activity():
    section("1. Activity, atoms and mass")
    print("  A = lambda N, and 1 Bq = 1 disintegration per second = 60 dpm.")
    print("  The curie is the legacy unit: 1 Ci = 3.7e10 Bq exactly, by")
    print("  definition. It is still in use in some regulatory documents and")
    print("  in some instrument specifications, so the conversion matters.")
    print()
    print("  Source activities are conventionally quoted at a reference date,")
    print("  because the nuclide decays. The mass of nuclide in a source is")
    print()
    print("    m = A M / (lambda N_A),")
    print("  with M the molar mass in g/mol.")
    print()
    print(f"{'nuclide':<10}{'A (GBq)':>10}{'atoms':>14}{'mass (g)':>12}"
          f"{'mass (mg)':>12}{'Ci':>12}")
    for name, a_gbq in (("Cs-137", 1.0), ("Co-60", 1.0), ("Ir-192", 10.0),
                        ("Am-241", 1.0), ("Ra-226", 1.0)):
        a = a_gbq * 1e9
        l = lam(T_HALF_A[name] * YEAR)
        n = a / l
        m = n * MOLAR_MASS[name] / AVOGADRO
        print(f"{name:<10}{a_gbq:>10.3f}{n:>14.4e}{m:>12.4e}"
              f"{m * 1e3:>12.4e}{a / 3.7e10:>12.4e}")
    print()
    print("  Read the mass column carefully. A 10 GBq iridium-192 source, a")
    print("  routine industrial radiography source, contains a fraction of a")
    print("  milligram of the nuclide. The source encapsulation is what is")
    print("  handled, weighed and leak-tested; the activity is not visible and")
    print("  not proportional to the size of the object. That is why sealed")
    print("  sources are inventoried by activity and serial number and not by")
    print("  appearance, and why a source that has lost its label is treated as")
    print("  a maximum-activity source until it is identified.")


# --------------------------------------------------------------------------
# 2. Fluence and the inverse-square law
# --------------------------------------------------------------------------

def part2_fluence():
    section("2. Fluence, the inverse-square law, and the factor of two")
    print("  For an unshielded point source the photon fluence rate at")
    print("  distance r is")
    print("    phi = A y / (4 pi r^2),")
    print("  with y the gamma yield per decay. No tabulated quantity enters")
    print("  except y, and the 4 pi is geometry.")
    print()
    a_mbq = 1000.0
    y = 0.85
    print(f"  Source: {a_mbq:.0f} MBq of a nuclide with a gamma yield of {y:.2f}")
    print("  per decay (ILLUSTRATIVE; the yield of a real line must come from")
    print("  a decay-data compilation and, for a branching decay, from the")
    print("  branching ratios).")
    print()
    print(f"{'r (m)':>8}{'r^2':>10}{'phi (photons/cm2/s)':>22}")
    for r in (0.3, 0.5, 1.0, 2.0, 4.0, 8.0):
        phi = a_mbq * 1e6 * y / (4.0 * math.pi * (r * 100.0) ** 2)
        print(f"{r:>8.1f}{r * r:>10.2f}{phi:>22.4e}")
    print()
    print("  Fluence falls as 1/r^2, so doubling the distance quarters it and")
    print("  halves the dose rate: the 'factor of two' rule. Halving the")
    print("  distance multiplies the dose rate by four. This is the single")
    print("  cheapest protective measure available and the one most often")
    print("  lost when a source is handled with tongs of the wrong length.")
    print()
    print("  For a LINE or a PLANE source the exponent changes: a long line")
    print("  gives 1/r at distances small compared with its length and a large")
    print("  plane gives no fall-off at all. That is why a whole-body counter")
    print("  is calibrated with phantoms rather than with a point source, and")
    print("  why a contaminated floor is a different problem from a point")
    print("  source: the geometry, not the activity, decides the answer.")


# --------------------------------------------------------------------------
# 3. Shielding
# --------------------------------------------------------------------------

def part3_shielding():
    section("3. Shielding, half-value layers and sensitivity to mu")
    print("  A narrow beam is attenuated as phi(x) = phi_0 exp(-mu x), so the")
    print("  half-value layer is HVL = ln2 / mu and the attenuation of a")
    print("  thickness x is a factor exp(-mu x).")
    print("  The thickness for a factor F of attenuation is")
    print("    x = ln(F) / mu.")
    print()
    print("  mu values used below are ILLUSTRATIVE starting points for a")
    print("  662 keV photon. The real values must come from a photon")
    print("  cross-section compilation, because the photoelectric contribution")
    print("  cannot be computed from a closed form (lesson 03).")
    print()
    print(f"{'material':<12}{'mu (1/cm)':>12}{'HVL (cm)':>11}"
          f"{'tenth-value (cm)':>18}{'x for 100x (cm)':>17}")
    for name, mu in MU_ILLUSTRATIVE.items():
        print(f"{name:<12}{mu:>12.4f}{math.log(2) / mu:>11.3f}"
              f"{math.log(10) / mu:>18.3f}{2 * math.log(10) / mu:>17.3f}")
    print()
    print("  Now the question that decides whether a calculation is worth")
    print("  anything. Suppose the true mu for lead is 10 per cent higher than")
    print("  the value in the table:")
    print()
    print(f"{'mu error':>10}{'x for 100x (cm)':>18}{'x error (%)':>14}")
    for err in (-0.2, -0.1, 0.0, 0.1, 0.2, 0.5):
        mu = MU_ILLUSTRATIVE["lead"] * (1.0 + err)
        print(f"{100 * err:>9.0f}%{2 * math.log(10) / mu:>18.4f}"
              f"{-100 * err / (1 + err):>14.2f}")
    print()
    print("  The required thickness scales as 1/mu, so the fractional")
    print("  thickness error is -d/(1+d) for a fractional coefficient error d:")
    print("  a 10 per cent overestimate of mu gives a 9 per cent")
    print("  underestimate of the thickness, and a 50 per cent overestimate")
    print("  gives a 33 per cent underestimate. The coefficient is an input")
    print("  of the same quality as the answer, which is why it, and not the")
    print("  arithmetic, is the part of a dose calculation that must be")
    print("  cited.")
    print()
    print("  Note also what the table does NOT contain -- any treatment of")
    print("  scattered photons. A broad beam is attenuated less than a narrow")
    print("  one, by a build-up factor that can exceed 2 for a thick lead")
    print("  shield. The narrow-beam formula is a lower bound on the required")
    print("  thickness, and a design that relies on it alone is optimistic.")
    print()
    print("  Distance versus thickness. Hold the shield fixed at 1 cm of lead")
    print("  and move the observer back:")
    print()
    print(f"{'r (m)':>8}{'exp(-mu x)/r^2':>17}{'relative to 0.5 m':>19}"
          f"{'shield area for 10 deg cone (m2)':>34}")
    mu_pb = MU_ILLUSTRATIVE["lead"]
    for r in (0.5, 1.0, 1.5, 2.0, 4.0):
        factor = math.exp(-mu_pb * 1.0) / r ** 2
        area = math.pi * (r * math.tan(math.radians(10.0))) ** 2
        print(f"{r:>8.1f}{factor:>17.4f}{factor / (math.exp(-mu_pb) / 0.25):>19.3f}"
              f"{area:>34.4f}")
    print()
    print("  Moving from 0.5 m to 2.0 m buys a factor of sixteen in dose")
    print("  rate for no material at all. But a shield at 2.0 m must subtend")
    print("  the same solid angle, and the table's last column shows that the")
    print("  area, and therefore the mass, grows as r^2 -- sixteen times the")
    print("  lead. The two effects cancel exactly for a source-to-shield")
    print("  distance that is small: what actually helps is distance between")
    print("  the SHIELD and the observer, not distance alone. That is why a")
    print("  shield is placed as close to the source as it can be, and why a")
    print("  radiography collimator is bolted to the source housing.")


# --------------------------------------------------------------------------
# 4. Bremsstrahlung
# --------------------------------------------------------------------------

def part4_bremsstrahlung():
    section("4. Beta sources: why the first absorber is always low-Z")
    print("  A beta particle slowing in a material radiates bremsstrahlung")
    print("  with a yield proportional to Z of the absorber and to the beta")
    print("  energy. Approximating the radiative yield per beta as")
    print("    Y ~ Z E_max(MeV) / 3000,")
    print("  an order-of-magnitude form of the standard estimate:")
    print()
    print(f"{'absorber':<12}{'Z':>5}{'E_max (MeV)':>13}{'Y per beta':>12}"
          f"{'photons per 1000 betas':>24}")
    for name, z in (("water", 7.4), ("aluminium", 13.0), ("iron", 26.0),
                    ("lead", 82.0)):
        for e_max in (0.514, 2.280):
            y = z * e_max / 3000.0
            print(f"{name:<12}{z:>5.1f}{e_max:>13.3f}{y:>12.4e}"
                  f"{y * 1000:>24.2f}")
    print()
    print("  A strontium-90 source with its yttrium-90 daughter has a maximum")
    print("  beta energy near 2.28 MeV. Shielded with lead, roughly")
    y_pb = 82.0 * 2.280 / 3000.0
    y_al = 13.0 * 2.280 / 3000.0
    print(f"  {y_pb * 100:.1f} per cent of the betas convert to a bremsstrahlung")
    print(f"  photon; shielded with aluminium, only {y_al * 100:.1f} per cent.")
    print(f"  The lead shield then has to attenuate a hard photon flux that the")
    print("  aluminium shield never produced. The standard practice -- put a")
    print("  few millimetres of plastic or aluminium against the source and")
    print("  the lead outside it -- is nothing more than this ratio.")
    print()
    print("  The estimate itself is crude: the coefficient and the spectral")
    print("  shape come from the Bethe-Heitler cross section, the self-")
    print("  absorption of the beta in the source is ignored, and the")
    print("  angular distribution is forward-peaked. Use it to decide the")
    print("  ORDER of the absorber layers, and use a transport calculation for")
    print("  a design.")


# --------------------------------------------------------------------------
# 5. Counting statistics and detection limits
# --------------------------------------------------------------------------

def part5_statistics():
    section("5. Counting statistics: the part with no tabulated inputs")
    print("  Counting is a Poisson process, so a count N has standard")
    print("  deviation sqrt(N) and a rate N/t has a relative uncertainty")
    print("  1/sqrt(N). Nothing here needs a table; this is the only part of")
    print("  dosimetry that is exact.")
    print()
    print(f"{'counts':>10}{'sigma':>10}{'rel unc (%)':>15}"
          f"{'time for 1% (s at 1 cps)':>27}")
    for n in (10.0, 100.0, 1000.0, 10000.0, 100000.0, 1000000.0):
        print(f"{n:>10.0f}{math.sqrt(n):>10.2f}{100.0 / math.sqrt(n):>15.2f}"
              f"{1e4 / n:>27.1f}")
    print()
    print("  To reach 1 per cent on a count rate you need 10 000 counts, and")
    print("  the time that takes scales as 1/rate. That single line explains")
    print("  why a low-activity sample is counted for a day and a high-")
    print("  activity one for a minute, and why a survey instrument trades")
    print("  its counting time against its speed over the ground.")
    print()
    print("  Detection limit. For a sample counted for time t_s against a")
    print("  background counted for time t_b at rate R_b, the net rate has")
    print("  standard deviation")
    print("    sigma_net = sqrt(R_b / t_b + R_b / t_s),")
    print("  and the Curie criterion for the minimum detectable activity at")
    print("  three standard deviations is")
    print("    MDA = 3 sigma_net / (eff * y),")
    print("  with eff the detection efficiency and y the gamma yield. Take")
    print("  eff and y as MODEL inputs; the statistics are not.")
    print()
    r_b = 2.0
    t_b = 3600.0
    eff, y = 0.05, 0.85
    print(f"  Background rate R_b = {r_b:.2f} cps over t_b = {t_b:.0f} s,")
    print(f"  efficiency {eff:.2f}, yield {y:.2f}.")
    print()
    print(f"{'t_s (s)':>10}{'3 sigma of net rate (cps)':>27}"
          f"{'MDA (Bq)':>12}{'MDA (kBq)':>12}")
    for t_s in (60.0, 600.0, 3600.0, 36000.0):
        sigma_net = math.sqrt(r_b / t_b + r_b / t_s)
        mda = 3.0 * sigma_net / (eff * y)
        print(f"{t_s:>10.0f}{3.0 * sigma_net:>27.6f}{mda:>12.1f}"
              f"{mda / 1e3:>12.4f}")
    print()
    floor = 3.0 * math.sqrt(r_b / t_b) / (eff * y)
    print("  The detection limit improves only as the square root of the")
    print("  counting time, and it has a FLOOR: as t_s grows, sigma_net")
    print(f"  approaches sqrt(R_b/t_b) and the MDA approaches {floor:.2f} Bq whatever")
    print("  you do to the sample. Counting for ten times longer buys a factor")
    print("  of two, not ten, and beyond the floor it buys nothing at all")
    print("  except a longer background count. This is why 'detection limit'")
    print("  is meaningless without a stated counting time, background and")
    print("  efficiency. Quote all three or quote none.")
    print()
    print("  The geophysical reason this matters: a gamma-ray survey anomaly")
    print("  is a count-rate contrast above a background that is itself")
    print("  Poisson distributed. An anomaly that is two standard deviations")
    print("  of the background is not an anomaly, it is a coin toss, and the")
    print("  only way to tell is to state the background, the counting time")
    print("  and the area of the accumulation.")


# --------------------------------------------------------------------------
# 6. Time, distance, shielding, with every limit kept symbolic
# --------------------------------------------------------------------------

def part6_control():
    section("6. Time, distance and shielding, with the limit left symbolic")
    print("  A regulatory system works like this:")
    print()
    print("    (a) the national regulation adopts a dose limit L for a stated")
    print("        category (occupational, public, trainee, pregnant worker);")
    print("    (b) the limit is derived from the recommendations of the")
    print("        International Commission on Radiological Protection as")
    print("        published in the current ICRP recommendations, and IAEA")
    print("        safety standards give the operational form;")
    print("    (c) the licensee must demonstrate that the dose received is a")
    print("        stated fraction of L, and must apply the optimisation")
    print("        principle (ALARA) to go below it.")
    print()
    print("  None of (a)-(c) can be reproduced from memory. L is")
    print("  jurisdiction specific and is revised; the recommended value in")
    print("  force on the day you work is the one in the current IAEA/ICRP")
    print("  publication, and it is that number, with its date, that belongs")
    print("  in a calculation or a licence application. This script therefore")
    print("  keeps L symbolic and computes only the arithmetic that follows")
    print("  once it is supplied.")
    print()
    print("  Dose rate from a point source, with a declared conversion")
    print("  coefficient h and the fluence of section 2:")
    print("    H_dot = A y h / (4 pi r^2)  [Sv/s]  for h in Sv m^2 per photon.")
    print()
    a_bq = 1e9
    r = 1.0
    y = 0.85
    h = H_STAR_ILLUSTRATIVE_PSV_CM2 * 1e-12 * 1e-4     # Sv m^2 per photon
    phi = a_bq * y / (4.0 * math.pi * r ** 2)
    h_dot = phi * h
    print(f"  A = 1 GBq, y = {y:.2f}, r = {r:.1f} m, and a declared h of")
    print(f"  {H_STAR_ILLUSTRATIVE_PSV_CM2:.1f} pSv cm^2 per photon, which is a MODEL")
    print("  input standing in for the current ICRP/IAEA fluence-to-dose")
    print("  conversion coefficients.")
    print()
    print(f"    phi   = {phi:.4e} photons per m^2 per s")
    print(f"    H_dot = {h_dot * 1e6:.4e} microSv/s = {h_dot * 3.6e6:.4f} mSv/h")
    print()
    print("  Sensitivity to h, which is the honest way to present this:")
    print(f"{'h multiplier':>14}{'H_dot (mSv/h)':>17}{'change (%)':>13}")
    base = h_dot * 3.6e6
    for mult in (0.5, 0.8, 1.0, 1.2, 2.0):
        print(f"{mult:>14.1f}{base * mult:>17.4f}{100 * (mult - 1):>13.0f}")
    print()
    print("  The dose rate is linear in h, so a factor of two in the")
    print("  coefficient is a factor of two in the answer. That is why a")
    print("  dose assessment must cite the conversion coefficient it used,")
    print("  its publication and its date, and why a bare 'the dose rate is")
    print("  X' is not a statement about the world but about a choice of")
    print("  coefficients.")
    print()
    print("  Permitted occupancy time, with L symbolic:")
    print()
    print(f"{'L (mSv/a)':>12}{'H_dot (mSv/h)':>16}{'hours at 1 m':>15}"
          f"{'hours, 50 cm back':>20}")
    h_dot_far = base * (1.0 / 1.5) ** 2
    for l_mSv in (1.0, 5.0, 20.0, 50.0):
        print(f"{l_mSv:>12.1f}{base:>16.4f}{l_mSv / base:>15.2f}"
              f"{l_mSv / h_dot_far:>20.2f}")
    print()
    print("  The first three columns are the arithmetic; the first column is")
    print("  the only one you must look up. Substitute the L that applies to")
    print("  the worker category in your jurisdiction, from the current")
    print("  published limit, and state its source. Where the computed")
    print("  occupancy time is impractically short, the response is not a")
    print("  longer working day but more distance or more shielding -- and")
    print("  the numbers above show how much more effective distance is.")
    print()
    print("  Two facts about internal dose belong in the same section,")
    print("  because they are what makes the point-source arithmetic")
    print("  insufficient in a geophysical setting:")
    print("  1. Radon. The largest single contributor to natural background")
    print("     dose is radon and its progeny, which are inhaled rather than")
    print("     irradiated from outside. A uranium-bearing rock is a radon")
    print("     source, and a poorly ventilated core shed or an underground")
    print("     working is where the limit is likely to be approached. Its")
    print("     assessment needs the current IAEA guidance on radon and the")
    print("     current national reference level, neither of which is")
    print("     reproduced here.")
    print("  2. NORM. Oilfield scale, produced water, some mineral sands and")
    print("     some industrial residues concentrate naturally occurring")
    print("     radionuclides to levels that bring the material into the")
    print("     regulatory system. The threshold concentrations are set by")
    print("     national regulation and are conventionally expressed per gram")
    print("     of material; look them up before classifying a waste.")


def main():
    part1_activity()
    part2_fluence()
    part3_shielding()
    part4_bremsstrahlung()
    part5_statistics()
    part6_control()


if __name__ == "__main__":
    main()
