#!/usr/bin/env python3
import sys
import re #re เป็นโมดูลสำหรับค้นหาข้อความ

if len(sys.argv) == 3: #ตรวจว่ามีข้อมูลใน sys.argv ทั้งหมด 3 รายการ
    word = sys.argv[1] #นำคำค้นหาจากตำแหน่งที่ 1 มาเก็บไว้ในตัวแปร word
    text = sys.argv[2] #นำข้อความจากตำแหน่งที่ 2 มาเก็บไว้ในตัวแปร text

    result = re.findall(word, text)  # ค้นหาและรวบรวมสิ่งที่ตรงกับรูปแบบที่กำหนดทั้งหมด แล้วคืนค่าเป็น List

    if len(result) > 0: #ตรวจสอบว่า List result มีสมาชิกมากกว่า 0
        print(len(result))
    else:
        print("None")
else:
    print("None") # ถ้าไม่พบข้อความที่ค้นหา ให้แสดงคำว่า None
    