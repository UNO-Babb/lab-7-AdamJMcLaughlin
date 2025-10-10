#NumberTests.py

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False
  
def getFactors(num):
  """Returns a list of all factors of a given integer"""
  factors =[]
  for f in range(1, num//2+1):
    if num % f == 0:
      factors.append(f)

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p ==2:
    return True
  if isEven(p):
    return False
  
  for div in range(3,p // 2):
    if p % div ==0:
      return False
    
  return True

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

def largest_prime_factor(n):
    """
    Finds the largest prime factor of a given number n.

    Args:
        n: The number to factorize.

    Returns:
        The largest prime factor of n.
    """
    largest_prime = -1

    # Divide out all factors of 2
    while n % 2 == 0:
        largest_prime = 2
        n //= 2

    # Divide out odd factors starting from 3
    # We only need to check up to the square root of n
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 2

    # If n is still greater than 2 after all divisions,
    # it must be a prime number itself.
    if n > 2:
        largest_prime = n

    return largest_prime

def is_prime(n):
    """Checks if a number is prime using trial division."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_nth_prime(n):
    """Finds the nth prime number."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

def is_palindrome(n):
    """Checks if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def find_largest_palindrome_product():
    """Finds the largest palindrome made from the product of two 3-digit numbers."""
    largest_palindrome = 0
    # Iterate through all 3-digit numbers from 999 down to 100
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            # If the product is a palindrome and larger than the current largest
            if product > largest_palindrome and is_palindrome(product):
                largest_palindrome = product
            # Optimization: If the current product is smaller than the largest found,
            # we can stop checking for this i, as further products will be even smaller.
            elif product < largest_palindrome:
                break
    return largest_palindrome

#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]

  num = int(input("Enter a number: "))

  if isPrime(num):
    print("%d is a prime number" %(num))

  if isEven(num):
    print("%d is an even number" %(num))


if __name__ == '__main__':
    main()
