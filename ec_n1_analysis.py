from sage.all import QQ, EllipticCurve
import sys

def a4(n): return -45349632*n**4 + 419904*n**3
def a6(n): return 3*(39182082048*n**6 - 544195584*n**5 + 1259712*n**4 - 19*n)

results = []

for n in range(1, 16):
    A = a4(n); B = a6(n)
    E = EllipticCurve(QQ, [0, 0, 0, A, B])
    if E.discriminant() == 0:
        print("n=%d: SINGULAR" % n); continue

    # Torsion (fast)
    tors_pts = [P for P in E.torsion_points() if P != E(0)]
    
    # Rank (proof=False is fast but may be uncertain)
    try:
        rk = E.rank(proof=False)
    except Exception as e:
        rk = "unknown (%s)" % e
    
    print("n=%d: rank=%s, torsion_pts=%s" % (n, rk, len(tors_pts)))
    sys.stdout.flush()
    
    if isinstance(rk, int) and rk >= 1:
        try:
            gens = E.gens()
            for P in gens:
                print("  generator: X=%s, v=%s" % (P[0], P[1]))
                results.append((n, P[0], P[1]))
        except Exception as e:
            print("  gens error:", e)

print()
print("="*60)
print("Summary - n with rank >= 1:")
seen = set()
for (n, Xp, vp) in results:
    if n not in seen:
        print("  n=%d: X=%s, v=%s" % (n, Xp, vp))
        seen.add(n)
if not seen:
    print("  None found in n=1..15 (rank=0 for all, or computationally undetermined)")
