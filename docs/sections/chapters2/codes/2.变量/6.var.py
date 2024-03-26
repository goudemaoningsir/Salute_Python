# !/usr/bin/env python
# -*- coding:utf-8 -*-　

### [quanjudingyi]

global_var = "I am a global variable"

def my_function():
    print(global_var)  # 可以访问全局变量

my_function()

### [quanjudingyi]

### [quanjuxiugai]
global_var = "I am a global variable"

def my_function():
    global global_var
    global_var = "Modified global variable"

my_function()
print(global_var)  # 输出: Modified global variable
### [quanjuxiugai]


### [jubu]
def my_function():
    local_var = "I am a local variable"
    print(local_var)  # 在函数内部打印局部变量

my_function()
# print(local_var)  # 这会抛出错误，因为 local_var 在这个范围内是不可见的
### [jubu]