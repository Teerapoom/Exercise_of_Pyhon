print("โปรเเกรมหาจำนวนเงินส่วนลด")
product = float(input("กรุณากรอกสินค้า:>>> "))
discount = int(input("ส่วนลด(%):>>> "))
discount_baht = discount / 100 * product
payment = product - discount_baht
print("ได้รับส่วนลด", "%d" "บาท"  %discount_baht)
print("ราคาสินค้าหลังหักส่วนลด", payment ,"บาท")
