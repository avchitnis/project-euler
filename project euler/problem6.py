"""
The sum of the squares of the first ten natural numbers is 385.

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_the_squares() -> int:
    """
    gives the sum of the squares of the first 100 natural numbers
    """
  
    total = 0

    for i in range(1, 101):
        total = total + (i ** 2)

    return total

def square_of_the_sum() -> int:
    """
    gives the square of the sum of the first 100 natural numbers
    """

    total = 0

    for i in range(1, 101):
        total = total + i

    return total ** 2

print(square_of_the_sum() - sum_of_the_squares())