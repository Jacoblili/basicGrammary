# 带有成员方法的类
# 成员变量
# 成员方法

class Student(object):
    def __init__(self, name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def show(self):
        print(f"{self.name},今年{self.age}岁，已经得到积分{self.score}")

    @staticmethod  # 静态方法，不使用self来访问实例的属性或者方法
    def say(msg):
        print(f"Hello,{msg}")


if __name__ == '__main__':
    student1 = Student("Jacob",18, 100)  # 基于类创建对象
    # student1.name = "Jacob"
    # student1.age = 18
    # student1.score = 100
    student1.show()
    student1.say("认识大家很高兴！")
