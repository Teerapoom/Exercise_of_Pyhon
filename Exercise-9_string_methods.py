# print("จงเขียนโปรแกรมเพื่อให้ได้ผลลัพธ์ตามตัวอย่าง โดยใช้ string methods")
# x = "you are my destiny"
# ข้อ1 You are my destiny
# print(x.capitalize())

# ข้อ2 you ARE my destiny
# print(x.replace("are","ARE"))

# ข้อ 3 You are mY destiny
# result1 = x.replace("my","mY")
# result2 = result1.replace("you","You")
# print(result2)
# วิธีที่2
# result = "Y" + x[1:9] + "Y" + x[10:]
# print(result)

# ข้อ 4 You Are My Destiny
# print(x.title())

# ข้อ 5 ต้องการทราบว่า “r” อยู่ตําแหน่งใด
# print(x.find("r"))

# ข้อ 6 ข้อความลงท้ายด้วย “d” หรือไม่
# print(x.endswith("d"))

# ข้อ 7 ข้อความเป็นตัวพิมพ์เล็กทั้งหมดหรือไม่
# print(x.islower())

# ข้อ 8 ข้อความขึ้นต้นด้วยตัวพิมพ์ใหญ่หรือไม่
# print(x[0].isupper())

# ข้อ 9 ข้อความลงท้ายด้วยตัวพิมพ์เล็กหรือไม่
# print(x[-1].islower())

# ข้อ 10 จงเขียนโปรแกรมเพื่อหาความยาวคําสุดท้ายของประโยค
# str1 = input()
# count = 0
# for i in range(len(str1)-1,-1,-1):
#     if str1[i] == " ":
#         break
#     else:
#         count += 1
# print(count)
"""
จงเขียนโปรแกรมเพื่อตรวจสอบว่าการตั้ง username ถูกต้องหรือไม่ โดยมีเกณฑ์ดังนี้ 
  - username ต้องอยู่ระหว่าง 4-25 ตัวอักษร 
  - ต้องขึ้นต้นด้วยตัวอักษร 
  - สามารถประกอบด้วย ตัวอักษร, ตัวเลข และ underscoreได้ 
  - ต้องไม่ลงท้ายด้วย underscor
"""
alpha = "abcdefghijklmnopqrstuvwxyz"
u_score = "_"
numbers = "0123456789"
username = input("username: ")
status = 1
if len(username) >= 4 and len(username) <= 25:
    if username[0].isalnum():
        for i in username:
            if i not in alpha and i not in u_score and i not in numbers:
                status = 0
        if status == 0:
            print("No")
        elif status == 1:
            if not(username.endswith("_")):
                print("Yes")
            else:
                print("No")
    else:
        print("No")
else:
    print("No")
