from collections import UserDict


class MyDict(UserDict):
    # 添加自定义行为
    def __setitem__(self, key, value):
        # 只允许字符串作为键
        if not isinstance(key, str):
            raise TypeError("Keys must be strings")
        super().__setitem__(key, value)


my_dict = MyDict()
my_dict["key"] = "value"  # 正常工作
print(my_dict)
try:
    my_dict[123] = "value"  # 将引发TypeError
except TypeError as e:
    print(e)  # 输出：Keys must be strings
