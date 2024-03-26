# !/usr/bin/env python
# -*- coding:utf-8 -*-　

### [minglinghang]
name = input("请输入您的名字：")
print(f"您的名字是：{name}")
### [minglinghang]


### [minglinghang1]
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"您的名字是：{name}")
else:
    print("请提供一个名字作为参数。")

### [minglinghang1]
    
### [wenjian]
# with open("input.txt", "r") as file:
#     name = file.readline().strip()
#     print(f"您的名字是：{name}")
### [wenjian]
    
### [huanjing]
import os

name = os.getenv('USER_NAME', 'Guest')
print(f"您的名字是：{name}")
### [huanjing]