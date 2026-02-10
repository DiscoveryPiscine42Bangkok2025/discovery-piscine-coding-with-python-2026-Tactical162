#!/usr/bin/env python3

# Ask the user for two numbers
first = input("Give me the first number: ")
second = input("Give me the second number: ")

# Convert to numbers (float ครอบคลุมทั้ง int และ decimal)
a = float(first)
b = float(second)

print("Thank you!")

# Perform calculations
print(f"{a:g} + {b:g} = {a + b:g}")
print(f"{a:g} - {b:g} = {a - b:g}")
print(f"{a:g} / {b:g} = {a / b:g}")
print(f"{a:g} * {b:g} = {a * b:g}")
