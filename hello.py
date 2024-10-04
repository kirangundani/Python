print("HI")

def chai(n):
  print(n)

chai(5)

chai_one="masla chai"
chai_two="normal chai"
chai_three="desi chai"




# PS D:\Python3\Basics> ls


#     Directory: D:\Python3\Basics


# Mode                 LastWriteTime         Length Name
# ----                 -------------         ------ ----
# d-----        04-10-2024     19:04                __pycache__
# -a----        04-10-2024     19:02             45 chai.py
# -a----        04-10-2024     19:04             50 hello.py
# -a----        04-10-2024     19:04             11 tempCodeRunnerFile.py


# PS D:\Python3\Basics> python
# Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print("hii")
# hii
# >>> import os
# >>> os.getcwd()
# 'D:\\Python3\\Basics'
# >>> for c in "chai"
#   File "<stdin>", line 1
#     for c in "chai"
#                    ^
# SyntaxError: expected ':'
# >>> for c in "chai":
# ...   
# ...
#   File "<stdin>", line 3

#     ^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> for c in "chai":
# ...   print(c) 
# ...
# c
# h
# a
# i
# >>> import sys  
# >>> sys.platform
# 'win32'
# ...
# c
# h
# a
# i
# >>> import sys
# >>> sys.platform
# 'win32'
# a
# i
# >>> import sys
# >>> sys.platform
# 'win32'
# >>> import sys
# >>> sys.platform
# 'win32'
# 'win32'
# >>> import chai
# HI
# 5
# abdul kalam
# >>> import hello
# >>> hello.chai("Ramram")
# Ramram
# >>> from importlib import reload
# >>> reload(hello)
# HI
# 5
# <module 'hello' from 'D:\\Python3\\Basics\\hello.py'>
# >>> hello.chai_one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'hello' has no attribute 'chai_one'
# >>> chai.chai_one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'chai' has no attribute 'chai_one'
# >>> from importlib import reload
# >>> reload(hello)
# HI
# 5
# <module 'hello' from 'D:\\Python3\\Basics\\hello.py'>
# >>> hello.chai_one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'hello' has no attribute 'chai_one'
# >>> chai.chai_one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'chai' has no attribute 'chai_one'
# >>> from importlib from reload
#   File "<stdin>", line 1
#     from importlib from reload
#                    ^^^^
# SyntaxError: invalid syntax
# >>> from importlib import reload
# >>> reload(hello)
# HI
# 5
# <module 'hello' from 'D:\\Python3\\Basics\\hello.py'>
# >>> hello.chai_one
# 'masla chai'
# >>> hello.chai_two
# 'normal chai'
# >>> hello.chai_three
# 'desi chai'


# MUTABLE AND IMMUTABLE IN PYTHON (GOOGLE IT)