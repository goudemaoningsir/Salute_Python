# !/usr/bin/env python
# -*- coding:utf-8 -*-　

### [hello]
print("hello python")
print("hello world")
### [hello]

### [count]
count = 3 + 4 \
        + 6 + 9 \
        + 10 + 11
### [count]

### [lst]
lst = [1, 3, 4,
       5, 5, 2,
       7, 9, 10]
### [lst]

### [danhang]
# 这是第一个单行注释
print("hello 单行注释")
### [danhang]

### [danhang1]
print("hello 单行注释")  # 输出 `hello python`
### [danhang1]

### [duohang]
"""
这是一个多行注释

在多行注释之间，可以写很多很多的内容……

"""
'''
    注释1
    注释2
    注释3
'''
print("hello 多行注释")
### [duohang]

### [hanshu]
def test(param1, param2) -> str:
    """
    This is a groups style docs.

    Parameters:
        param1 - this is the first param
        param2 - this is a second param

    Returns:
        This is a description of what is returned

    Raises:
        KeyError - raises an exception
    """
    return param1 + param2
### [hanshu]

### [encoding]
s = "你好，世界！"
b = s.encode("utf-8")
print(b)
### [encoding]

### [decoding]
b = b"\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81"
s = b.decode("utf-8")
print(s)
### [decoding]

### [zijie]
import dis

def hello_world():
    print("Hello, World!")

dis.dis(hello_world)
### [zijie]

