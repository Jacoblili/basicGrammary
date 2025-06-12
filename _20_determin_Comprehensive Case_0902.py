# 导入Python内置随机库
import random

# 构建一个随机的数学变量
num = random.randint(1, 10)
heart_num = int(input("请在1~10之间猜一个数字："))
# 通过if判断语句进行数字的猜测
if heart_num == num:
    print("太厉害了，一次性就猜对了！")
else:
    if heart_num > num:
        print("太大了,请重新猜！")
    else:
        print("你猜测的数字太小了！")
    heart_num = int(input("请重新继续在1~10之间猜一个数字："))
    if heart_num == num:
        print("不错哦，第二次就猜对了！")
    else:
        if heart_num > num:
            print("太大了,请重新猜！")
        else:
            print("你猜测的数字太小了！")
        heart_num = int(input("请重新继续在1~10之间猜一个数字："))
        if heart_num == num:
            print("还好猜对了！")
        else:
            if heart_num > num:
                print("太大了,请重新猜！")
            else:
                print("你猜测的数字太小了！")
