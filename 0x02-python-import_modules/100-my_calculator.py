#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = argv[1]
    b = argv[3]
    op = argv[2]
    if op == '+':
        print("{} {} {} = {}".format(a, b, op, add(a, b)))
    elif op == '-':
        print("{} {} {} = {}".format(a, b, op, sub(a, b)))
    elif op == '*':
        print("{} {} {} = {}".format(a, b, op, mul(a, b)))
    elif op == '/':
        print("{} {} {} = {}".format(a, b, op, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
