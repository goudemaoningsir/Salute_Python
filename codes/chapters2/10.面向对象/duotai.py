class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute


my_object = MyClass("I am an instance attribute")
print(my_object.instance_attribute)  # 输出 "I am an instance attribute"
print(my_object.class_attribute)  # 输出 "I am a class attribute"

my_object.instance_attribute = "I am a new instance attribute"
print(my_object.instance_attribute)  # 输出 "I am a new instance attribute"

my_object.class_attribute = "I am an instance attribute now"
print(my_object.class_attribute)  # 输出 "I am an instance attribute now"

# del my_object.instance_attribute
# print(my_object.instance_attribute)  # 抛出 AttributeError 异常


class MyClass:
    class_attribute = "I am a class attribute"

    @classmethod
    def class_method(cls):
        print("This is a class method of", cls.__name__)
        print("The class attribute is", cls.class_attribute)


MyClass.class_method()  # 输出 "This is a class method of MyClass" 和 "The class attribute is I am a class attribute"
my_object = MyClass()
my_object.class_method()  # 输出 "This is a class method of MyClass" 和 "The class attribute is I am a class attribute"
