def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract the second number from the first and return the result."""
    return a - b


def main():
    num1 = 10

    num2 = 5


    # 调用 add 函数并打印结果
    sum_result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}")

    # 调用 subtract 函数并打印结果
    difference_result = subtract(num1, num2)
    print(f"The difference between {num1} and {num2} is {difference_result}")


if __name__ == '__main__':
    main()
