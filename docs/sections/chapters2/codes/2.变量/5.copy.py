# !/usr/bin/env python
# -*- coding:utf-8 -*-　

### [shallowcopy]

import copy
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)

original_list[0][0] = 'X'

print(original_list)          # 输出: [['X', 2, 3], [4, 5, 6]]
print(shallow_copied_list)    # 输出: [['X', 2, 3], [4, 5, 6]]

### [shallowcopy]

### [deepcopy]

import copy

original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

original_list[0][0] = 'X'

print(original_list)          # 输出: [['X', 2, 3], [4, 5, 6]]
print(deep_copied_list)       # 输出: [[1, 2, 3], [4, 5, 6]]
### [deepcopy]