# a = "I'm good at programming"
# print(a[0:])
# print(a[4:8])
# print(a[12:23])
# print(a[12:23:2])
# print(a[-1:-24:-1])
# print(a[:3:]+""+a[12:])

# print("รับตัวอักษรเข้ามา 1 ตัว แล้วตรวจสอบว่าเป็นสระในภาษาอังกฤษหรือไม่")
# StringOne = input("กรอกข้อมูล: ")
# if StringOne in "aeiouAEIOU":
#     print("Yes")
# else:
#     print("No")

# print("รับข้อความเข้ามา จากนั้นให้พิมพ์ความยาวของข้อความนั้นออกมา")
# StringOne = input("กรอกข้อมูล: ")
# print("ความยาวตัวอักษรของคุณ:>>>",len(StringOne))

# print("รับข้อความเข้ามา แล้วตรวจสอบว่ามีสระทั้งหมดกี่ตัว (นับตัวซ้ํา)")
# StringOne = input("กรอกข้อมูล: ")
# connect = 0
# for x in StringOne :
#     if x in "aeiouAEIOU":
#         connect += 1
# print(connect)

# print("รับข้อความเข้ามา แล้วตรวจสอบว่ามีสระทั้งหมดกี่ตัว โดยให้แสดงดังนี้")
# StringOne = input("กรอกข้อมูล: ")
# connect_a = 0
# connect_e = 0
# connect_i = 0
# connect_o = 0
# connect_u = 0
# for x in StringOne :
#     if x == "a":
#         connect_a += 1
#     elif x == "e":
#         connect_e += 1
#     elif x == "i":
#         connect_i += 1
#     elif x == "o":
#         connect_o += 1
#     elif x == "u":
#         connect_u += 1
# print("a =",connect_a)
# print("e =",connect_e)
# print("i =",connect_i)
# print("o =",connect_o)
# print("u =",connect_u)
# total = connect_a + connect_e  + connect_i + connect_o +connect_u
# print("total =",total)


# print("รับข้อความเข้ามา แล้วทําการ reverse (กลับข้อความ) ")
# StringOne = input("กรอกข้อมูล: ")
# result = ""
# for i in range(len(StringOne)-1,-1,-1):
#     result += StringOne[i]
# print(result)

# print("รับข้อความเข้ามา แล้วตรวจสอบว่าเป็นพาลินโดรม(palindrome) หรือไม่")
# StringOne = input("กรอกข้อมูล: ")
# result = ""
# for i in range(len(StringOne)-1,-1,-1):
#     result += StringOne[i]
# if StringOne ==  StringOne:
#     print("Yes")
# else:
#     print("No")