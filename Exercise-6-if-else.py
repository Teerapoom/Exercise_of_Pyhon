# print("รับค่า a เเละ b เป็นเลขจำนวนเต็ม จากนั้นทำการสลับค่าตัวเเปร")
# a = int(input("a:กรอกตัวเลขจำนวนเต็ม "))
# b = int(input("b:กรอกตัวเลขจำนวนเต็ม "))
# if a < b:
#     print("a =",b)
#     print("b =",a)
# else:
#     print("กรอกข้อมูลใหม่")

# print("""\t เขียนโปรเเกรมโดยสอบถามรายได้ของผู้ใช้งานก่อนจะตัดสินใจ จะเลือกทำบัตรเคดิตเเบบใด 
#     โดยต้องมีรายได้ตั้งเเต่ 15000 บาท จึงทำบัตรเคติดได้ เเละมีเงื่อนไขการทำบัตรดังนี้
#     - หากรายได้ต่ำกว่า 70000 บาท ให้ทำบัตรเงิน
#     - หากรายได้ต่ำกว่า 100000 บาท ให้ทำบัตรทอง
#     - หากรายได้มากกว่า 100000 บาท ให้ทำบัตร platinum""")

# money = int(input("รายได้ของท่าน: "))
# if money >= 15000:
#     if money >= 100000:
#         print("บัตร platinum")
#     elif money < 70000:       
#         print("บัตรเงิน")
#     elif money < 100000:
#         print("บัตรทอง")
# else:
#     print("เงินไม่พอที่จะทำบัตร")

# print(""" \t รับค่าขนาดหน้าอก เพื่อทำการตรวจสอบขนาดของเสื้อโดยมีเงื่อนไขดังนี้
#         - ถ้าขนาดหน้าอกไม่เกิน 34 จะได้ขนาดเสื้อขนาด XS 
#         - ถ้าขนาดหน้าอกไม่เกิน 36 จะได้ขนาดเสื้อขนาด S
#         - ถ้าขนาดหน้าอกไม่เกิน 38 จะได้ขนาดเสื้อขนาด M
#         - ถ้าขนาดหน้าอกไม่เกิน 40 จะได้ขนาดเสื้อขนาด L
#         - ถ้าขนาดหน้าอกมากกว่า 40 จะได้ขนาดเสื้อขนาด XL""")
# size = int(input("กรอกขนาดหน้าอก: "))
# if size <= 34:
#     print("ขนาดเสื้อขนาด XS ")
# elif size <= 36:
#     print("ขนาดเสื้อขนาด S")
# elif size <= 38:
#     print("ขนาดเสื้อขนาด M")
# elif size <= 40:
#     print("ขนาดเสื้อขนาด L")
# else:
#     print("ขนาดเสื้อขนาด XL")

# print("รับจํานวนเต็มบวกหนึ่งจํานวน แล้วหาว่าเป็นจํานวนคู่หรือคี่")
# Number = int(input("กรอกจำนวนเต็มบวก "))
# if Number % 2 == 0:
#     print("เลขคู่")
# else:
#     print("เลขคี่")

# print("รับจํานวนเต็มบวกหนึ่งจํานวน แล้วหาว่าเป็นจํานวนที่หารด้วย 3 ลงตัวหรือไม่")
# Number = int(input("กรอกจำนวนเต็มบวก "))
# if (Number % 3) == 0:
#     print("หารลงตัว")
# else:
#     print("หารไม่ลงตัว")

# print("รับจํานวนเต็มบวกหนึ่งจํานวน แล้วหาว่าเป็นจํานวนคู่ที่หารด้วย 3 ลงตัวหรือไม่")
# Number = int(input("กรอกจำนวนเต็มบวก "))
# if Number % 2 == 0:
#         if Number % 3 == 0:
#             print("หารลงตัว")
#         else:
#             print("หารไม่ลงตัว")
# else:
#     print("เป็นเลขคี่")

# print("รับจํานวนเต็มบวกที่เป็นเลขสองหลักหนึ่งจํานวน แล้วหาว่าจํานวนนั้นมีเลขแต่ละหลักเหมือนกันหรือต่างกัน")
# Number = int(input("กรอกจำนวนเต็มบวก "))
# Ones = Number % 10
# tens = Number // 10
# if Ones == tens:
#     print("Same")
# else:
#     print("Different")

# print("รับจำนวนเต็มบวกที่เป็นเลขสองหลักหนึ่งจำนวน แล้วหาว่าจำนวนนั้นมีเลขโดดในหลักสิบมากกว่าเลขโดดในหลักหน่วยหรือไม")
# Number = int(input("กรอกจำนวนเต็มบวก "))
# Ones = Number % 10
# tens = Number // 10
# if tens > Ones:
#     print("มากกว่า")
# else:
#     print("น้อยกว่า")

# print("รับจำนวนเต็มบวกที่เป็นเลขสองหลักหนึ่งจำนวน แล้วหาว่า หลักหน่วยน้อยกว่า (หรือมากกว่า หรือเท่ากับ) หลักสิบอยู่เท่าไหร่")
# Number = int(input("กรอกจำนวนเต็มบวก "))
# Ones = Number % 10
# tens = Number // 10
# result = 0 #ผลต่าง
# if Ones < tens:
#     result = tens - Ones
#     print("Less = %d" % result)
# elif Ones > tens:
#     result = Ones - tens
#     print("Over = %d" % result)
# else:
#     print("Same")

# print("รับจํานวนเต็มบวกที่เป็นเลขสองหลักหนึ่งจํานวน แล้วหาว่าผลรวมของเลขโดดมีค่าเท่ากับ 15 หรือไม่")
# Number = int(input("กรอกจำนวนเต็มบวก "))
# Ones = Number % 10
# tens = Number // 10
# if Ones + tens == 15:
#     print ("ใช่")
# else:
#     print ("ไม่")

# print ("รับจำนวนเต็ม 3 จำนวน แล้วหาจำนวนที่มากที่สุด")
# Number_1 = int(input("กรอกจำนวนเต็มบวกตัวที่ 1: "))
# Number_2 = int(input("กรอกจำนวนเต็มบวกตัวที่ 2: "))
# Number_3 = int(input("กรอกจำนวนเต็มบวกตัวที่ 3: "))
# if Number_1 > Number_2 and Number_1 > Number_2:
#     print(Number_1)
# elif Number_2 > Number_3 and Number_2 > Number_1:
#     print(Number_2)
# else:
#     print(Number_3)

# print("รับจำนวนเต็ม 3 จำนวน แล้วหาว่าจำนวนที่มากที่สุดมากกว่าจำนวนที่น้อยที่สุดอยู่เท่าไหร")
# Number_1 = int(input("กรอกจำนวนเต็มบวกตัวที่ 1: "))
# Number_2 = int(input("กรอกจำนวนเต็มบวกตัวที่ 2: "))
# Number_3 = int(input("กรอกจำนวนเต็มบวกตัวที่ 3: "))
# max = 0
# min = 0
# if Number_1 > Number_2 and Number_1 > Number_2:
#     max = Number_1                                      
# elif Number_2 > Number_3 and Number_2 > Number_1:
#     max = Number_2
# elif Number_3 > Number_1 and Number_3 > Number_2:
#     max = Number_3

# if Number_1 < Number_2 and Number_1 < Number_2:
#     min = Number_1                                      
# elif Number_2 < Number_3 and Number_2 < Number_1:
#     min = Number_2
# elif Number_3 < Number_1 and Number_3 < Number_2:
#     min = Number_3

# result = max - min
# print(result)

# 17.
# C = int(input("กรอกอุณหภูมิหน่วยองศาเซลเซียส C :"))
# Str = input("กรอกตัวอักษร: ")
# F = ((9/5)*C)+32
# K = C + 273.15

# if Str == "F" or Str == "f":
#     print("องศาฟาเรนไฮต %.2f " %F )
# elif Str == "K" or Str == "k":
#     print("เคลวิน %.2f" %K)
# elif Str != "F" and Str != "f" and Str != "K" and Str != "k":
#     print("Error")

# print(" ค่า BMI เป็นค่าที่ใช้วัดความอ้วน เพื่อประเมินหาไขมันส่วนเกินในร่างกาย เพื่อคำนวณความเสี่ยงในการ เป็นโรค ")
# print("ซึ่ง weight มีหน่วยเป็น กิโลกรัม (kg) และ height มีหน่วยเป็น เมตร (m)")
# weight = float(input("กรอกน้ำหนักของท่าน(kg): "))
# height = float(input("กรอกส่วนสูงของท่าน(m): "))
# m = height*100
# Bmi = weight/height**2
# print("BMI is %.1f" %Bmi) 

# if Bmi < 18.5:
#     print("Underweight")
# elif Bmi < 25:
#     print("Normal weight")
# elif Bmi >= 25:
#     print("Overweight")
# else:
#     print("Obesity ")

# print(""" \t บริษัท ABC จํากัด ต้องการให้ส่วนลดลูกค้าที่ซื้อสินค้าในมูลค่าตั้งแต่ 1000 บาทขึ้นไป โดยถ้าลูกค้าซื้อ
# สินค้าตั้งแต่ 1000 บาทขึ้นไป แต่น้อยกว่า 3000 บาท ให้ส่วนลด 10% และถ้าซื้อสินค้าตั้งแต่ 3000 บาทขึ้นไป ให้
# ส่วนลด 15%  """)
# Customer = float(input("Enter buying amount: "))
# if Customer >= 1000 and Customer < 3000:
#     result = Customer*(100 - 10 )/100
#     print("Amount due after discount is %.2f baht " %result )
# else:
#     Result = Customer*(100 - 15 )/100
#     print("Amount due after discount is %.2f baht " %Result )

# print("""จงเขียนโปรแกรมสําหรับเล่นเกมทายตัวเลข โดยกําหนดให้โปรแกรมสร้างเลขเป้าหมาย (target) ที่มีค่า
# ตั้งแต่ 0 – 100 แล้วรับตัวเลขจากผู้เล่นที่ทายเข้ามา กําหนดให้เป้าหมาย (target) เท่ากับ 72""")
# target = int(input("Enter your guess (0 – 100): "))
# if target > 100:
#     print("Sorry, out of range, try again later")
# elif target == 72:
#     print("Congratulations, your guess is correct.")
# else:
#     print("Sorry, your guess is wrong, try again later")

# print("เขียนโปรแกรมเพื่อตรวจสอบ Username และ Password เพื่อตรวจสอบว่าเป็น Admin หรือไม่ กําหนดให้")
# Username = input("Username: ")
# Password = input("Password: ")

# if Username == "admin" and Password == "Ad13n@23t":
#     print("Welcome, admin ")
# else:
#     print("You are not admin")

# print("""เขียนโปรแกรมเพื่อช่วยร้านอาหารคํานวณราคา โดย Japanese buffet ราคา 1000 บาท และ Korean 
# buffet ราคา 1500 บาท ถ้าวันนี้เป็นวันพุธจะได้รับส่วนลด 15%""")
# choice = input("Enter your buffet choice: ")
# JapaneseBuffet = 1000 
# KoreanBuffet = 1500 

# if choice == "Japanese":
#     Wednesday = input("Is today Wednesday (yes/no): ")
#     if Wednesday == "yes" or Wednesday == "Yes":
#         Result = JapaneseBuffet *(100 - 15 )/100
#         print("Your payment is %.2f baht"%Result)
#     elif Wednesday == "no" or Wednesday == "No":
#         print("Your payment is %.2f bath" %JapaneseBuffet)
# elif choice == "Korean":
#     Wednesday = input("Is today Wednesday (yes/no): ")
#     if Wednesday == "yes" or Wednesday == "Yes":
#         Result = KoreanBuffet *(100 - 15 )/100
#         print("Your payment is %.2f baht"%Result)
#     elif Wednesday == "no" or Wednesday == "No":
#         print("Your payment is %.2f bath" %KoreanBuffet)
# else:
#     print("Sorry, there is no %s buffet. " %choice)

# print("ร้านขายเครื่องใช้ไฟฟ้าแห่งหนึ่ง นําเครื่องใช้ไฟฟ้าสามชนิดมาลดราคา ดังนี้")
# print(""" \t - TV ราคา 6000 บาท  
#             -  DVD player ราคา 1500 บาท 
#             - Audio System ราคา 3000 บาท
#     ร้านค้ามอบส่วนลดพิเศษ 20% ให้กับลูกค้าที่มียอดซื้ออย่างน้อย 24,000 บาท """)

# TvAmount = int(input("How many TVs: "))
# DvdAmount = int(input("How many DVD players: "))
# AudioAmount = int(input("How many Audio System: "))
# Tv = 6000
# DVd = 1500
# Audio = 3000
# TotalPrice = (Tv*TvAmount)+(DVd*DvdAmount)+(Audio*AudioAmount)
# Discount = (20/100)*TotalPrice
# payment = TotalPrice-Discount
# if TotalPrice >= 24000:
#     print("Total price is %.2f baht"%TotalPrice)
#     print("You’ve got a discount of %.2f baht"%Discount)
#     print("Your payment is %.2f baht"%payment)
# else:
#     print("Total price is %.2f baht"%TotalPrice)
#     print("Your payment is %.2f baht"%TotalPrice)