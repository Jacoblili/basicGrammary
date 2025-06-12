"""

def COVID_2019 (num):
    print("你好！请你出示一下核酸证明！\n不出示就过去不！！！")

for i in range(10):
    COVID_2019(i)

if __name__ == "__main__":
    COVID_2019(i)


x = float(input("请输入第一个数："))
y = float(input("请输入第二个数："))
# 函数的传入参数
def add(x,y):
    result = x + y
    print(f"{x}+{y}={result}")
if __name__ == "__main__":
    add(x,y)
"""

# 实例：体温监测
def check (a):
    """

    :param a:形参a是被测人员的实时体温显示
    :param a:
    :return: 返回实时值，同时再通过if条件判断返回不同的打印输出
    """
    print("请您出示您的核酸检验码，并将额头靠近传感器！")
    input(f"正在测量您当前的体温......\n 您当前体温为：{a}摄氏度")
    if a >= 37.2 or a <= 36.1:
        print("您体温似乎不太正常!\n 请您及时休息就医！")
    else:
        print("祝您天天幸福愉快，身体健康！")
check(36.5)
check(45)

# 函数返回值
#（1） return 函数的运行结果
#（2） None 类型<class 'NoneType'>

# 函数的说明文档：通过多行注释的形式对函数进行说明解释，但应注意内容要写在函数体的前面