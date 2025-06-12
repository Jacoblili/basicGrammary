# If的基本用法：
import sys
from random import random, choice

age = int(input('输入你的年龄: '))
if type(age) is not int:
    print("请输入正确的格式！")
    sys.exit()

if age >= 18:
        print("你可以去网吧！")
        input("请输入身份证号：")
        input("请输入密码：")
        input("请输入充值金额：")
        items = ['A区1号', 'A区2号', 'C区3号']
        random_item = choice(items)  # 从列表中随机选择一个元素
        print("您的座位为：", random_item)
"""
import sys
from random import choice

age = int(input('请输入你的年龄: '))
if not isinstance(age, int):
    print("请输入正确的年龄格式！")
    sys.exit()

if age >= 18:
    print("你可以去网吧！")
    input("请输入身份证号：")
    input("请输入密码：")
    input("请输入充值金额：")
    areas = ['A区', 'B区', 'C区']
    random_area = choice(areas)  # 从列表中随机选择一个元素
    print("您的座位为：", random_area)
else:
    print("你还未满18岁，不能进入网吧。")
"""


# 成年人判断
# 获取键盘输入
age = int(input("请输入你的年龄："))
if age >= 18:
    print("您已经成年，游玩本地需要购票，10元/人")
print("祝您游玩愉快！")