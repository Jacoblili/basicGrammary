# 定义一个函数，接受其他函数的输入
def test_func(compute):
    result = compute(1,2)
    print(f"结果是：{result}")

# 通过lambda匿名函数的形式，将匿名函数作为参数输入
test_func(lambda x,y: x + y) # just 1 line

my_list = input("请输入多个整数数值，并使用逗号“，”隔开：")
num = map(int,my_list.split(","))
odd = filter(lambda x: x % 2 != 0,num)
odd_list = list(odd)
print(f"这些整数中的奇数分别是：{odd_list}")