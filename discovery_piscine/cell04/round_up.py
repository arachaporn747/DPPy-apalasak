#!/usr/bin/env python3
import math

num = float(input("Give me a number: "))
rounded_num = round(num)
print("The rounded number is:", rounded_num)

#round(num) : ปัดเศษตามหลักการปัดเศษลงท้ายด้วย .5
#math.ceil(num) : ปัดขึ้นไปยังจำนวนเต็มถัดไปเสมอ เช่น 23.01 >> 24
