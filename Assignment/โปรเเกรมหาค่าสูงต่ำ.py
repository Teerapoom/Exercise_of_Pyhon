max = 0
min = 99999999
while True:
    number = float(input("กรอกตัวเลข: "))
    if number < 0 :
        break
    if number > max :
        max = number
    if number < min:
        min = number
print("ค่าสูงสุด: ", max)
print("ค่าต่ำสุด: ", min)