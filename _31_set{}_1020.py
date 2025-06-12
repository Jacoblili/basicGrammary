"""
empty_set = set()
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 3, 4, 5, 6, 7}
set3 = set1.difference(set2)

print(set1)
print(set3)
"""
my_list = ['《瓦尔登湖》','《百年孤独》','《人间失格》','《第七天》','《兄弟》','《我们生活在巨大的差距里》']
empty_set = set()
i = 1
for element in my_list:
    print(f"列表中有第{i},书名叫{element}")
    empty_set.add(element)
    i += 1
print(f"新生成的集合里有{empty_set}，一共{len(empty_set)}本书!!!")

# 字典的嵌套
student_dict = {"Jacob":{"math":99,"english":98,"physics":97}}
print(student_dict)
print(student_dict["Jacob"]["physics"])

