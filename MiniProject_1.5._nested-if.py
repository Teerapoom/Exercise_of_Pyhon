sore = int(input("กรุณากรอกคะเเนนขิงคุณ:>>>>> "))
if sore >= 80:
    print(" คุณได้เกรด A ")
elif sore >= 70:
    if sore >= 75:
        print(" คุณได้เกรด B+ ")
    else:
        print("  คุณได้เกรด B  ")
elif sore >= 60:
    if sore >= 65:
        print(" คุณได้เกรด C+ ")
    else:
        print("  คุณได้เกรด C  ")
elif sore < 60:
    if sore >= 55:
        print(" คุณได้เกรด D+ ")
    elif sore < 55 and sore >= 50:
        print("  คุณได้เกรด D  ")
    else:
        print(" คุณได้เกรด F ")
else:
        print("  GG  ")
print(" ตั้งใจเรียนนะครับนักเรียน ")