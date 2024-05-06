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


h = list(range(100))
for i in range(len(h)):
    if h[i] % 26 == 0:
        h[i] = 3

for i in h:
    if not is_prime(2 * (i * i) + 29):
        print(i)

