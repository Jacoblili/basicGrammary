"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result1 = sum(my_list)
result2 = my_list[1:5:3]
print(result1)
print(result2)
my_str = "0123456789"
# [:]表示从头到尾进行切片，步数为1
result3 = my_str[::2]
result4 = my_str[::-1]
print(result3)
print(result4)
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result5 = my_tuple[10:1:-2]
print(result5)
print(type(result5))


word2 = right_Sequence.split(",")
word3 = str(word2)
word4 = word3.replace("来"," ")
print(word4)


"""
# 序列切片的练习
# “万过薪月，员序程马黑来，nohtyP学”取出黑马程序员
# 方法一
str1 = "万过薪月,员序程马黑来,nohtyP学"
right_Sequence = str1[::-1]
print(right_Sequence)
print(right_Sequence[9:14])
# 方法二
str2 = "万过薪月,员序程马黑来,nohtyP学"
word1 = str2.replace("来"," ")
word2 = word1[::-1]
word3 = word2.split(",")
print(type(word3))
print(word3[1])