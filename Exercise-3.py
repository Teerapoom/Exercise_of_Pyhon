# print("""\tสูตรในการเปลี่ยนค่าจากองศาเซลเซียสเป็นองศาฟาเรนไฮต์และเคลวิน มีดังนี้
#             𝐹=9/5𝐶+32
#             𝐾=𝐶+273.15
#     ให้อ่านข้อมูลอุณหภูมิ (หน่วยองศาเซลเซียส) แล้วคํานวณหาค่าองศาฟาเรนไฮต์และเคลวิน 
#     เมื่อ C คือ องศาเซลเซียส F คือ องศาฟาเรนไฮต์ และ K คือเคลวินข้อมูลเข้าหนึ่งบรรทัด 
#     ประกอบด้วยค่าอุณหภูมิหน่วยองศาเซลเซียส เป็นจํานวนจริงข้อมูลออกหนึ่งบรรทัด ประกอบด้วยตัวเลขจํานวนจริง 
#     2 จํานวน คั่นด้วยเว้นวรรค จํานวนแรกคือค่าอุณหภูมิหน่วยองศาฟาเรนไฮต์ จํานวนที่สองคือค่าอุณหภูมิหน่วยเคลวิน
# """)
# C = float(input("กรุณากรอก องศา :>>>> "))
# F = ((9/5) * C) + 32
# K = C + 273.15
# print("กด 1 เเสดงค่า องศาฟาเรนไฮต์ ")
# print("กด 2 เเสดงค่า เคลวิน ")
# data = int(input("กรอกตัวเลือกของท่าน:>>>> "))
# if data == 1:
#     print(" องศาฟาเรนไฮต์ "+"ของท่าน คือ", "%.2f" %F )
# elif data == 2:
#     print(" เคลวิน "+"ของท่าน คือ", K )
# else:
#     print("โปรดเลือกข้อมูลใหม่")

# print("โปรแกรมเพื่อคํานวณหาพื้นที่สามเหลี่ยม")
# platform = float(input("กรุณากรอกค่าฐาน:>>> "))
# high = int(input("กรุณากรอกความสูง:>>> "))
# sum = 1/2 * platform * high
# print("พื้นที่สามเหลี่ยม: %f ตร.ซม." %sum )

# print("เขียนโปรแกรมรับจํานวนเต็มมาสองจํานวน แสดงผลลัพธ์โดยใช้ operator +")
# A = input("Addition:  ")
# B = input("Concatenation:  ")
# sum = int(A) + int(B)
# print("Addition:",sum)
# print("Concatenation:",A+B)

# print("เขียนโปรแกรมรับจํานวนคะแนนสอบกลางภาค และปลายภาค ซึ่งแต่ละครั้งมีคะแนนเต็ม 60 คะแนน แล้วแสดงผลรวมและค่าเฉลี่ยของคะแนนสอบทั้งสองครั้ง")
# midterm = float(input("กรอกคะเเนนกลางภาค:>>> "))
# final = float(input("กรอกคะเเนนปลายภาค:>>> "))
# if midterm <= 60 and final <= 60:
#     Total = midterm + final
#     Average = (midterm + final)/2
#     print("Total: %.1f" %Total)
#     print("Average: %.1f " %Average)
# else:
#     print("กรุณากรอกข้อมูลใหม่")

# print(""" "\t"กำหนดให้สระว่ายน้ํา เป็นรูปสี่เหลี่ยมผืนผ้า โดยเราต้องการเติมน้ําลงไปในสระให้เต็ม จงเขียนโปรแกรมเพื่อรับความกว้าง 
#         ความยาว และความลึกของสระในหน่วยเมตร เพื่อคํานวณว่า ต้องใช้เวลากี่นาทีในการเติมน้ําลงในสระให้เต็ม 
#         เมื่อกําหนดให้ใช้เวลา 15 วินาทีในการเติมน้ํา 1 ลูกบาศก์เมตร แสดงคําตอบด้วยทศนิยมสองตําแหน่ง""")
# width = float(input("Enter width: "))
# length = float(input("Enter length: "))
# depth = float(input("Enter depth: "))
# Time = ((width * length * depth)*15)/60
# print("Time to fill a pool is %.2f minutes." %Time)