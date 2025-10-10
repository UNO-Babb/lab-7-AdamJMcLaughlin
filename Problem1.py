#Project Euler Problem 1

import NumberTests

def main():
  total = 0
  for i in range(1000):
        if NumberTests.isThreeOrFive(i):
              total += i

              print(total)


              if __name__ == '__main__':
                  main()
