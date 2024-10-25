"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from math import gcd

def smallest_multiple(a: list) -> int:
    """
    find smallest number evenly divisibly by a group of numbers
    """

    lcm = 1

    for i in a:
        lcm = lcm * i // gcd(lcm, i)

    return lcm

print(smallest_multiple([i for i in range(1, 21)]))