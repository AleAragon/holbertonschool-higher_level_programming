#!/usr/bin/python3
"""Check for lowercase characters."""
def islower(c):
    c = ord(c)
    if 97 <= c <= 122:
        return True
    else:
        return False
