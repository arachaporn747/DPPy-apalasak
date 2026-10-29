#!/usr/bin/env python3
import sys
#นำเข้าโมดูล sys ซึ่งช่วยให้เราเข้าถึงข้อมูลของโปรแกรม

# ตรวจสอบว่ามีพารามิเตอร์ส่งมา 1 ตัวพอดีหรือไม่ (ความยาว = 2 เพราะนับชื่อไฟล์ด้วย)
if len(sys.argv) == 2:
    user_input = input("What was the parameter? ")

    if user_input == sys.argv[1]:
        print("Good job!")

    else:
        print("Nope, sorry...")

else:
    # ถ้าส่งพารามิเตอร์มาเกิน 1 ตัว หรือไม่ได้ส่งมาเลย
    print("none")
