# 数一数这个字符串里有多少个a
name = "itheima is a brand of itcast"
i = 0
for x in name:
    if x == "a":
        i += 1
    else:
        pass
print(f"有{i}个字母a")