# Determine the nesting of statements
# 判断           嵌套
# 现在公司要发礼物，但条件是：必须大于18岁小于40岁且入职时间需要大于两年或者级别大于3
age = 20
year = 5
level = 1
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 3:
            print("可以领取")
        elif level > 3:
            print("可以领取")
        else:
            print("no!!")
    else:
        print("年龄有一点小")
else:
    print("no")





"""
import random

# 随机生成一个目标数字
heart_num = random.randint(1, 100)  # 可以设置为其他范围
print("猜出我心中的数字是多少（1到100）")

# 游戏主循环
while True:
    guess = int(input("请输入你的猜测: "))

    if guess == heart_num:
        print("猜对了！！！")
        break
    else:
        if guess < heart_num:
            print("猜的数字太小了。")
            if heart_num - guess >= 50:
                print("差距较大，试着猜更大一点。")
            elif heart_num - guess >= 30:
                print("差距中等，试着猜更大一点。")
            else:
                print("差距较小，试着猜更大一点。")
        else:
            print("猜的数字太大了。")
            if guess - heart_num >= 50:
                print("差距较大，试着猜小一点。")
            elif guess - heart_num >= 30:
                print("差距中等，试着猜小一点。")
            else:
                print("差距较小，试着猜小一点。")

"""
