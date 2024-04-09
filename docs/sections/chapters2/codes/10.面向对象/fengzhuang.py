class Example:
    def __init__(self, public_var):
        self.public_var = public_var

    def public_method(self):
        return "This is a public method."


ex = Example("public value")

print(ex.public_var)  # 输出 "public value"
print(ex.public_method())  # 输出 "This is a public method."


class Example:
    def __init__(self, public_var, private_var):
        self.public_var = public_var
        self.__private_var = private_var

    def public_method(self):
        return "This is a public method."

    def __private_method(self):
        return "This is a private method."


ex = Example("public value", "private value")

print(ex.public_var)  # 输出 "public value"
print(ex.public_method())  # 输出 "This is a public method."
# print(ex.__private_var)  # 报错，无法访问私有变量
# print(ex.__private_method())  # 报错，无法访问私有方法
