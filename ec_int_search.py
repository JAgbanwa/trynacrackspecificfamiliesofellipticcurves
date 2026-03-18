"""
Integer point search for the EC family
  v^2 = X^3 + A(n)*X + B(n)
  A(n) = -45349632*n^4 + 419904*n^3
  B(n) = 3*(39182082048*n^6 - 544195584*n^5 + 1259712*n^4 - 19*n)
  forbidden: X = -3888*n^2

Strategy: for each n, scan integer X in [-10^6, 10^6] and
check if RHS is a perfect square.
"""
from math import isqrt

def a4(n): return -45349632*n**4 + 419904*n**3
def a6(n): return 3*(39182082048*n**6 - 544195584*n**5 + 1259712*n**4 - 19*n)
def rhs(X, n): return X**3 + a4(n)*X + a6(n)
def forb(n): return -3888*n**2

results = []

for n in range(1, 31):
    Xf = forb(n)
    A = a4(n)
    B = a6(n)
    found = []
    # Scan integer X in a range
    # For large n, coefficients are huge, so limit scan
    limit = max(100, min(500000, 10**7 // (n**3 + 1)))
    for X in range(-limit, limit+1):
        if X == Xf:
            continue
        rhs_val = X**3 + A*X + B
        if rhs_val < 0:
            continue
        sq = isqrt(rhs_val)
        if sq*sq == rhs_val and sq > 0:
            found.append((X, sq))
    if found:
        print("n=%d: INTEGER POINTS found (X, v):" % n)
        for xv, vv in found[:5]:
            print("  X=%d  v=%d" % (xv, vv))
        results.append((n, found))
    else:
        print("n=%d: no integer points in |X|<=%d" % (n, limit))

print()
print("="*60)
if results:
    print("Summary of integer points found:")
    for n, pts in results:
        print("  n=%d:" % n)
        for xv, vv in pts[:3]:
            print("    X=%d, v=%d" % (xv, vv))
else:
    print("No integer solutions found.")
