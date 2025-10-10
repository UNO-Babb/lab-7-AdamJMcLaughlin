#Problem4.py
#Project Euler problem 4

from NumberTests import find_largest_palindrome_product

def main():
  
  result = find_largest_palindrome_product()
  print(f"The largest palindrome made from the product of two 3-digit numbers is {result}.")  

if __name__ == '__main__':
  main()