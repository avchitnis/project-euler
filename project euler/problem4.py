"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num: int) -> bool:
    """
    check if a given number is a palindrome
    """
    
    if str(num) == str(num)[:: -1]:
        return True
        
    else:
        return False

def find_largest_palindrome(lb: int, ub: int) -> int:
    """
    find the largest palindrome made from the product of two 3-digit numbers.
    """

    largest = 0

    for i in range(lb, ub):
        for j in range(lb, ub):
            prod = i * j

            if is_palindrome(prod):
                if prod > largest:
                    largest = prod

    return largest

print(find_largest_palindrome(100, 1000))