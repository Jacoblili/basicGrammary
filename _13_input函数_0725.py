# 通过input获取键盘上输入的内容，并使用一个变量进行接收
"""
print("你的名字是什么？")
name = input()
print("我的名字是：%s" % name)
"""

# 对比以上内容
name1 = input("请输入你的名字：")
print("%s" % name1)
password = input("请输入银行卡密码：")  # input()函数默认接受的数据类型为：字符串类型
password = int(password)
print("银行卡密码类型是：",type(password))

input("请输入密码：")

print("输入密码成功，银行卡还剩余1413960元！")
