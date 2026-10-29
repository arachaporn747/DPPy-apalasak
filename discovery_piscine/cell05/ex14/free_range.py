#!/usr/bin/env python3

import sys

if len(sys.argv) != 3: #sys.argv จะเก็บข้อมูลเป็น list

    print("none")

else:

    start_num = int(sys.argv[1]) #ดึง parameterตัวที่ 1
    end_num = int(sys.argv[2]) #ดึง parameterตัวที่ 2
    
    number_array = list(range(start_num, end_num + 1)) #รวมตัวเลขตัวสุดท้าย
    #ฟังก์ชัน range(เริ่มต้น, สิ้นสุด)
    #list() แปลงข้อมูลตให้กลายเป็นโครงสร้างแบบ List
    
    print(number_array)