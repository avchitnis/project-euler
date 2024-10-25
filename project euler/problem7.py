"""
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13 we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def primes_upto(limit):
    """
    gives all the primes up to a given limit
    """

    limitN = limit + 1
    not_prime = set()
    primes = [2]

    for i in range(3, limitN, 2):
        if i in not_prime:
            continue

        for j in range(i * 3, limitN, i * 2):
            not_prime.add(j)

        primes.append(i)
    return primes

print(primes_upto(200000)[10000])