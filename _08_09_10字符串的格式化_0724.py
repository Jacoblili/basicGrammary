# 通过占位的形式完成拼接
name = "李帅"
message0 = "今天熬夜的是：%s" % name
print(message0)
# 数字与字符串的拼接（多个占位符拼接需要用括号按顺序写变量）
class_num = 57
avg_salary = 14000
message2 = "他的班级是:%s，平均工资是:%s" % (class_num, avg_salary)
print("",message2)

# %s,%d,%f的应用以及对字符串精度的控制（m限制宽度，n限制小数点精度）
name = "BaiDu"
setup_year = 1995
stock_price = 19.945
message2 = "%s 成立于 %5d,今天的股价是 %f" % (name,setup_year,stock_price)
message3 = "%s 成立于 %d,今天的股价是 %10f" % (name,setup_year,stock_price)
message4 = "%s 成立于 %d,今天的股价是 %8.2f" % (name,setup_year,stock_price)
message5 = "%s 成立于 %d,今天的股价是 %.2f" % (name,setup_year,stock_price)
print(message2)
print(message3)
print(message4)
print(message5)