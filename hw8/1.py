def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

for p in range(1000):
    for k in range(1000):
        if (is_prime(p) and is_prime(p+2) and (p != 3) and (p == 6*k-1) and (p+2 == 6*k+1)):
            print(p,", ",k)

# easy output: p = 5, k = 1