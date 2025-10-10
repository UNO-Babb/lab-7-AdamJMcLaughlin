#Problem7.py
#Project Euler problem 7

from NumberTests import find_nth_prime

def main():
  
    nth = 10001
    result = find_nth_prime(nth)

    print(f"The {nth}st prime number is {result}.")

if __name__ == '__main__':
  main()