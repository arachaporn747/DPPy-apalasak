#!/usr/bin/env python3

import sys

# เอาเฉพาะพารามิเตอร์ที่ส่งเข้ามา
params = sys.argv[1:]

if len(params) == 0:   # ตรวจสอบว่ามีพารามิเตอร์ส่งมา
    print("none")
else:
    print(f"parameters: {len(params)}")  # แสดงจำนวนพารามิเตอร์ทั้งหมด
    
    for param in params:
        # พิมพ์ชื่อพารามิเตอร์ ตามด้วยเครื่องหมาย : และความยาวของคำ
        print(f"{param}: {len(param)}")