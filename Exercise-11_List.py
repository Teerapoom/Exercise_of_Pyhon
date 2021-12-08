# x =  ["dog", "cat", "hamster"]

# ต้องการเพิ่มข้อมูล “snake” ไปที่ท้ายสุดของ list
# x.append("snake")
# print(x)

# ต้องการเพิ่มข้อมูล “bird” ไปยังตําแหน่งที่ 2
# x.insert(2, "bird")
# print(x)

# ต้องการลบข้อมูลตัวสุดท้าย
# x.pop()
# print(x)

# ต้องการลบข้อมูล “dog” 
# x.remove("dog")
# print(x)

# ต้องการเรียงข้อมูลในลิสต์
# x.sort()
# print(x)

# ต้องการกลับข้อมูลในลิสต์ 
# x.reverse()
# print(x)

# ต้องการคัดลอกลิสต์ x ใส่ในตัวแปร y
# mylist = x.copy()
# print(mylist)

# ต้องการนําข้อมูลในลิสต์ y ต่อท้ายลิสต์ x
# xx =  ["dog", "cat", "hamster"]
# tropical = ["mango", "pineapple", "papaya"]
# xx.extend(tropical)
# print(xx)
# x.extend(mylist)
# print(x)

# ลบข้อมูลใน y ออกทั้งหมด
# del mylist
# mylist.clear()
# print(mylist)

# แสดงผล x และ y 
# print(x)
# print(mylist)

# รับค่าตัวเลขเข้ามาเรื่อยๆ เก็บค่าลงในลิสต์ หยุดรับเมื่อเป็น -1 จากนั้นแสดงค่าของลิสต์
# mylist = []
# while True:
#     n = int(input("กรอกข้อมูล: "))
#     if n == -1:
#         break
#     else:
#         mylist.append(n)
# print(mylist)

# 12. รับค่าข้อความเข้ามา แล้วทําการนับว่ามีทั้งหมดกี่ตัวอักษร โดยใช้ลิสต์ในการเก็บข้อมูล
# str = input("กรอกข้อมูล: ")
# list = list(str)
# count = 0
# for i in list:
#     count += 1
# print(count)


# รับค่าตัวเลขเป็นจํานวนเต็มเข้ามาเรื่อยๆ จนกว่าจะป้อน -1 จึงหยุด แล้วทําการกลับตัวเลข
# mylist = []
# while True:
#     n = int(input("กรอกข้อมูล: "))
#     if n == -1:
#         break
#     else:
#         mylist.append(n)
#         mylist.reverse()
# print(mylist)

# รับค่าตัวเลขจํานวนเต็ม 5 ตัว เก็บไว้ในลิสต์ บรรทัดละตัว จากนั้นทําการหาผลรวมของตัวเลขทุกตัวที่
# รับเข้ามา และหาค่าเฉลี่ย 
# list = []
# sum = 0
# i = 1
# while i <= 5:
#     n = int(input("กรอกข้อมูล: "))
#     list.append(n)
#     i += 1
# for i in list:
#     sum += i
# avg = sum / len(list)
# print(avg)

# เขียนโปรแกรมรับค่าคะแนนของนักเรียน 10 คน เป็นจํานวนเต็ม แล้วหาค่าสูงสุด ค่าต่ําสุด และค่าเฉลี่ย 
# โดยคะแนนเต็มคือ 10 คะแนน
# list = []
# max = 0
# min = 9999999
# sum = 0
# for i in range (10):
#     score = int(input("กรอกข้อมูล: "))
#     list.append(score)
# for i in list:
#     sum += i
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# avg = sum / len(list)
# print("Max = %d" %max)
# print("Min = %d" %min)
# print("average = %d" %avg)

# จากข้อที่แล้ว ถ้าผู้ใช้ไม่ได้กรอกคะแนนในช่วง 0-10 ให้แสดงข้อความเตือน “Score out of range” แล้ว
# ทําการกรอกข้อมูลตัวนั้นซ้ําใหม่จนกว่าจะถูก
# list = []
# max = 0
# min = 9999999
# sum = 0
# while True:
#     score = int(input("กรอกข้อมูล: "))
#     if score >= 0 and score <= 10:
#         list.append(score)
#     else:
#         print("Score out of range")
#     if len(list) == 10:
#         break
# for i in list:
#     sum += i
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# avg = sum / len(list)
# print("Max = %d" %max)
# print("Min = %d" %min)
# print("average = %d" %avg)

# รับข้อความเข้ามา ความยาวไม่เกิน 30 ตัวอักษร แล้วแสดงผลข้อความที่ตัดสระ
# vowel =["a","e","i","o","u"]
# str = input("กรอกข้อมูล: ")
# list = list(str)
# for i in str:
#     if i in vowel:
#         list.remove(i) 
# print(list)
