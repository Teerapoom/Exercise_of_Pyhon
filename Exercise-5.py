import math
# x = int(input("กรอกค่า x : "))
# y = math.sqrt(16 - 4 * x)
# print(y)

# x = int(input("กรอกค่า x : "))
# y = math.sqrt(16 - 4 * math.pow(x, 2))
# print(y)

# print("จงเขียนโปรแกรมเพื่อแปลงเลขจํานวนเต็มลบ ให้เป็นจํานวนเต็มบวก")
# Number = int(input("กรุณากรอกตัวเลขจำนวนจริงติดลบ: "))
# change = abs(Number)
# print(change)

# print("จงเขียนโปรแกรมเพื่อแปลงเลขจํานวนเต็มลบ ให้เป็นจํานวนเต็มบวก")
# Number = float(input("กรุณากรอกตัวเลขจำนวนจริงติดลบ: "))
# change = math.ceil(abs(Number))
# print(change)

print("""จงเขียนโปรแกรมเพื่อคํานวณหาพื้นที่วงกลมและเส้นรอบวงของวงกลมที่มีรัศมี r 
    กําหนดให้ข้อมูลเข้าเป็นเลขจํานวนเต็มเท่านั้น แสดงพื้นที่และเส้นรอบวงเป็นเลขจํานวนจริงทศนิยมสองตําแหน่ง""")
circle = int(input("Enter a radius:"))
area = math.pi * circle ** 2 
circum = 2 * math.pi * circle
print("Area of a circle with radius %d is %.2f" %(circle,area))
print("Circumference of a circle with radius  %d is %.2f"%(circle,circum))