# #导入'random'模块，进行随机操作
import random

# #使用choice()，从给出的列表中随机选取一个数值

# # print('A random number from list is :',end='')
# # print(random.choice([1,2,3,4,5,6,7]))


# # #使用randrange()函数生成一个给定范围内的随机数。

# # print('A random number from range is :',end='')
# # print(random.randrange(20,50,3))

# #输出浮点数
# print ("A random number between 0 and 1 is : ", end="") 
# print (random.random()) 
  
# #使用seed()生成一个随机种子 
# random.seed(5) 
  
# # 打印映射的随机数
# print ("The mapped random number with 5 is : ", end="") 
# print (random.random()) 
  
# # 生成另外一个随机种子
# random.seed(7) 
  
# print ("The mapped random number with 7 is : ", end="") 
# print (random.random()) 
  
# #再一次用5作为参数
# random.seed(5) 
  

# print ("The mapped random number with 5 is : ",end="") 
# print (random.random()) 
  
# #再一次用7作为参数 
# random.seed(7) 
  

# print ("The mapped random number with 7 is : ",end="") 
# print (random.random()) 

# 初始化列表 
li = [1, 4, 5, 10, 2] 
  
# 打印重排之前的list 
print ("The list before shuffling is : ", end="") 
for i in range(0, len(li)): 
    print (li[i], end=" ") 
print("\r") 
  
# 重拍 
random.shuffle(li) 
  
# 打印重排之后的list
print ("The list after shuffling is : ", end="") 
for i in range(0, len(li)): 
    print (li[i], end=" ") 
print("\r") 

#使用uniform()生成给定范围内的浮点数
print ("The random floating point number between 5 and 10 is : ",end="") 
print (random.uniform(5,10)) 