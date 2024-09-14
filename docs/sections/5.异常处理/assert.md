## 5、断言

在Python中，`assert`语句用于断言某个条件是真的，如果条件是假的，那么会引发一个`AssertionError`异常。`assert`语句是一种在开发阶段检测错误的便捷方式，它可以在代码中确保程序的某个条件一定为真，如果不为真则快速失败。

### （1）基本用法

```python
assert condition, message
```

- `condition`：这是要测试的条件表达式，结果应该为`True`或`False`。
- `message`：如果条件表达式的结果是`False`，则显示的错误信息。

### （2）示例：

```python
def divide(x, y):
    assert y != 0, "除数不能为0"
    return x / y

try:
    result = divide(10, 0)
except AssertionError as e:
    print(e)
```

在这个示例中，如果`y`为0，`assert`语句将引发一个`AssertionError`，并打印出"除数不能为0"。

### （3）在异常处理中使用`assert`

`assert`语句通常用于确保程序中的关键条件得到满足，它是一种调试辅助工具。在异常处理的上下文中，`assert`可以用来捕获逻辑错误，然而请注意，`assert`语句可以通过解释器参数被全局禁用（使用`-O`选项），因此它不应该用于执行程序关键的功能性检查。

### （4）示例：结合异常处理和断言

```python
try:
    assert 2 + 2 == 4, "数学照样工作"
    assert 1 + 1 == 3, "这里有个问题"
except AssertionError as e:
    print(f"断言错误：{e}")
```

这个示例中的第一个`assert`语句不会失败，因为2 + 2确实等于4。第二个`assert`会失败，因为1 + 1显然不等于3，这将会捕获`AssertionError`并打印错误信息。