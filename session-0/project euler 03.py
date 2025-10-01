#Largest prime factor
def largest_prime_factor(n):
    # remove factor 2
    last = None
    while n % 2 == 0:
        last = 2
        n //= 2

    # try odd factors from 3 upwards
    d = 3
    while d * d <= n:
        while n % d == 0:
            last = d
            n //= d
        d += 2  # only odd d

    # if anything left >1, it's prime and the largest factor
    if n > 1:
        last = n

    return last

num = 600851475143
print(largest_prime_factor(num))