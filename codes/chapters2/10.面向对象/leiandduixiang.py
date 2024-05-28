class Dog:
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 行为/方法
    def bark(self):
        print(f"{self.name} is barking!")


# 创建一个名为"Rex"，年龄为5的Dog对象
rex = Dog("Rex", 5)

# 调用rex的bark方法
print(rex.bark())


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)


person = Person("Tom")
person.say_hello()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建一个Person对象
person1 = Person("John", 30)

# 访问对象的属性
print(person1.name)  # 输出: John
print(person1.age)  # 输出: 30


class Example:
    def __init__(self, id):
        self.id = id
        print(f"Object with id {self.id} created")

    def __del__(self):
        print(f"Object with id {self.id} destroyed")


# 创建一个对象
obj = Example(1)

# 删除对象的引用，触发垃圾回收
del obj


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name: {self.name}, age: {self.age})"


# 创建一个Person对象
person1 = Person("John", 30)

# 使用print函数打印对象
print(person1)


class Person:
    """表示一个人的类。

    属性:
        name (str): 人的名字。
        age (int): 人的年龄。
    """

    def __init__(self, name, age):
        """初始化Person对象。

        参数:
            name (str): 人的名字。
            age (int): 人的年龄。
        """
        self.name = name
        self.age = age


# 访问类的文档字符串
print(Person.__doc__)


class MyClass:
    pass


print(MyClass.__module__)


obj = MyClass()
print(obj.__class__)


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


# 创建一个Adder实例
add_five = Adder(5)

# 使用实例像函数一样调用
print(add_five(10))  # 输出: 15


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建一个Person对象
person = Person("John", 30)

# 访问对象的__dict__属性
print(person.__dict__)

# 修改对象的属性
person.__dict__["age"] = 31

# 添加新属性
person.__dict__["gender"] = "Male"

# 再次打印修改后的__dict__
print(person.__dict__)
