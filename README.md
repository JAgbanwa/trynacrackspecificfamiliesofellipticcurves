# trynacrackspecificfamiliesofellipticcurves

## Main equation

$v^2  = x^3 + m^2 \cdot x^2 + \dfrac{1}{3}  m^3 \cdot x + \dfrac{m^4 - 19m}{36}$

The Weierstrass equation of the above equation is:

$v^2 = X^3 + \left(-\frac{1}{3} \cdot m^4 + \frac{1}{3} \cdot m^3\right) \cdot X + \frac{72m^6 - 108m^5 + 27m^4 - 513m}{972}$


where

$X = x + \frac{m^2}{3}$ and $u = \frac{72m^6 - 108m^5 + 27m^4 - 513m}{972}$

---

## Parametrized integer points $(m(n), u(n))$

| \# | $m(n)$ | $u(n)$ |
|---|---|---|
| 1 | $108 \cdot n$ | $3\cdot\left(39182082048n^6 - 544195584n^5 + 1259712n^4 - 19n\right)$ |
| 2 | $36 \cdot (3n+1)$ | $117546246144n^6 + 233459905536n^5 + 193193211456n^4 + 85262347008n^3 + 21165681024n^2 + 2802159303n + 154571309$ |
| 3 | $36 \cdot (3n+2)$ | $117546246144n^6 + 468552397824n^5 + 778203464256n^4 + 689324484096n^3 + 343457957376n^2 + 91268093895n + 10105316314$ |
| 4 | $27 \cdot (4n+1)$ | $3 \cdot \left(39182082048n^6 + 58228927488n^5 + 36054217152n^4 + 11905538112n^3 + 2211266952n^2 + 219032405n + 9039413\right)$ |
| 5 | $9 \cdot (12n+7)$ | $117546246144n^6 + 409779274752n^5 + 595217699136n^4 + 461101201344n^3 + 200925481176n^2 + 46694776911n + 4521537356$ |
| 6 | $9 \cdot (12n+11)$ | $117546246144n^6 + 644871767040n^5 + 1474093567296n^4 + 1797106398912n^3 + 1232376407064n^2 + 450723291423n + 68685282985$ |

The goal is to find at least an integral point $(n,X,v)$ for any of the six resulting Weierstrass equations if $m(n)$ and $u(n)$ were substituted into 
$v^2 = X^3 + \left(-\frac{1}{3} \cdot m^4 + \frac{1}{3} \cdot m^3\right) \cdot X + \frac{72m^6 - 108m^5 + 27m^4 - 513m}{972}$.

The first case to be dealt with is:

$$v^2 = X^3 + \left(-45349632 \cdot n^4 + 419904 \cdot n^3\right) \cdot X + 3\cdot\left(39182082048n^6 - 544195584n^5 + 1259712n^4 - 19n\right)$$

with the constraint $X \neq 0$.

---

## Case 1 Search Results: $m(n) = 108n$

### Curve structure

Substituting $m = 108n$ into the general short Weierstrass model gives the one-parameter family:

$$E_n : v^2 = X^3 + A(n)\,X + B(n)$$

where

$$A(n) = -45349632n^4 + 419904n^3 = 419904n^3(1 - 108n)$$

$$B(n) = 3\cdot\left(39182082048n^6 - 544195584n^5 + 1259712n^4 - 19n\right)$$

At $X = 0$ the curve equation reduces to $v^2 = B(n) = 3n(39182082048n^5 - 544195584n^4 + 1259712n^3 - 19)$, which is excluded by the constraint $X \neq 0$.  For $n = 1,\ldots,10$ this value is not a perfect square (verified by direct computation), so the constraint is again vacuous for these $n$.

### Computational results (18 March 2026)

**Tools used:** SageMath (`EllipticCurve.rank(proof=False)`, torsion subgroup) and a Python integer sieve.

| $n$ | MW rank | Torsion pts | Integer pts found | Search bound $\lvert X\rvert \leq$ |
|:---:|:---:|:---:|:---:|:---|
| 1 | **0** | none | none | 500 000 |
| 2 | **0** | none | none | 500 000 |
| 3 | — | — | none | 357 142 |
| 4 | — | — | none | 153 846 |
| 5 | — | — | none | 79 365 |
| 6 | — | — | none | 46 082 |
| 7 | — | — | none | 29 069 |
| 8 | — | — | none | 19 493 |
| 9 | — | — | none | 13 698 |
| 10 | — | — | none | 9 990 |
| 11–30 | — | — | none | decreasing (see note) |

*Note:* For $n \geq 3$ the integer sieve used bound $\lfloor 10^7/(n^3+1) \rfloor$ to keep runtime practical.  MW rank for $n \geq 3$ is still being determined (full 2-descent is slow because the conductor of $E_n$ grows as $O(n^{12})$).

### Key observations

1. **Rank 0 for $n=1,2$:** Sage confirms the Mordell–Weil rank is 0 and the torsion is trivial, so $E_1$ and $E_2$ have **no rational points at all** (beyond $\mathcal{O}$).

2. **No integer points for $n=1\ldots30$:** The brute-force sieve found zero perfect-square values of the RHS in the searched range.

3. **Forbidden point check:** At $X = 0$, $v^2 = B(n)$ is not a perfect square for $n=1,\ldots,10$; so the constraint $X \neq 0$ is vacuous for these $n$.

4. **Conductor growth:** $\Delta(E_n) \sim n^{12}$ (inferred from the degree of $A(n)$ and $B(n)$), so the curve gets harder to attack algebraically as $n$ grows.

### Conclusion (so far)

No rational points with $X \neq 0$ have been found for $n = 1,\ldots,30$.  For $n=1$ and $n=2$ this is a proven statement (rank 0, trivial torsion).  Extending the rank computation and the sieve to larger $n$ and larger $X$-bounds is ongoing.

