#!/usr/bin/env python3

import sys

args = sys.argv[1:] #ดึงรายการพารามิเตอร์ 

if len(args) == 0: #ถ้าจำนวนพารามิเตอร์เท่ากับ 0 ให้พิมพ์ "none"
    print("none")
else:
    for arg in args: #วนลูปอ่านพารามิเตอร์ทีละตัว

        if not arg.endswith("ism"):    #ถ้าคำนั้นไม่ได้ลงท้ายด้วย "ism" ให้เติม "ism" แล้วพิมพ์
            print(arg + "ism")

#ใช้เมธอด .endswith() เพื่อตรวจสอบว่าคำนั้นลงท้ายด้วยคำว่า "ism" หรือไม่