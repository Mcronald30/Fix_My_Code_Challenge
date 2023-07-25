#!/usr/bin/python3
"""
Creating Class FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    The FizzBuzz function generates a sequence of numbers from 1 to n

    where each number is separated by a space. However, for multiples
    of three, it prints "Fizz" instead of the number, and for multiples
    of five, it prints "Buzz". If a number is a multiple of both 
    three and five, it prints "FizzBuzz".
    """
    for data in range(1, n + 1):
        if data % 15 == 0:
            print("FizzBuzz", end=" ")
        elif data % 3 == 0:
            print("Fizz", end=" ")
        elif data % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(data, end=" ")

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: ./0-fizzbuzz.py <n>")
            sys.exit(1)

        try:
            n = int(sys.argv[1])
            fizzbuzz(n)
        except ValueError:
            print("Invalid input. Please enter an integer.")
