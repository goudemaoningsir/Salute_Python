# !/usr/bin/env python
# -*- coding:utf-8 -*-　

### [variable]
level = 1       # 定义一个名为level的变量，初始值为1
level = 10      # 更新变量level的值为10
is_alive = True # 定义一个名为is_alive的布尔变量，初始值为True
is_alive = False # 更新变量is_alive的值为False
name = "Albert" # 定义一个名为name的字符串变量，初始值为"Albert"
name = "AlbertMa" # 更新变量name的值为"AlbertMa"
### [variable]

### [type]
name = "Alice"
print(type(name))  # 输出: <class 'str'>

age = 30
print(type(age))  # 输出: <class 'int'>
### [type]

### [input_1]
name = input("请输入您的名字：")
print(f"您的名字是：{name}")
### [input_1]

### [input_2]
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"您的名字是：{name}")
else:
    print("请提供一个名字作为参数。")

### [input_2]
    

### [input_3]
# with open("input.txt", "r") as file:
#     name = file.readline().strip()
#     print(f"您的名字是：{name}")
### [input_3]
    

### [input_4]
import os

name = os.getenv('USER_NAME', 'Guest')
print(f"您的名字是：{name}")
### [input_4]

### [output_1]
name = "Tom"
age = 20
print("My name is %s and my age is %d years old." % (name, age))
### [output_1]

### [output_2]
name = "Tom"
age = 20
print("My name is {} and my age is {} years old.".format(name, age))
### [output_2]

### [output_3]
name = "Tom"
age = 20
print(f"My name is {name} and my age is {age} years old.")
### [output_3]

### [yinyong_1]
a = 10
b = a
### [yinyong_1]

### [yinyong_2]
x = 5
y = x
x = 3
print(y)  # y 的值仍然是 5
### [yinyong_2]

### [yinyong_3]
a = [1, 2, 3]
b = a
a.append(4)
print(b)  # b 的输出为 [1, 2, 3, 4]
### [yinyong_3]

### [yinyong_4]
def modify(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify(my_list)
print(my_list)  # 输出 [1, 2, 3, 4]
### [yinyong_4]

### [copy]
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)

original_list[0][0] = 'X'

print(original_list)          # 输出: [['X', 2, 3], [4, 5, 6]]
print(shallow_copied_list)    # 输出: [['X', 2, 3], [4, 5, 6]]
### [copy]

### [deepcopy]
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

original_list[0][0] = 'X'

print(original_list)          # 输出: [['X', 2, 3], [4, 5, 6]]
print(deep_copied_list)       # 输出: [[1, 2, 3], [4, 5, 6]]
### [deepcopy]

### [quanjubianliang]
global_var = "I am a global variable"

def my_function():
    print(global_var)  # 可以访问全局变量

my_function()
### [quanjubianliang]


### [xgquanjubianliang]
global_var = "I am a global variable"

def my_function():
    global global_var
    global_var = "Modified global variable"

my_function()
print(global_var)  # 输出: Modified global variable
### [xgquanjubianliang]

### [jububianliang]
def my_function():
    local_var = "I am a local variable"
    print(local_var)  # 在函数内部打印局部变量

my_function()
# print(local_var)  # 这会抛出错误，因为 local_var 在这个范围内是不可见的
### [jububianliang]

### [shuzi]
a = 100
b = 100
print(a is b)  # 输出: True，因为两个变量引用的是内存中相同的对象
### [shuzi]

### [shuzi1]
a = 28891213123
b = 28891213123
print(a is b)  # 输出可能是 False，因为超出了小整数池的范围
### [shuzi1]

### [zifuchuan]
a = "hello"
b = "hello"
print(a is b)  # 输出: True，因为两个字符串对象相同
### [zifuchuan]

### [zifuchuan1]
a = "".join(["he", "llo"])
b = "".join(["he", "llo"])
print(a is b)  # 输出: False，可能不是同一个对象，因为字符串是运行时生成的
### [zifuchuan1]