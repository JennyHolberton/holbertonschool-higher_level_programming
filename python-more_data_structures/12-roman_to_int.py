#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    roman_num = 0
    for value in range(len(roman_string)):
        if value + 1 < len(roman_string) and roman_dict[roman_string[value]] \
           < roman_dict[roman_string[value + 1]]:
            roman_num = roman_num - roman_dict[roman_string[value]]
        else:
            roman_num = roman_num + roman_dict[roman_string[value]]
    return roman_num
