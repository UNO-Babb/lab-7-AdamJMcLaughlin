#Problem3.py
#Project Euler problem 3

from NumberTests import largest_prime_factor

def main():
  
    number_to_factor = 600851475143
    result = largest_prime_factor(number_to_factor)

    print(f"The largest prime factor of {number_to_factor} is {result}.")

if __name__ == '__main__':
  main()
