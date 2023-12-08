#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(romain_string, str):
        return 0
    total = 0
    num = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in reversed(romain_string):
        num = digits[r]
        total += num if total < num * 5 else -num
    return total
