#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

# 定义一个命名元组类型，名称为'Person'，字段有'name'和'age'
Person = namedtuple("Person", ["name", "age"])

alice = Person(name="Alice", age=30)

print(alice)  # 'Alice'
print(alice.name)  # 'Alice'
print(alice.age)  # 30

print(alice[0])  # 'Alice'
print(alice[1])  # 30


bob = alice._replace(name="Bob")
print(bob)  # Person(name='Bob', age=30)
