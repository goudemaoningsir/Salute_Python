# !/usr/bin/env python
# -*- coding:utf-8 -*-

### [jbsy]
# 定义一个匿名函数，接受两个参数，返回它们的和
sum = lambda a, b: a + b

# 使用
print(sum(5, 3))  # 输出: 8

### [jbsy]


### [gjhs]
# 使用map()函数和匿名函数对列表中的每个元素加3
nums = [1, 2, 3, 4]
result = map(lambda x: x + 3, nums)
print("==================")
print(result)

print(list(result))  # 输出: [4, 5, 6, 7]
### [gjhs]


### [fzhs]
def make_incrementor(n):
    return lambda x: x + n


inc_by_2 = make_incrementor(2)
print(inc_by_2(5))  # 输出: 7
### [fzhs]
