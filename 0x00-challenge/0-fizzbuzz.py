#!/usr/bin/python3
"""
Creating Class FizzBuzz
"""


def fizzbuzz(n):
    """
    The FizzBuzz function generates a sequence of numbers from 1 to n
    where each number is separated by a space.
    - multiples of three, it prints "Fizz" instead of the number.
    - for multiples of five, it prints "Buzz". If a number is a
    multiple of both three and five, it prints "FizzBuzz".
    """
    if n < 1:
        return

    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        fizzbuzz(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")
