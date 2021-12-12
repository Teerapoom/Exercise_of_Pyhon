start = 1
stop = 5
sum = 0
avg = 0
while start <= stop :
    number = float(input("ป้อนตัวเลขของคุณ: "))
    sum += number
    start += 1
print("ผลรวมของท่าน",sum)
print("ค่าเฉลี่ยของท่าน",sum/stop)

# sum = 0
# connect = 0
# while True:
#     number = float(input("ป้อนตัวเลขของคุณ: "))
#     if number == -1:
#         break;
#     else:
#         connect += 1
#         sum += number
# print("ผลรวมของท่าน",sum)
# print("ค่าเฉลี่ยของท่าน",sum/connect)