"""
import time
f = open('D:/Python_practice/PythonStudy/_33fileWritetest_1024.txt', 'w', encoding="utf-8")
f.write("今天是程序员的节日！")  # 会将内容写到内存中
f.flush()  # 将内存中积攒的内容写入到磁盘中
f.close()  # close方法内置flush功能
"""
f = open("_33fileWritetest_1024.txt", "a", encoding="utf-8")  # a = append
f.write("\n月薪过万！！！")
f.close()