#!/usr/bin/env python3

text = input("Enter a string: ")

for letter in text:
    if letter.isupper():
        print(letter.lower(), end="")
    else:
        print(letter.upper(), end="")

#for letter in text: วนอ่านตัวอักษรทีละตัว
#letter.isupper() ตรวจสอบว่าตัวอักษรเป็นพิมพ์ใหญ่ ?
#end="" ทำให้แสดงผลต่อกันในบรรทัดเดียว