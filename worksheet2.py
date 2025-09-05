
import math
import random as r
import string as s
# ques 1
# list=[11, 12, 13, 14]
# print(list)

# #1
# list.append(50)
# list.append(60)
# print("add 50 and 60 in list",list)

# #2
# list.remove(11)
# list.remove(13)
# print("remove 11 and 13 in list ",list)

# #3
# list.sort()
# print("list in asending order ",list)

# #4
# list.reverse()
# print("list in descending order",list)

# #5
# for i in range(len(list)):
#     if(list[i]==13):
#         print("13 is in list")
#         break
# else:
#     print("13 is not in list")

# #6
# size=len(list)
# print("number of element",size)

# #7
# sum=0
# for i in range(len(list)):
#     sum=sum+list[i]
# print("sum of all element",sum)    

# #8
# sum=0
# for i in range(len(list)):
#     if(list[i]%2!=0):
#         sum=sum+list[i]
# print("sum of odd element",sum)

# #9
# sum=0
# for i in range(len(list)):
#     if(list[i]%2==0):
#         sum=sum+list[i]
# print("sum of even element",sum)

# ques 2   

# list2=[1,2,3,4,5,6,7]
# sum=0
# for i in list2:
#     sum=sum+i
# print("sum of all elements in list: ",sum)

# ques 3

# list3=[1,2,3,4,5]
# multiply=1
# for i in list3:
#     multiply=multiply*i
# print("multiply of all element in list3",multiply)

# # ques 4
# array_3d=[]
# for i in range(3):  
#     layer=[]
#     for j in range(4):  
#         row=[]
#         for k in range(6): 
#             row.append("*")
#         layer.append(row)
#     array_3d.append(layer)
# for layer in array_3d:
#     for row in layer:
#         print(row)

# # ques 5
# d={1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# #1
# d[8]=8.8
# print("after adding key 8",d)

# #2
# d.pop(2)
# print("after removing key 2",d)

# #3
# print(6 in d)

# #4
# print("number of element ",len(d))

# #5
# sum=0
# for i in d.values():
#     sum=sum+i
# print("sum of all element:",sum) 

# #6
# d[3]=7.1
# print(" after updating the value of 3",d)

# #7
# d.clear()
# print("after clearing d",d )

# ques 6

# s1= {10,20,30,40,50,60}
# s2= {40,50,60,70,80,90}

# #1
# s1.add(55)
# s1.add(66)
# print("after adding 55 and 66 in s1:",s1)

# #2
# s1.remove(10)
# s1.remove(30)
# print("after removing 10 and 30 from s1:",s1)

# #3
# print(40 in s1)

# #4
# u=s1.union(s2)
# print("union of s1 and s2",u)9

# #5
# intsection=s1.intersection(s2)
# print("intersection between S1 and S2",intsection)

# #6
# diff=s1.difference(s2)
# print("S1-S2",diff)

# ques 7

# #1
# characters=s.ascii_letters
# for i in range(100):
#     length=r.randint(6,8)
#     random_string=''.join(r.choices(characters,k=length))
#     print(random_string)

# #2
# for num in range(600, 801):
#     is_prime = True
#     if num < 2:
#         is_prime = False
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#     if is_prime:
#         print(num)
        
#3
# print("all numbers btw 100 and 1000 that are divisible by 7 and 9:")
# for num in range(100, 1001):
#     if(num%7==0 and num%9==0):
#         print(num)

# ques 8

# exam_st_date = (11, 12, 2025)
# print("The examination will start from:")
# print(exam_st_date[0] ,"/", exam_st_date[1] ,"/", exam_st_date[2])

# ques 9

# list=[10,231,34,565,45,24,70,29,25,75,200]
# for i in list:
#     if(i%5==0):
#         print(i)

# ques 10

# n=int(input("enter the number"))
# is_even=(n%2==0)
# if is_even:
#     print("the number is even")
# else:
#     print("number is odd")

# ques 11

# text="Emma is writer. Emma is lina's sister. Emma palys football"
# count=text.count("Emma")
# print(count)

# ques 12

# list_1=[12,13,1,30,5,6]
# list_2=[1,45,6,21,8,9,10]
# new_list=[]
# for i in list_1:
#       if i%2!=0:
#             new_list.append(i)
# for j in list_2:
#       if j%2==0:
#             new_list.append(j)            
# print("new list is:",new_list)          
    
# ques 13

# positions = [(2,3), (4,5), (6,7), (7,8)]
# print("x-coordinate is even")
# for i in positions:
#     if i[0]%2==0:
#         print(i)

#ques 14

# sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
# print("sensor IDs whose reading is above 3.0")
# for i in sensor_data.values():
#     if i>3:
#         print(i)

# ques 15

# commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
# commands_executed = {"MOVE", "TURN_LEFT", "STOP"}
# not_executed=commands_received-commands_executed
# print("commands not executed by the robot",not_executed)
   



