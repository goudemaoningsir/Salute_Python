# !/usr/bin/env python
# -*- coding:utf-8 -*-　

### [bukebian]

x = 5
y = x
x = 3
print(y)  # y 的值仍然是 5

### [bukebian]

### [kebian]
a = [1, 2, 3]
b = a
a.append(4)
print(b)  # b 的输出为 [1, 2, 3, 4]
### [kebian]

### [hanshu]
def modify(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify(my_list)
print(my_list)  # 输出 [1, 2, 3, 4]
### [hanshu]