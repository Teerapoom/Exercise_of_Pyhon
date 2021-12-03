# ต้องการทราบ ascii code ของ “A”
# print("ascii code ของ A","คือ",ord("A"))

# ต้องการทราบ ascii code ของ “z”
# print("ascii code ของ z ","คือ",ord("z"))

# ต้องการทราบอักขระที่มี ascii code เท่ากับ 100
# print(chr(100))

# ต้องการทราบอักขระที่มี ascii code เท่ากับ 112
# print(chr(112))

# จงบอกว่า True หรือ False
# if "a" > "b":
# a = ord("a")
# b = ord("b")
# print(a > b)

# if "a" > "b":
# a = ord("a")
# b = ord("b")
# print(a < b)

# if "a" == "b":
# a = ord("a")
# b = ord("b")
# print(a == b)

# if ord("a") < ord("b"):
# print(ord("a") < ord("b"))
# sum = ord("a") < ord("b")
# if ord("a") < ord("b"):
#     print(sum)

# if ord("Z") < ord("z"):
# print( ord("Z") < ord("z"))

# if chr(100) < chr(115):
# a = ord(chr(100))
# b = ord(chr(115))
# print( a < b )

# รับอักขระตัวพิมพ์เล็กเข้ามา 1 ตัว แล้วทําการแปลงให้เป็นตัวพิมพ์ใหญ่
# str= input("กรอกข้อมูล: ")
# a = chr(ord(str) - 32)
# print(a)

# รับอักขระตัวพิมพ์ใหญ่เข้ามา 1 ตัว แล้วทําการแปลงให้เป็นตัวพิมพ์เล็ก
# str= input("กรอกข้อมูล: ")
# a = chr(ord(str) + 32)
# print(a)

# รับอักขระเข้ามา 1 ตัว ถ้าข้อมูลเข้าเป็นตัวพิมพ์เล็ก ให้แปลงเป็นตัวพิมพ์ใหญ่ แต่ถ้าข้อมูลเข้าเป็นตัวพิมพ์ใหญ่ ให้แปลงเป็นตัวพิมพ์เล็ก 
# str = input("กรอกข้อมูล: ")
# notes = str.islower()
# if notes == True:
#     notes_up = chr(ord(str) - 32)
#     print(notes_up)
# else:
#     notes_low = chr(ord(str) + 32)
#     print(notes_low)

# -----------------------
# รับอักขระเข้ามา 1 ตัว แล้วทําการหาลําดับถัดไปของอักขระ 
# str = input("กรอกข้อมูล: ")
# notes = chr(ord(str)+1)
# print(notes)

# จงแปลงข้อความ “PROGRAMMER” ให้เป็นตัวพิมพ์เล็กทั้งหมด โดยห้ามใช้ string methods
# str = "PROGRAMMER"
# str0 = ""
# for i in str:
#     str0 += chr(ord(i) + 32)
# print(str0)

# จงแปลงข้อความ “I DO NOT like you” ให้เป็นตัวพิมพ์เล็กทั้งหมด โดยห้ามใช้ string methods 
# str = "I DO NOT like you"
# str0 = ""
# for i in str:
#     if ord(i) >= 65 and ord(i) <= 90 or ord(i) == 32:
#         if ord(i) != 32:
#             str0 += chr(ord(i)+ 32)
#         else:
#             str0 += chr(32)
#     else:
#         str0 += i
# print(str0)

# จงแปลงข้อความ “I DO NOT like you” จากตัวพิมพ์ใหญ่ให้เป็นตัวพิมพ์เล็ก และจากตัวพิมพ์เล็กให้
# เป็นตัวพิมพ์ใหญ่ โดยห้ามใช้ string methods
# str1 = "I DO NOT like you"
# str2 = ""
# for i in str1:
#     if ord(i) >= 65 and ord(i) <= 90:
#         str2 += chr(ord(i) + 32)
#     elif ord(i) >= 97 and ord(i) <= 122:
#         str2 += chr(ord(i) - 32)
#     else:
#         str2 += i
# print(str2)