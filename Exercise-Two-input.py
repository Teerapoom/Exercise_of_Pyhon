# print("จงแสดงผลข้อมูลต่อไปนี้ให้ถูกต้องโดยกําหนดให้(ทําด้วยตัวเองก่อน หลังจากนั้นตรวจสอบกับโปรแกรม)")
# a = 25
# b = 1253.59845
# c = "python"
#print(“Hello %s programming” % c)
#print("Hello %s programming" % c)

#print(“a = %d” %a)
#print("a = %d" % a )

#print(“b = %d” % b)
#print("b = %d" % a) 
# print("""   Just because something
#         thinks differently from you,
#         does that mean it’s not thinking ?""")

# a = 12.5
# print(">>> %.1f" % a)

# a = 2
# b = 3
# print(">>>>>", a , "x" , b , "=" ,a*b)

# a = 2.4
# b = 2.5
# sum = a + b
# print(">>>", a ,"+", b , "=" , "%.4f" %sum)

# a = 5
# b = 2
# sum = a - b
# print(">>>", "%.2f" % a ,"+", "%.2f" %b , "=" , "%.4f" %sum)

# birthday = 25
# print("ฉันเกิดวันที่", birthday )

# a = 5
# b = 100
# print(">>>>", a , "เท่าของ", b , "มีค่าเท่ากับ" , a*b )

#จงเขียนโปรแกรม ให้พิมพ์ข้อความว่า “Good morning” ออกมาทางหน้าจอ
# a = "Good morning"
# print('"', a , '"')

# จงเขียนโปรแกรม ให้พิมพ์ดาวออกมาแสดงดังตัวอย่างข้างล่างนี้
# *
# **
# ***
# print("""  *
#             **
#              ***
# """)
# print("*")
# print("**")
# print("***")

#รับค่าตัวเลขเข้ามา 2 จํานวน แล้วทําการหาผลรวมของสองตัวเลข25
# number1 = int(input("กรอกตัวเลข>>>"))
# number2 = int(input("กรอกตัวเลข>>>"))
# sum  = number1 * number2
# print("ผลลัพธ์",sum)

# a = input("กรอก *")
# b = int(input("กรอกตัวเลข>>> "))
# print(a * b)

#print("รับค่าตัวเลขจํานวนเต็ม 3 จํานวน จากนั้นทําการหาค่าเฉลี่ย")
# number1 = int(input("กรอกตัวเลข>>>"))
# number2 = int(input("กรอกตัวเลข>>>"))
# number3 = int(input("กรอกตัวเลข>>>"))
# sum = (number1 + number2 + number3 )/3
# print("ตอบ",sum)

# print(""" จงเขียนโปรแกรมรับข้อมูลน้ําหนักและส่วนสูง พร้อมแสดงผล
#     ข้อมูลนําเข้า
#         บรรทัดแรก รับค่า weight เป็นจํานวนเต็ม
#         บรรทัดที่ 2 รับค่า height เป็นจํานวนเต็ม
#         """)
# weight = float(input("กรอกน้ำหนักของท่าน>>> "))
# height = float(input("กรอกส่วนสูงของท่าน>>> "))/100
# BMI = weight/(height*height)
# print("ค่า BMI ของท่าน"," %.2f "%BMI)

# print(""" จงเขียนโปรแกรมรับอักขระจํานวน 1 ตัวอักษร แล้วแสดงผลข้อมูล
#     ข้อมูลเข้า
#         บรรทัดแรก รับอักขระจากแป้นพิมพ์จํานวน 1 ตัวอักษร
#     ข้อมูลออก
#         แสดงข้อความ “You Press” ตามด้วย ช่องว่าง 1 ช่อง และตามด้วยอักขระที่รับเข้ามา
# """)
# str = input("กรอกข้อมูล: ")
# a = "A"
# A = "a"
# if str == a :
#     print('"'+" You Press "+'"')
# elif str == A:
#     print('"'+" You Press "+'"')
# else:
#     print("กรอกข้อมูลใหม่")

# print("""กําหนดให้ m และ n เป็นตัวแปรชนิดขํานวนเต็ม ให้รับค่าตัวเลขเข้ามา 2 จํานวน แล้วแสดงผลลบของทั้ง2 จํานวน
#     ข้อมูลเข้า
#         บรรทัดแรก รับค่า m เป็นเลขจํานวนเต็มบรรทัดที่ 2รับค่า n เป็นเลขจํานวนเต็ม
#     ข้อมูลออก
#         บรรทัดเดียว แสดงผลลบของ m กับ n
# """)
# m = int(input("กรอกตัวเลขตัวที่ 1>>> "))
# n = int(input("กรอกตัวเลขตัวที่ 2>>> "))
# sum = m - n
# print(m , "-" , n , "=" , sum )

# print(""" จงเขียนโปรแกรม รับค่า ชื่อนามสกุลและ อายุ พร้อมแสดงผลดังตัวอย่าง
#     ข้อมูลเข้า 
#         บรรทัดแรก รับชื่อจริง(แสดงข้อความว่า “Enter your first name: ” ก่อนรับค่า)
#         บรรทัดที่2รับนามสกุล(แสดงข้อความว่า “Enter your last name: ” ก่อนรับค่า)
#         บรรทัดที่ 3 รับอายุ(แสดงข้อความว่า “Enter your age: ” ก่อนรับค่า)
#     ข้อมูลออก
#     บรรทัดแรก แสดงผล “Hello” ตามด้วยชื่อและนามสกุลคั่นด้วยช่องว่าง
#     บรรทัดที่ 2 แสดงผล “You’re” ตามด้วยอายุ แล้วตามด้วย “years old”
# """)
# fname = input("Enter your firstname: ")
# Lname = input("Enter your lastname: ")
# age = int(input(" Enter your age:"))
# print("Hello",fname,Lname)
# print("You’re",age,"years old")