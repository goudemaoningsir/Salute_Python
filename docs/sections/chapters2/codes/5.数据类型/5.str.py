# !/usr/bin/env python
# -*- coding:utf-8 -*-

### [lc]
# 连接
hello = "Hello, "
world = "World!"
greeting = hello + world
print(greeting)  # "Hello, World!"

# 重复
laugh = "ha"
lots_of_laugh = laugh * 3
print(lots_of_laugh)  # "hahaha"
### [lc]

### [qp]
text = "Hello, World!"
first_char = text[0]
print(first_char)  # 'H'
slice_text = text[7:12]
print(slice_text)  # 'World'
### [qp]

### [ct]
quote = "To be or not to be"
position = quote.find("not")
print(position)  # 9
replaced_quote = quote.replace("be", "see")
print(replaced_quote)  # "To see or not to see"
### [ct]

### [fh]
sentence = "Hello, my name is Alice"
words = sentence.split(" ")
print(words)  # ['Hello,', 'my', 'name', 'is', 'Alice']
rejoined = " ".join(words)
print(rejoined)  # "Hello, my name is Alice"
### [fh]

### [dx]
greeting = "hello, World"
upper_greeting = greeting.upper()
print(upper_greeting)  # "HELLO, WORLD"
lower_greeting = greeting.lower()
print(lower_greeting)  # "hello, world"
capitalized_greeting = greeting.capitalize()
print(capitalized_greeting)  # "Hello, world"
### [dx]

### [qc]
text = "  Hello, World!  "
clean_text = text.strip()
print(clean_text)  # "Hello, World!"
### [qc]

### [gs]name = "Alice"
age = 30
greeting = "My name is {0} and I am {1} years old.".format(name, age)
f_string_greeting = f"My name is {name} and I am {age} years old."
### [gs]
