#!/usr/bin/python3


import sys
import sympy as sp

def find_first_divisor(num_str):
    num = int(num_str)
    divisors = list(sp.divisors(num))
    
    if len(divisors) >= 2:
        p = divisors[1]
        q = num // p
        print(f"{num}={q}*{p}")

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            num_str = line.strip()
            find_first_divisor(num_str)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)

