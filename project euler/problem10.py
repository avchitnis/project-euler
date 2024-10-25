"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sum_of_primes(n: int) -> int:
    """
    find the sum of all the primes below a given number
    """

    sum = 0
    sieve = [True] * n
    
    for p in range(2, n):
        if sieve[p]:
            sum += p
            
            for i in range(p * p, n, p):
                sieve[i] = False
                
    return sum

print(sum_of_primes(2000000))