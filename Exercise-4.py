# print("""\t จงเขียนโปรแกรมรับค่า n ซึ่งเป็นเลขจํานวนเต็มบวก และรับอักขระ 2 ตัว บรรทัดละตัว 
# แล้วพิมพ์อักขระความยาว n ตัวในบรรทัดเดียวกัน โดยให้พิมพ์อักขระ 2 ตัว สลับกัน โดยไม่ใช้ if-else or loop""")
# Number = int(input("Enter Number:>>> "))
# Str_1 = input("Enter Str:>>> ")
# Str_2 = input("Enter Str:>>> ")    # "#$"
# Mob = Number % 2
# SumNumber = (Str_1 + Str_2) * (Number // 2) + (Mob * Str_1)
# print(SumNumber) 

# print(""" \t จงเขียนโปรแกรมเพื่อรับค่าเศษ (numerator) และค่าส่วน (denominator) ของเศษส่วน(fraction) สองจํานวน 
#         แล้วคํานวณหาผลรวมของเศษส่วนทั้งสองสมมติให้เศษส่วนแรกอยู่ในรูป a/b 
#         และเศษส่วนที่สองอยู่ในรูป c/d ในที่นี้ให้แสดงผลลัพธ์ p/q ซึ่งเป็นผลรวมที่ได้ในรูปเศษส่วนเช่นกัน 
#         และไม่ต้องทําให้เป็นเศษส่วนอย่างต่ํา""")

# print("First fraction")

# a = int(input(">>Enter a numerator a: "))
# b = int(input(">>Enter b denominator b: "))

# print("Second fraction")

# c = int(input(">>Enter c  numerator c: "))
# d = int(input(">>Enter a denominator d: "))
# NewNumerator = ( a * d ) + (b * c)
# denominator = (b * d)
# print("Summation of the two fractions is %d / %d" %(NewNumerator,denominator ))


# print(""" \t จงเขียนโปรแกรมเพื่อรับจํานวนวินาทีที่ใช้ออกกําลังกาย 
#       2 ครั้ง แล้วแสดงผลเวลารวมที่ใช้ในการออกกําลังกายในรูปของจํานวนชั่วโมง 
#       นาที และวินาที ตามลําดับ """)

# a = int(input("Enter your exercise time 1:>> "))
# b = int(input("Enter your exercise time 2:>> "))
# min =  (a + b)/60
# hr = min/60
# sec = ((a+b)%3600)%60
# print("It is %d hours %d minutes and %d seconds."%(hr,min,sec))