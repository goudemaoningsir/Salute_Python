# !/usr/bin/env python
# -*- coding:utf-8 -*-　

### [encode]
s = "你好，世界！"
b = s.encode("utf-8")
print(b)
# b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'
### [encode]

### [decode]
b = b"\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81"
s = b.decode("utf-8")
print(s)
# 你好，世界！
### [decode]


### [zijiema]
import dis

def hello_world():
    print("Hello, World!")

dis.dis(hello_world)
### [zijiema]