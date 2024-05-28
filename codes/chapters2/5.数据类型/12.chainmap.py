#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
chain_map = ChainMap(dict1, dict2)

print(chain_map["b"])  # 输出: 2

chain_map["c"] = 5  # 更新dict1中的'c'，如果不存在则添加到dict1
print(chain_map)
del chain_map["c"]  # 从dict1中删除'c'
print(chain_map)

new_dict = {"e": 5, "f": 6}
new_chain_map = chain_map.new_child(new_dict)
print(new_chain_map)

print(list(new_chain_map.keys()))  # 输出所有键
print(list(new_chain_map.values()))  # 输出所有值
