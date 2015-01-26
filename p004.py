'''
Problem 004:

    A palindromic number reads the same both ways. The largest
    palindrome made from the product of two 2-digit numbers is
    9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit
    numbers.
'''

def is_palindrome(word):
    '''
    Check whether a string is a palindrome
    '''
    word = str(word)
    if word == word[::-1]: # Dear future self: 
        return True
    else:
        return False

def solve():
    '''
    Solve the problem.
    '''
    three_digits = range(100, 1000)
    palindromes = []

    for i in three_digits:
        for j in three_digits:
            candidate = i*j
            if is_palindrome(candidate):
                palindromes.append(candidate)

    return max(palindromes)

if __name__ == '__main__':
    print(solve())
