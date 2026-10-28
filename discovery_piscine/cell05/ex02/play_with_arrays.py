#!/usr/bin/env python3
array = [2, 8, 9, 48, 8, 22, -22, 2]

new_array = []
#list `สำหรับเก็บค่าทีใหม่

#ดึงค่าตัวเลขจาก array ทีละตัว มาตรวจในตัวแปร num
for num in array:
    if num > 5:
        new_array.append(num + 2)

print("Original array:", array)
print("New array:", new_array)