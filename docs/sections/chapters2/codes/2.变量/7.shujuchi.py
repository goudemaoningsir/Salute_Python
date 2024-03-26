# !/usr/bin/env python
# -*- coding:utf-8 -*-　

### [zhengshu]

a = 100
b = 100
print(a is b)  # 输出: True，因为两个变量引用的是内存中相同的对象

### [zhengshu]

### [zhengshu1]

a = 28891213123
b = 28891213123
print(a is b)  # 输出可能是 False，因为超出了小整数池的范围

### [zhengshu1]

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