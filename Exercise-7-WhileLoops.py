print("เขียนคําสั่งโดยใช้ลูป while เพื่อให้แสดงผลลัพธ์ต่อไปนี้ออกทางหน้าจอ")

# print("1, 3, 5, 7, 9, 11, 13, 15")
# i = 1
# while i <= 15:
#     print(i) #อีกเเบบ print("%d, "% i , end="")
#     i += 2


# print("2, 5, 8, 11, 14, 17")
# i = 2
# while i <= 17:
#     print(i)
#     i += 3


# print("30, 20, 10, 0, -10, 20, -30")
# i = 30
# while 30 >= -30:
#     print(i)
#     # i -= 10 #ถ้าใส่ตรงนี้จะไม่มีการ print(-30) เพราะมันจะ break เลย
#     if i == -30:
#         break
#     i -= 10

# print("15, 23, 31, 39, 47, 55")
# i = 15
# while i <= 55:
#     print(i)
#     i += 8

# print("พิมพ์จํานวนเต็มตั้งแต่ 0 ถึง 100")
# i = 0
# while i <= 100:
#     print(i)
#     i += 1

# print("รับจํานวนเต็มบวกมา 1 จํานวน แล้วพิมพ์จํานวนเต็มตั้งแต่ 0 ถึง จํานวนเต็มบวกที่รับเข้ามา")
# Number = int(input("กรอกตัวเลขนวนเต็มบวก: "))
# i = 0
# if Number >= 0:
#     while i <= Number:
#         print(i)
#         i += 1
# else:
#     print("โปรเเกรมไม่รับเลขติดลบ")

# print("พิมพ์จํานวนเต็มตั้งแต่ 100 ถึง 0")
# i = 100
# while i >= 0:
#     print(i)
#     i -= 1

# print("รับจํานวนเต็มบวกมา 1 จํานวน แล้วพิมพ์จํานวนเต็มตั้งแต่จํานวนเต็มบวกที่รับเข้ามา ถึง 0")
# Number = int(input("กรอกตัวเลขนวนเต็มบวก: "))
# while Number >= 0 :
#     print(Number)
#     Number -= 1

# print("รับข้อมูลเข้าจํานวนจริงบวกบรรทัดละจํานวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จํานวนจริงบวก แล้วหาผลบวกของจํานวนจริงบวกทั้งหมดที่รับเข้ามา")
# sum = 0
# while True:
#     Number = int(input("กรอกตัวเลขนวนเต็มบวก: "))
#     if Number < 0:
#         break
#     else:
#         sum += Number #ที่บวกได้เพราะว่าเราตัว Number ไปเก็บในSum
# print(sum)

# print("รับข้อมูลเข้าจํานวนจริงบรรทัดละจํานวน หยุดรับเมื่อข้อมูลเข้าเป็น 0 แล้วหาว่าจํานวนจริงที่รับเข้ามามีจํานวนจริงบวกกี่จํานวน และจํานวนจริงลบกี่จํานวน")
# count1 = 0
# count2 = 0
# while True:
#     Number = int(input("กรอกตัวเลขนวนเต็มบวก: "))
#     if Number == 0:
#         break
#     else:
#         if Number > 0:
#             count1 += 1 #ที่ไม่บวกเพราะว่ามันไม่ได้เอา Number มันเเค่ทำรอบ
#         elif Number < 0:
#             count2 += 1
# print(count1)
# print(count2)

# print("รับข้อมูลเข้าจํานวนจริงบวกบรรทัดละจํานวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จํานวนจริงบวก แล้วหาค่าเฉลี่ยของจํานวนจริงบวกทั้งหมดที่รับเข้ามา")
# count = 0 #จำนวนของข้อมูล
# sum = 0 #ข้อมูลทั้งหมด
# answer = 0 #เก็บคำตอบ
# while True:
#     Number = int(input("กรอกตัวเลขนวนเต็มบวก: "))
#     if Number < 0 :
#         break
#     else:
#         sum += Number
#         count += 1
#         answer = sum/count
# print("ค่าเฉลี่ยของท่านคือ {:,.2f}".format(answer))

# 12
# print("รับข้อมูลเข้าจํานวนจริงบวกบรรทัดละจํานวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จํานวนจริงบวก แล้วหาจํานวนจริงบวกที่มีค่ามากที่สุดจากจํานวนจริงบวกทั้งหมดที่รับเข้ามา")
# max = 0
# while True:
#     Number = int(input("กรอกตัวเลขนวนเต็มบวก: "))
#     if Number < 0 :
#         break
#     else:
#         if Number > max:
#             max = Number
# print(max)

# print("รับข้อมูลเข้าจํานวนจริงบวกบรรทัดละจํานวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จํานวนจริงบวก แล้วหาจํานวนจริงบวกที่มีค่าน้อยที่สุดจากจํานวนจริงบวกทั้งหมดที่รับเข้ามา")
# low = 999999999999999999999
# while True:
#     Number = int(input("กรอกตัวเลขนวนเต็มบวก: "))
#     if Number < 0:
#         break
#     else:
#         if Number < low :
#             low = Number
# print(low)

# print(""" \t รับข้อมูลเข้าจํานวนจริงบวกบรรทัดละจํานวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จํานวนจริงบวก แล้วหาผลต่างของ จํานวนจริงบวกที่มีค่ามากที่สุด
# และจํานวนจริงบวกที่มีค่าน้อยที่สุด จากจํานวนจริงบวกทั้งหมดที่รับเข้ามา โดยใช้ Loop เดียว""")
# max = 0
# low = 999999999999999999999
# while True:
#     Number = int(input("กรอกตัวเลขนวนเต็มบวก: "))
#     if Number < 0:
#         break
#     else:
#         if  Number > max:
#             max = Number #เก็บค่าเดียว
#         else:
#             low = Number #เก็บค่าเดียว
# answer = max - low
# print(abs(answer))

# 15
# print("รับข้อมูลเข้าจำนวนเต็มบรรทัดละจำนวน หยุดรับเมื่อข้อมูลเข้าเป็น -1 จากนั้นทำการหาผลรวมของข้อมูลที่รับเข้ามา")
# sum = 0
# while True:
#     Number = int(input("กรอกตัวเลขนวนเต็มบวก: "))
#     if Number < 0:
#         break
#     else:
#         sum += Number
# print(sum)

# print(""" \t เขียนโปรแกรมรับเลขจํานวนเต็มเข้ามา ถ้าเป็นเลขจํานวนเต็มบวกให้พิมพ์หลักเลขออกมาทีละหลักต่อ
# หนึ่งบรรทัด โดยเริ่มจากหลักที่มีค่าน้อยสุด (หลักหน่วย) ถ้ารับอินพุตเป็นเลข 0 หรือจํานวนเต็มลบ ให้พิมพ์คําว่า 
# “ERROR”""")
# while True:
#     Number = int(input("กรอกตัวเลข: "))
#     if Number <= 0:
#         print("Error")
#         break
#     else:
#         UnitNumber = Number % 10
#         print(UnitNumber)
#         Hundred = ((Number//10)%10)
#         print(Hundred)
#         MainUnit = (Number//100)
#         print(MainUnit)
# วิธีที 2
# Number = int(input("กรอกตัวเลข: "))
# if Number <= 0:
#         print("Error")
# else:
#     i = Number
#     while i > 0:
#         a = i % 10
#         print(a)
#         i //= 10 


# print("เขียนโปรแกรมรับค่าจํานวนเต็มเข้ามาจนกว่าจะเป็นเลขติดลบ จากนั้นตรวจสอบว่ามีตัวเลขที่เป็นเลขคี่ทั้งหมดกี่จํานวน")
# count = 0
# while True:
#     Number = int(input("กรอกตัวเลข: "))
#     if Number < 0:
#         break
#     else:
#         if Number % 2 != 0:
#             count += 1
# print("Received {:,d} odd numbers".format(count))

#18
# n = int(input("กรอกข้อมูล:"))
# sum = 0
# i = n
# while i > 0:
#     a  = i % 10
#     sum += a
#     i //= 10
# if sum % 9 == 0:
#     print("Yes %d" % sum)
# else:
#     fraction = sum % 9
#     print("No %d" %fraction )

#19
# count = 0
# target = 72
# while True:
#     n = int(input("Enter your guess: "))
#     count += 1
#     if n == target:
#         print("Congratulations, your guess is correct.")
#         break
#     else:
#         if n < 0 or n > 100:
#             print("Sorry, your guess is out of range")
#         elif n < target:
#             print("Sorry, your guess is too low")
#         elif n > target:
#             print("Sorry, your guess is too high")
# print("Total number of guesses is %d "%count)

#20
# high = 0
# count = 0
# while True:
#     Number = int(input("Enter your Number: "))
#     if Number == -1:
#         break
#     else:
#         if Number > high:
#             high = Number
#             count += 1
# print(count)
        
#21
# Number = int(input("Enter Number: "))
# i = Number
# sum = 0
# while i > 0:
#     a = i % 10
#     sum += a 
#     i //= 10
# if sum < 10:
#     print(sum)
# else:
#     while True:
#         if sum < 10:
#             break
#         else:
#             i = sum
#             sum = 0
#             while i > 0:
#                 a = i % 10
#                 sum += a
#                 i //= 10
#     print(sum)
#22
# i = 1
# sum = 0
# while True:
#     if i > 10:
#         break
#     else:
#         print("Frame # %d "% i)
#         n1 = int(input("Number of pins down: "))
#         sum += n1
#         if n1 == 10:
#             i += 1
#         else:
#             print("Frame # %d" %i)
#             n3 = 10 - n1
#             n2 = int(input("Number of pins down (0 - %d): "%n3))
#             i += 1
#             sum += n2
#     print("Total score is %d" %sum)