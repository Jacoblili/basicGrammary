# 函数的定义域分为：1、局部变量 2、全局变量
# gloabl关键字声明a是全局变量
num = 100
def A():
    print(num)
def B():
    # 使用global改变全局变量
    global num
    num = 200
    print(num)
A()
B()
print(num)