#!/usr/bin/python3
# import 
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    else:
        roman_string = roman_string.upper()
        if (roman_string == 'I'):
            return 1
        if (roman_string == 'V'):
            return 5
        if (roman_string == 'X'):
            return 10
        if (roman_string == 'C'):
            return 100
        if (roman_string == 'L'):
            return 50
        if (roman_string == 'D'):
            return 500
        if (roman_string == 'M'):
            return 1000
        