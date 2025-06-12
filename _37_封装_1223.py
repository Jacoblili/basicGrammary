"""
class Phone:
    __current_voltage = 1

    def __keep_single_core(self):
        print("CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 5:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法开启5G通话！")
iphone = Phone()
iphone.call_by_5g()

"""
class Phone:
    __is_5G_enable = False

    def __check_5G(self):
        if self.__is_5G_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G网络")
    def call_by_5g(self):
        self.__check_5G()
        print("正在通话中。。。。。。")
bphone = Phone()
bphone.call_by_5g()

squares = [x**2 for x in range(10)]
print(squares)
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
        print(count)
print(count_up_to(10))