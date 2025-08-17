
import math
#1

# string=""" Twinkle
#     twinkle
# little star
#     how I wonder what you are! Up above the world so high 
# like a diamond in the sky
#     Twinkle,
# twinkle,
#     little star 
# how I wonder what you are."""
# print( string )

#2

#a= input("user's first name is")
#b= input("user's last name is")
#print("reverse order is ",b," and ",a)

#3

# r= float(input("enter the value of radius:"))
# pi=3.14
# area=pi*r*r
# print("area of circle",area)

#4

#color_list= ["red","green","white","black"]
#print("first colour is:",color_list[0] ,"\nlast color is:",color_list[3])

#5

# n= int(input("enter your integer:"))
# result= n+pow(n,2)+pow(n,3)
# print("answer is:",result)

#6

# list=[3,5,7,23]
# print(list)
# t=tuple(list)
# print(t)

#7

# c=int(input("value in celsius"))
# f=(c*9/5)+32
# print("value in fahrenheit",f)

#8

# x=int(input("enter 1st number "))
# y=int(input("enter 2nd number "))
# temp=x
# x=y
# y=temp
# y=y+1
# print(x," and ",y)

#9

# n= int(input("enter your integer:"))
# if(n%2==0):
#     print("number is even")
# else:
#     print("number is odd")

#10

# y=int(input("enter year "))
# if(y%4==0 and y%100!=0):
#     print("year is leap year")
# else:
#     print("year is not leap year")

#11

# x1=int(input("1st x-coordinate"))
# x2=int(input("2nd x-coordinate"))
# y1=int(input("1st y-coordinate"))
# y2=int(input("2nd y-coordinate"))
# distance=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
# print("euclidean distance", distance)

#12

# a=int(input("Angle a:"))
# b=int(input("Angle b:"))
# c=int(input("Angle c:"))
# if(a+b+c==180):
#     print("It is a triangle")
# else:
#     print("It is not triangle")

#13

# p=float(input("enter principle: "))
# r=float(input("enter rate(%): "))
# t=float(input("enter time: "))
# c=p*(1+r/100)*t
# print("compound interset :",c)

#14

# n=int(input("enter number: "))
# for i in range(2,n):
#     if(n%i==0):
#         print("number is not prime")
#         break
# else:
#         print("number is prime")

#15

# n=int(input("enter number: "))
# a=n
# b=n+1
# c=(2*n)+1
# sum =(a*b*c)/6
# print("sum of series is: ",sum)
