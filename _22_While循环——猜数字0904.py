# while循环的猜数字游戏
# 获取范围在1~100的随机数字
import random
num = random.randint(1,100)
# 通过一个boolean类型的变量做循环是否继续的标志
flag = True
count = 0
while flag:
    guess = int(input("请输入你心里猜的数字："))
    count += 1
    if guess == num:
        print("猜对啦！")
        flag = False
    else:
        if guess > num:
            print("猜大了！")
        else:
            print("猜小了！再试试！")
print(f"所以你一共猜了{count}")




