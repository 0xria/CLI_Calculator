"""
Building a CLI calculator using argparse
"""

import argparse


parser = argparse.ArgumentParser(description="CLI Calculator")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("operator", type=str, help="Operator: + - * /")
parser.add_argument("num2", type=float, help="Second_number")


args = parser.parse_args()
    
if args.operator == "+":
    result = args.num1 + args.num2
elif args.operator == "-":
    result = args.num1 - args.num2
elif args.operator == "*":
    result = args.num1 * args.num2
elif args.operator == "/":
    result = args.num1 / args.num2
else:
    raise ValueError("Invalid operator! Use +, -, *, or /")

print ("Result:", result)

