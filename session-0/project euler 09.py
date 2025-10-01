#Special Pythagorean triplet
def find_special_triplet(total=1000):
    for m in range(2, int((total//2)**0.5)+2):
        for n in range(1, m):
            if (m - n) % 2 == 0:    # opposite parity required for primitive
                continue
            if __import__('math').gcd(m, n) != 1:
                continue
            denom = 2*m*(m + n)
            if total % denom != 0:
                continue
            k = total // denom
            a = k*(m*m - n*n)
            b = k*(2*m*n)
            c = k*(m*m + n*n)
            return a*b*c
    return None
print(find_special_triplet(1000))