#Smallest multiple
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
multiple = 1
for i in range(1, 21):
    multiple = lcm(multiple, i)
print(multiple)