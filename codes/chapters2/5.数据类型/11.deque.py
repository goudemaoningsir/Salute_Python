#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque

my_deque = deque()  # 定义
my_deque = deque([1, 2, 3, 4, 5])

my_deque.append(6)  # 右端添加
print(my_deque)
my_deque.appendleft(0)  # 左端添加
print(my_deque)

right = my_deque.pop()  # 弹出右端元素
print(my_deque)
left = my_deque.popleft()  # 弹出左端元素
print(my_deque)

my_deque.extend([7, 8, 9])  # 右侧扩展
print(my_deque)
my_deque.extendleft([0])  # 左侧扩展
print(my_deque)

limited_deque = deque(maxlen=3)
limited_deque.extend([1, 2, 3])
print(limited_deque)
limited_deque.append(4)  # [2, 3, 4]
print(limited_deque)

my_deque.rotate(1)  # 右旋转1步
print(my_deque)
my_deque.rotate(-1)  # 左旋转1步
print(my_deque)
