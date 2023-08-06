"""
    this file responsible for containing any number of regex strings used to validate
    text
"""
import re

strict_unsigned_int = re.compile('^([0-9]+)$')
"""
    Matches only unsinged integers without whitespace or returns nothing
"""
strict_optionally_signed_int = re.compile('^([+|-]?[0-9]+)$')
"""
    Matches optionally signed integers with no whitespace or returns nothing
"""
strict_optionally_signed_decimal = re.compile('^[+|-]?[0-9]+\.[0-9]+$')
"""
    Matches  optionally signed decimals with no whitespace or returns nothing
"""
strict_unsigned_decimal = re.compile('[0-9]+\.[0-9]+$')

strict_match_list = re.compile("^\[((?:('?|\"?[A-Za-z0-9]+\"?|'?)[,]?)*)\]$")
""" matches a strigified list, THIS IS NOT STABLE YET. DOES NOT HANDLE MISMATCHED QUOTATIONS"""
strict_match_dict = re.compile("^\[((?:('?|\"?[A-Za-z0-9]+\"?|'?)[,]?)*)\]$")

alpha= u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
numeric = u'0123456789'
number_signs = u'+-'
decimal_point = '.'
special_characters = u'!@#$%^&*()_=<>,?/|\\'