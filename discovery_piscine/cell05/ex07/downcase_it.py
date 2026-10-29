#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    print(sys.argv[1].lower())
else:
    print("none")
    
#len() นับจำนวนอาร์กิวเมนต์ที่ส่งเข้ามาในโปรแกรม
#.lower() แปลงข้อความเป็นตัวพิมพ์เล็ก