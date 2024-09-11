import random
random_int = random.randint(1,10)
num = int(input("请输入一个1-10的数"))
while num != random_int:
    if num > random_int:
        print("猜大了")
    else:
        print("猜小了")
    num = int(input("请输入一个1-10的数"))

print("恭喜你猜对了")