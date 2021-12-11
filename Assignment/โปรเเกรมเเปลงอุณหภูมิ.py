temp = input("ป้อนอุณหภูมิ(องศร): ")

degree = int(temp[:-1])
unit = temp[-1].upper()

if unit == "C":
    result = (9*degree)/5+32
    print("แปลงตัวเลข = ",temp,"เป็น ฟานเรนไฮน์","%.2f" %result)
if unit == "F":
    result01 = (degree-32)*5/9
    print("แปลงตัวเลข = ",temp,"เป็น เซลเซียส","%.2f" %result01)
else:
    print("กรุณากรอกหน่วยให้ถูกต้อง")