import random
target = random.randint(0,10)
i = 0
while True:
    Number = int(input("Enter a number between 0-10: "))
    i += 1
    if Number < target:
        print("The number is too low")
    elif Number > target:
        print("The number is too high")
    else:
        print("--------- You Win--------- ")
        break
print("You try {} times".format(i))
