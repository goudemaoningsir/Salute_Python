#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict

# 创建一个默认值为list的defaultdict
dd_list = defaultdict(list)

# 创建一个默认值为int的defaultdict
dd_int = defaultdict(int)

# 创建一个默认值为set的defaultdict
dd_set = defaultdict(set)
# 向dd_list中添加元素
dd_list["a"].append(1)
dd_list["a"].append(2)
print(dd_list)
# 向dd_int中添加元素
dd_int["key"] += 1
print(dd_int)

# 向dd_set中添加元素
dd_set["item"].add("value")
print(dd_set)
