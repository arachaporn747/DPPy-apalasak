#!/usr/bin/env python3
import sys

# เช็กว่าส่ง parameter มา 1 ตัว และมีตัว 'z' อยู่ในข้อความ?
if len(sys.argv) == 2 and 'z' in sys.argv[1]:

    # พิมพ์ 'z' ตามจำนวนที่นับได้ในข้อความ
    print('z' * sys.argv[1].count('z'))

else:
    print('none')