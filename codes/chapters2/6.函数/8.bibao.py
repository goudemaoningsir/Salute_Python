# !/usr/bin/env python
# -*- coding:utf-8 -*-
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


def make_secure(access_level):
    def decorator(func):
        def wrapper(user):
            if user["access_level"] == access_level:
                return func(user)
            return "Access denied."

        return wrapper

    return decorator


@make_secure("admin")
def get_admin_password(user):
    return "admin: 1234"


user = {"username": "joe", "access_level": "admin"}
print(get_admin_password(user))  # "admin: 1234"
