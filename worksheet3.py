# #ques 1
# def diff(n):
#     if(n>17):
#         diff=n-17
#     else:
#         diff=abs(n-17)
#     return diff
# print("difference with 12:",diff(12))
# print("difference with 34:",diff(34))

# # ques 2
# def test_range(n):
#     if(n>100 and n<1000):
#         return True
#     elif(n==2000):
#         return True
#     else:
#         return False
# print(test_range(122))
# print(test_range(2000))
# print(test_range(12))

# # ques 3
# def reverse(s):
#     r=s[::-1]
#     return r
# print(reverse("robot"))

# # ques 4
# def count_case(s):
#     uppercase_count = 0
#     lowercase_count = 0
#     for char in s:
#         if char.isupper():
#             uppercase_count += 1
#         elif char.islower():
#             lowercase_count += 1
#     print("Uppercase letters:", uppercase_count)
#     print("Lowercase letters:", lowercase_count)
# count_case("ArMANPReet")

# # ques 5
# def list(l):
#     s=[]
#     for i in l:
#         if i not in s:
#             s.append(i)
#     return s
# print(list([1,2,3,3,4,5,5,5,6]))

# # ques 6
# def even_element(l):
#     e=[]
#     for i in l:
#         if(i%2==0):
#             e.append(i)
#     return e
# print(even_element([1,2,3,4,5,6,7,8,9,10]))

# # ques 7
# def robot():
#     print("Robot is starting")
#     def move():
#         print("Robot is moving forward")
#     move()
# robot()

# # ques 8
# def student(name, age, course):
#     student.name = name
#     student.age = age
#     student.course = course
#     print("Name:", student.name)
#     print("Age:", student.age)
#     print("Course:", student.course)
# student("arman",19,"RAI")

# # ques 9
# def move_robot(x, y, direction):
#     if (direction=="up"):
#         y+=1
#     elif(direction=="down"):
#         y-=1
#     elif(direction=="left"):
#         x-=1
#     elif(direction=="right"):
#         x+=1
#     return (x, y)
# print(move_robot(1,2,"up"))
# print(move_robot(0,0,"right"))

# # ques 10
# def classify_temperature(temp):
#     if temp<15:
#         return "cold"
#     elif 15<=temp<= 30:
#         return "moderate"
#     else:
#         return "hot"
# print(classify_temperature(32))

# #ques 11
# def path(p):
#     x=0
#     y=0
#     for direction in p:
#         if (direction=="up"):
#             y+=1
#         elif(direction=="down"):
#             y-=1
#         elif(direction=="left"):
#             x-=1
#         elif(direction=="right"):
#             x+=1
#     if(x==2 and y==0):
#         return True
#     else:
#         return False
# print(path(["up", "right", "right", "down"]))
# print(path(["up","right","left","up"]))

# # ques 12
# class student():
#     def __init__(self,student_id,student_name):
#         self.student_id=student_id
#         self.student_name=student_name
#         self.student_class=None
#     def display(self):
#         print("Student ID:", self.student_id)
#         print("Student Name:", self.student_name)
#         print("Student Class:", self.student_class)
# a=student(1024230023,"ARMAN")
# a.student_class="2w11"
# a.display()

# #ques 13
# class student():
#     def __init__(self,student_id,student_name,student_class):
#         self.student_id=student_id
#         self.student_name=student_name
#         self.student_class=student_class
#     def display(self):
#         print("Student ID:", self.student_id)
#         print("Student Name:", self.student_name)
#         print("Student Class:", self.student_class)
# a=student(1024230023,"ARMAN","2w11")
# b=student(1024,"xxxx","2w11")
# a.display()
# b.display()

# #ques 14
# import math
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi*self.radius**2
#     def perimeter(self):
#         return 2*math.pi*self.radius
# c= Circle(3)
# print("area is:",c.area())
# print("perimeter is:",c.perimeter())

# # ques 15
# class MyString:
#     def __init__(self):
#         self.input_str = ""
#     def get_String(self):
#         self.input_str = input("Enter a string: ")
#     def print_String(self):
#         print("Uppercase String:", self.input_str.upper())
# s=MyString()
# s.get_String()
# s.print_String()

# # quse 16
# class Robot:
#     def __init__(self, name, task):
#         self.name = name
#         self.task = task
#         self.battery_level = 100
#     def perform_task(self):
#         if self.battery_level>=10:
#             print(f"{self.name} is performing task: {self.task}")
#             self.battery_level-=10
#         else:
#             print(f"{self.name} has low battery. Please recharge.")
#     def recharge(self):
#         self.battery_level = 100
#         print(f"{self.name} is fully recharged.")
#     def status(self):
#         print(f"Name: {self.name}")
#         print(f"Task: {self.task}")
#         print(f"Battery Level: {self.battery_level}%")
# r=Robot("RoboMax", "Cleaning")
# r.perform_task()
# r.status()
# r.recharge()
# r=Robot("RoboMax", "dancing")
# r.status()