# !/usr/bin/env python
# -*- coding:utf-8 -*-


def decorator_one(func):
    def wrapper():
        print("Decorator one")
        func()

    return wrapper


def decorator_two(func):
    def wrapper():
        print("Decorator two")
        func()

    return wrapper


@decorator_one
@decorator_two
def say_hello():
    print("Hello!")


say_hello()


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(times=3)
def say_hello():
    print("Hello!")


say_hello()
