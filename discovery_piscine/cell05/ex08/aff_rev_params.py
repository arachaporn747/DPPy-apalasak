#!/usr/bin/env python3

import sys
params = sys.argv[1:]

if len(params) < 2:
    print("None")

else:
    for param in reversed(params):
        print(param)

#import sys : Use module sys
#sys.argv[1:] : เลือกข้อมูลตั้งแต่ index 1 ขึ้นไป (ไม่เอา index 0 เพราะเป็นชื่อไฟล์)
#params ตัวแปรที่เก็บค่าที่ส่งเข้ามาในโปรแกรม
