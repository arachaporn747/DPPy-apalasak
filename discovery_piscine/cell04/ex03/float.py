#!/usr/bin/env python3

number = float(input("Give me a number: "))

if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
    
# python .\float.py (using Windows PowerShell, 
# but chmod +x is a Linux/macOS command)