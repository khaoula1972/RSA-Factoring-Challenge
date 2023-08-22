#!/usr/bin/python3

import sys
import math

def factorize(number):
    factors = []
    sqrt_n = int(math.sqrt(number))
    for i in range(2, sqrt_n + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            for line in file:
                number = int(line.strip())
                factor_pairs = factorize(number)
                for p, q in factor_pairs:
                    print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == "__main__":
    main()
