# เขียนฟังก์ชันเพื่อบวกเลข 2 ตัว และ return ผลลัพธ์ออกมา กําหนดให้ฟังก์ชันนี้รับ parameter 2 ตัว คือ a และ b
# def my_function(a,b):
#     sumOne = a + b
#     return sumOne
# a = my_function(1,2)
# print(a)

# เขียนฟังก์ชันเพื่อยกกําลังสองเลข 1 ตัว และ return ผลลัพธ์ออกมา กําหนดให้ฟังก์ชันนี้รับ parameter
# 1 ตัว คือ a
# def my_function(a):
#     sum = a**2
#     answer = print("answer %d" %sum)
#     return answer
# my_function(3)

# เขียนฟังก์ชันเพื่อหาผลบวกกําลังสองของสมาชิกใน list และ return ผลลัพธ์ออกมา 
# def my_function(mylist):
#     sum = 0
#     for i in mylist:
#         sum += i**2 
#     return sum
# print(my_function([1,2,3]))

# เขียนฟังก์ชันเพื่อต่อสายอักขระ 3 สายเข้าด้วยกัน และ return ผลลัพธ์ออกมา กําหนดให้ฟังก์ชันนี้รับ
# parameter 3 ตัว คือ str1, str2 และ str3
# def my_function(str1,str2,str3):
#     print(str1+str2+str3)
# my_function("ja","m","e")
# def my_function(str1,str2,str3):
#     result = str1+str2+str3
#     return result
# print(my_function("ja","m","e"))


# เขียนฟังก์ชันเพื่อลดราคาสินค้า และ return ราคาหลังได้รับส่วนลดแล้ว กําหนดให้รับ parameter 2 ตัว
# คือ price และ discount เป็นเปอร์เซ็นต์
# def my_function(price,discount):
#     a = price * discount
#     note = a / 100
#     answer = price - note
#     return answer
# print(my_function(1000,20))
# def my_function(price,discount):
#     answer= price - (price * discount /100)
#     return answer
# print(my_function(1000,20))

# เขียนฟังก์ชันเพื่อค้นหาตําแหน่งใน list โดยรับ parameter 2 ตัว ได้แก่ ls (ไม่มีข้อมูลซ้ํา) และ  k ซึ่งเป็น
# ข้อมูลที่ต้องการค้นหา รอคำตอบ
# def find_index(ls,k):
#     if k in ls:
#         index = []
#         for i in range(len(ls)):
#             if ls[i] == k:
#                 index.append(i)
#         return index
#     else:
#         return -1
# print(find_index([1,2,3,4],3))

# เขียนโปรแกรมรับเลขเดือน 1-12 แล้วแสดงผลเป็นชื่อของเดือนที่ได้รับมาบนจอภาพ เช่น รับเลข 5 ให้
# แสดง May เป็นต้น โดยให้ออกแบบเป็นฟังก์ชันำ
# def my_function():
    # month = int(input("Month = "))
    # if month == 1:
    #     print("Month = January")
    # elif month == 2:
    #     print("Month = February")
    # elif month == 3:
    #     print("Month = March")
    # elif month == 4:
    #     print("Month = April")
    # elif month == 5:
    #     print("Month = May")
    # elif month == 6:
    #     print("Month = June")
    # elif month == 7:
    #     print("Month = July")
    # elif month == 8:
    #     print("Month = August")
    # elif month == 9:
    #     print("Month = September")
    # elif month == 10:
    #     print("Month = October")
    # elif month == 11:
    #     print("Month = November")
    # elif month == 12:
    #     print("Month = December")
    # else:
    #     print("fill in new information")
# my_function()
# month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
# def find_month(a):
#     result = month[a-1]
#     return result
# m = int(input())
# print(find_month(m))

# เขียนโปรแกรมหาค่าต่ําสุดของข้อมูลจาก list ขนาด 5 จํานวน โดยให้ออกแบบเป็นฟังก์ชัน 
# def my_function():
#     i = 0
#     list = []
#     min = 9999999
#     while i < 5:
#         n = int(input("กรอกข้อมูล: "))
#         print("รอบที่",i)
#         list.append(n)
#         i += 1
#     for i in list:
#         if i < min:
#             min = i
#     print(min)
# my_function()
# def find_min(ls):
#     min = 999999
#     for i in ls:
#         if i < min:
#             min = i
#     return min
# print(find_min([1,2,3]))



