# !/usr/bin/env python
# -*- coding:utf-8 -*-
def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()

# 使用next()函数访问生成器的下一个元素
print(next(gen))  # 输出 1
print(next(gen))  # 输出 2
print(next(gen))  # 输出 3

# 再次尝试调用next()将抛出StopIteration，因为生成器已经没有元素可以返回了


def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


for count in countdown(5):
    print(count)
