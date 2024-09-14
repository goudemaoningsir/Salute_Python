## 10、命名元组（namedtuple）

命名元组是Python标准库`collections`模块中的一个功能，它扩展了基本的元组类型，允许你为元组中的每个位置指定名称，从而使代码更加可读和自文档化。命名元组是不可变的，就像普通元组一样，但是可以通过字段名而不是索引号来访问数据，提高了程序的可读性。

### （1）定义

首先需要从`collections`模块中导入`namedtuple`函数，然后使用它来定义一个命名元组类型。

```python
from collections import namedtuple

# 定义一个命名元组类型，名称为'Person'，字段有'name'和'age'
Person = namedtuple('Person', ['name', 'age'])
```

一旦定义了命名元组类型，就可以创建该类型的实例了。

```python
alice = Person(name='Alice', age=30)
```

命名元组的元素可以通过名称访问，这比使用索引访问更加清晰。

```python
print(alice.name)  # 'Alice'
print(alice.age)  # 30
```

也可以像普通元组一样通过索引访问：

```python
print(alice[0])  # 'Alice'
print(alice[1])  # 30
```

### （2）常用操作

虽然命名元组是不可变的，但你可以使用`_replace()`方法来创建内容被修改的新实例。

```python
bob = alice._replace(name='Bob')
print(bob)  # Person(name='Bob', age=30)
```

为什么使用命名元组？

- **可读性**：通过字段名访问元组元素比通过索引访问更加直观。
- **不可变性**：与列表相比，命名元组是不可变的，这意味着它们可以作为字典的键或者集合的元素。
- **轻量级**：命名元组是基于元组的，比使用完整的类定义更节省内存。

命名元组提供了一种便捷的方式来处理只有少数属性但没有方法的对象，如数据库记录或其他结构化数据。通过使用命名元组，你可以让这些数据结构更加清晰和自文档化。

## 11、双端队列（deque）

`deque`，全名为双端队列（Double-Ended Queue），是Python中`collections`模块提供的一种数据结构。它类似于列表，但是在两端进行添加和删除操作时更高效，因此被称为“超级列表”。`deque`支持线程安全的、快速从两端添加（append）和弹出（pop）的操作，非常适合用作队列和栈。

### （1）定义deque

要使用`deque`，首先需要从`collections`模块导入它：

```python
from collections import deque
```

然后可以像创建列表一样创建`deque`对象：

```python
my_deque = deque([1, 2, 3, 4, 5])
```

或者创建一个空的`deque`对象，并通过操作来添加元素：

```python
my_deque = deque()
```

### （2）常用操作

#### 1）添加元素

- `append(x)`：在右端添加一个元素。
- `appendleft(x)`：在左端添加一个元素。

```python
my_deque.append(6)  # 右端添加
my_deque.appendleft(0)  # 左端添加
```

#### 2）弹出元素

- `pop()`：移除并返回右端的一个元素。
- `popleft()`：移除并返回左端的一个元素。

```python
right = my_deque.pop()  # 弹出右端元素
left = my_deque.popleft()  # 弹出左端元素
```

#### 3）扩展

- `extend(iterable)`：在右侧添加多个元素。
- `extendleft(iterable)`：在左侧添加多个元素（注意，添加的序列元素将会反序出现在`deque`的左端）。

```python
my_deque.extend([7, 8, 9])  # 右侧扩展
my_deque.extendleft([0])  # 左侧扩展
```

#### 4）限制长度

`deque`可以设置最大长度，当超过设定的最大长度时，新添加元素会导致相对另一端的元素被移除。

```python
limited_deque = deque(maxlen=3)
limited_deque.extend([1, 2, 3])
limited_deque.append(4)  # [2, 3, 4]
```

#### 5）旋转元素

- `rotate(n)`：将`deque`向右旋转`n`步（如果`n`为负数，则向左旋转）。

```python
my_deque.rotate(1)  # 右旋转1步
my_deque.rotate(-1)  # 左旋转1步
```

## 12、链映射（ChainMap）

`ChainMap`是Python中`collections`模块的一部分，用于将多个字典或其他映射合并为一个单一的视图。当你有多个字典并希望将它们逻辑上合并为一个字典来查询时，`ChainMap`非常有用。它可以高效地重用字典，因为它只是创建了一个包含所有底层字典的列表，而不是创建一个完全独立的新字典。

### （1）定义

要使用`ChainMap`，首先需要从`collections`模块导入它：

```python
from collections import ChainMap
```

然后可以通过传递多个映射（如字典）来创建`ChainMap`对象：

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain_map = ChainMap(dict1, dict2)
```

在这个例子中，`chain_map`会首先搜索`dict1`，然后是`dict2`来查找键值对。

### （2）常用操作

#### 1）访问元素

可以像操作普通字典一样通过键来访问`ChainMap`中的元素。如果相同的键在多个字典中出现，`ChainMap`会返回第一个找到的值。

```python
print(chain_map['b'])  # 输出: 2
```

#### 2）更新/添加元素

向`ChainMap`添加元素时，元素会被添加到第一个映射中。

```python
chain_map['c'] = 5  # 更新dict1中的'c'，如果不存在则添加到dict1
```

#### 3）删除元素

从`ChainMap`中删除元素时，元素会从第一个映射中删除。

```python
del chain_map['c']  # 从dict1中删除'c'
```

#### 4）新映射

使用`new_child()`方法可以向`ChainMap`添加新的字典，该字典会被放在搜索顺序的最前面。

```python
new_dict = {'e': 5, 'f': 6}
new_chain_map = chain_map.new_child(new_dict)
```

#### 5）键和值的列表

- `keys()`方法返回所有键的视图。
- `values()`方法返回所有值的视图。

```python
print(list(new_chain_map.keys()))  # 输出所有键
print(list(new_chain_map.values()))  # 输出所有值
```

`ChainMap`提供了一种高效的方式来处理多个字典，使得多个映射可以被逻辑上合并为一个。这对于在多个配置源（如多个配置文件、环境变量和命令行参数）之间进行查找和更新时非常有用。通过使用`ChainMap`，可以避免合并字典时的性能损失，并且保留了底层字典的结构和数据。

## 13、计数字典（Counter）

`Counter`是Python中`collections`模块提供的一个子类，用于计数可哈希对象。它是一个字典的子类，提供了用于计算每个元素出现次数的快捷方式。`Counter`非常适合用于统计数据项的频率，例如，统计字符出现的次数、列表中元素的出现频率等。

### （1）定义

要使用`Counter`，首先需要从`collections`模块导入它：

```python
from collections import Counter
```

然后可以直接使用`Counter`来创建计数字典。它可以接受多种类型的输入，如列表、字典、字符串等。

```python
# 从列表创建
counter_list = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

# 从字符串创建
counter_string = Counter("abracadabra")

# 从字典创建
counter_dict = Counter({'red': 4, 'blue': 2})
```

### （2）常用操作

#### 1）更新计数

可以使用`update()`方法添加数据，更新元素的计数。

```python
counter_list.update(['blue', 'green'])
```

#### 2）访问计数

直接通过元素作为键来访问其计数。

```python
print(counter_list['blue'])  # 输出blue的计数
```

#### 3）元素

使用`elements()`方法可以返回一个迭代器，包含了每个元素重复计数次数的所有元素。

```python
list(counter_string.elements())  # ['a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
```

#### 4）最常见的元素

`most_common(n)`方法返回计数最高的`n`个元素及其计数的列表。

```python
counter_list.most_common(2)  # [('blue', 4), ('red', 2)]
```

#### 5）计数相减

`subtract()`方法从计数中减去元素。

```python
counter_list.subtract(['red'])
```

#### 6）计数字典运算

`Counter`对象支持加法、减法、交集和并集等运算。

```python
# 加法
c1 = Counter(['red', 'blue'])
c2 = Counter(['blue', 'yellow'])
print(c1 + c2)  # Counter({'blue': 2, 'red': 1, 'yellow': 1})

# 减法
print(c1 - c2)  # Counter({'red': 1})

# 交集
print(c1 & c2)  # Counter({'blue': 1})

# 并集
print(c1 | c2)  # Counter({'blue': 1, 'red': 1, 'yellow': 1})
```

`Counter`是处理计数问题的强大工具，它提供了一种简单方便的方法来统计元素的频率。通过其提供的各种方法和运算，可以轻松实现对数据的统计分析需求。

## 14、有序字典（OrderedDict）

`OrderedDict`是Python中`collections`模块的一个子类，它记住了字典对象中元素被插入的顺序。从Python 3.7开始，普通的`dict`类型也是有序的，但是`OrderedDict`在某些情况下仍有其独特的用途和功能，比如它的等价性测试是基于插入顺序的，而普通字典的等价性测试则是基于键值对的。

### （1）定义

要使用`OrderedDict`，首先需要从`collections`模块导入它：

```python
from collections import OrderedDict
```

然后可以使用`OrderedDict()`来创建一个有序字典对象：

```python
my_ordered_dict = OrderedDict([('a', '1'), ('b', '2'), ('c', '3')])
```

或者可以创建一个空的`OrderedDict`对象，然后通过赋值来添加元素：

```python
my_ordered_dict = OrderedDict()
my_ordered_dict['a'] = '1'
my_ordered_dict['b'] = '2'
my_ordered_dict['c'] = '3'
```

### （2）常用操作

#### 1）保持顺序

`OrderedDict`保持元素插入时的顺序，这在遍历或序列化时非常有用。

```python
for key, value in my_ordered_dict.items():
    print(key, value)
```

#### 2）更新元素而不改变顺序

如果更新已存在的键的值，它的位置不会改变。

```python
my_ordered_dict['a'] = 'updated'
```

#### 3）移动元素到末尾

`OrderedDict`有一个`move_to_end()`方法，可以快速将一个键移动到字典的开头或末尾。

```python
my_ordered_dict.move_to_end('a')  # 将键'a'移动到末尾
my_ordered_dict.move_to_end('b', last=False)  # 将键'b'移动到开头
```

#### 4）弹出首/末元素

可以使用`popitem()`方法弹出字典的最后一个或第一个键值对。

```python
my_ordered_dict.popitem(last=True)  # 弹出末尾元素
my_ordered_dict.popitem(last=False)  # 弹出首元素
```

#### 5）与dict的区别

尽管Python 3.7及更高版本中的普通字典已经是有序的，`OrderedDict`在功能上还是有一些区别：

- `OrderedDict`的等价性测试是考虑到元素的插入顺序的，而普通字典的等价性测试只考虑键值对是否相同。
- `OrderedDict`提供了一些额外的实用方法，如`move_to_end()`和`popitem(last=True|False)`。

`OrderedDict`提供了一个按照插入顺序排列元素的字典类型。尽管在最新的Python版本中普通字典也保持了元素的插入顺序，但`OrderedDict`在保持顺序的同时，还提供了一些特殊的方法，使得它在某些特定场景下仍然非常有用。

## 15、默认字典（defaultdict） 

`defaultdict`是Python中`collections`模块的一个子类，它提供了所有字典的方法，但是它接受一个工厂函数作为参数，用来为字典提供默认值。这意味着当你尝试访问一个不存在的键时，`defaultdict`会自动为这个键生成一个值，这个值是通过工厂函数产生的。这使得`defaultdict`在处理嵌套数据结构时非常有用，因为它免去了检查键是否存在的必要。

### （1）定义

要使用`defaultdict`，首先需要从`collections`模块导入它：

```python
from collections import defaultdict
```

在创建`defaultdict`对象时，你需要提供一个工厂函数，这个函数在需要时会被调用来为字典提供默认值。常见的工厂函数包括`list`、`int`、`set`等。

```python
# 创建一个默认值为list的defaultdict
dd_list = defaultdict(list)

# 创建一个默认值为int的defaultdict
dd_int = defaultdict(int)

# 创建一个默认值为set的defaultdict
dd_set = defaultdict(set)
```

### （2）常用操作

#### 1）添加元素

向`defaultdict`添加元素和普通字典一样简单。如果添加的是一个新键，`defaultdict`会自动使用工厂函数为其生成默认值。

```python
# 向dd_list中添加元素
dd_list['a'].append(1)
dd_list['a'].append(2)

# 向dd_int中添加元素
dd_int['key'] += 1

# 向dd_set中添加元素
dd_set['item'].add('value')
```

#### 2）访问不存在的键

当访问`defaultdict`中不存在的键时，它会自动使用工厂函数创建一个默认值，而不是抛出`KeyError`。

```python
print(dd_list['b'])  # 输出：[]
print(dd_int['another_key'])  # 输出：0
print(dd_set['another_item'])  # 输出：set()
```

#### 3）使用自定义工厂函数

你还可以定义自己的工厂函数来生成默认值。

```python
def default_value():
    return 'custom default'

dd_custom = defaultdict(default_value)
print(dd_custom['key'])  # 输出：custom default
```

`defaultdict`是一个非常实用的容器类型，它通过为字典提供默认值来简化了许多常见的编程任务，特别是在处理复杂或嵌套的数据结构时。使用`defaultdict`可以减少检查键是否存在的代码，使得数据处理更加简洁高效。

## 16、用户字典（UserDict）

`UserDict`是Python标准库中`collections`模块的一部分，它提供了一个字典对象的包装器。`UserDict`本身表现得像一个标准的字典，但它设计的目的是为了让开发者更容易地通过继承`UserDict`来创建自定义的字典类型。相对于直接继承内置的`dict`类型，使用`UserDict`作为基类可以避免某些陷阱，比如方法调用的递归，这使得添加自定义行为变得更加简单。

### （1）定义

要使用`UserDict`，首先需要从`collections`模块导入它：

```python
from collections import UserDict
```

然后，你可以通过继承`UserDict`来创建自定义的字典类：

```python
class MyDict(UserDict):
    # 添加自定义行为
    def __setitem__(self, key, value):
        # 只允许字符串作为键
        if not isinstance(key, str):
            raise TypeError("Keys must be strings")
        super().__setitem__(key, value)
```

### （2）使用自定义UserDict

一旦定义了自定义的字典类型，就可以像使用普通字典一样使用它，但它会包含你添加的自定义行为：

```python
my_dict = MyDict()
my_dict['key'] = 'value'  # 正常工作
try:
    my_dict[123] = 'value'  # 将引发TypeError
except TypeError as e:
    print(e)  # 输出：Keys must be strings
```

### （3）UserDict的特点

- **易于扩展**：`UserDict`使得添加自定义行为或修改现有行为变得简单。你可以覆盖或添加方法来扩展或修改字典的功能。
- **避免常见陷阱**：继承`UserDict`而不是`dict`可以避免一些常见的错误，如方法的递归调用等。因为`UserDict`内部实际上使用了一个标准字典来存储数据，这使得修改行为更加安全和直接。
- **更好的兼容性**：在某些情况下，直接继承和修改`dict`可能会导致与Python标准库中其他部分的兼容性问题。使用`UserDict`可以减少这种风险。

`UserDict`是一个非常有用的工具，特别适合于那些需要创建具有自定义行为的字典类型的场景。它通过提供一个标准字典的封装和易于扩展的接口，让自定义字典的创建变得更加简单和安全。

## 17、用户列表（UserLict）

`UserList`是Python中`collections`模块提供的一个类，它封装了列表对象，使得开发者可以通过继承`UserList`来创建自定义的列表类型。与`UserDict`相似，`UserList`的设计目的是为了让开发者更容易地扩展或修改列表的行为，而不是直接继承内置的`list`类型。这样做可以避免一些继承直接列表可能遇到的问题，比如方法调用的递归等。

### （1）定义

要使用`UserList`，首先需要从`collections`模块导入它：

```python
from collections import UserList
```

然后，可以通过继承`UserList`来定义自定义的列表类：

```python
class MyList(UserList):
    # 添加自定义行为
    def append(self, item):
        # 自定义条件，例如，只允许整数
        if not isinstance(item, int):
            raise TypeError("Only integers are allowed")
        super().append(item)
```

### （2）使用自定义UserList

创建了自定义的列表类型之后，就可以像使用普通列表一样使用它，但它会具有你添加的自定义行为：

```python
my_list = MyList()
my_list.append(1)  # 正常工作
try:
    my_list.append('a')  # 将引发TypeError
except TypeError as e:
    print(e)  # 输出：Only integers are allowed
```

### （3）UserList的特点

- **易于扩展**：`UserList`使得扩展或修改列表的功能变得简单。你可以通过覆盖或添加方法来自定义列表的行为。
- **避免继承陷阱**：通过继承`UserList`而不是直接继承`list`，可以避免一些继承自内置类型时可能遇到的问题，如方法的递归调用等。
- **适用性广**：`UserList`适用于需要列表行为略有变化或增加的场景，尤其是当内置的列表类不满足需求时。

`UserList`提供了一种创建具有自定义行为列表类型的便捷方式。通过封装标准列表的行为，并允许通过继承来扩展或修改这些行为，`UserList`为Python开发者提供了更大的灵活性和控制力。无论是需要添加额外的检查、限制、通知机制，还是需要完全不同的列表操作逻辑，`UserList`都是一个值得考虑的选择。

## 18、用户字符串（UserString）

`UserString`是Python中`collections`模块的一部分，它提供了一个字符串对象的封装。与`UserDict`和`UserList`类似，`UserString`的目的是使得通过继承`UserString`来创建自定义的字符串类型变得更加简单。这对于那些需要自定义或扩展基本字符串行为的应用来说非常有用。

### （1）定义

要使用`UserString`，首先需要从`collections`模块导入它：

```python
from collections import UserString
```

接着，可以通过继承`UserString`来定义一个自定义的字符串类：

```python
class MyString(UserString):
    # 添加自定义行为，例如，在字符串前后添加括号
    def __add__(self, other):
        return MyString("(" + super().__add__(other) + ")")
```

### （2）使用自定义UserString

创建了自定义的字符串类型之后，就可以像使用普通字符串那样使用它，但它会包含你添加的自定义行为：

```python
s1 = MyString("Hello")
s2 = MyString("World")
print(s1 + s2)  # 输出：(HelloWorld)
```

### （3）UserString的特点

- **易于扩展**：`UserString`使得为字符串添加自定义行为变得简单。你可以覆盖或添加方法来自定义字符串的行为。
- **避免继承陷阱**：通过继承`UserString`而不是直接操作字符串，可以避免一些继承自内置类型时可能遇到的问题，例如，方法的递归调用。
- **实用性**：`UserString`特别适用于需要修改字符串行为或添加额外功能的场景。例如，可以创建一个自动去除空格的字符串类，或者一个支持模板替换的字符串类。

`UserString`为开发者提供了一个简单而强大的工具，用于创建具有自定义行为的字符串类型。它的设计允许开发者轻松扩展或修改字符串的功能，而不必直接继承和修改Python的基本字符串类型。这样不仅提高了代码的可维护性，还可以避免潜在的继承问题，使得开发自定义字符串处理逻辑变得更加直接和安全。