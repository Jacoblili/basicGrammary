student_tuple = ("Jay",30,["football","music"])
print(f"该学生年龄所在的下标位置是{student_tuple.index(30)}")
name = student_tuple[0]
print(f"该学生的姓名是：{name}")
hobby = student_tuple[2]
hobby.remove("football")
hobby.append("coding")
print(f"增加后的爱好是{hobby}")

# str的遍历
str1 = "A B C D E"
x = 0
for i in str1:
    print(i)
while x < len(str1):
    print(str1[x])
    x += 1