# PS D:\Python3\Basics> python
# Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 12 +12
# 24
# >>> 2.5*5
# 12.5
# >>> 2**3
# 8
# >>> 2*100
# 200
# >>> 2**100
# 1267650600228229401496703205376
# >>> import math
# >>> math.pi
# 3.141592653589793
# >>> import random
# >>> random.random()
# 0.7970277686411839
# >>> random.choice([1,2,3,4,5])
# 2
# >>> random.choice([1,2,3,4,5])      
# 1
# >>> random.choice([1,2,3,4,5])
# 1
# >>> random.choice([1,2,3,4,5])
# 3
# >>> random.choice([1,2,3,4,5])
# 2
# >>> username="kirankumarg" 
# >>> len(username)
# 11
# >>> username[0]='A'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# >>> username[0]]
#   File "<stdin>", line 1
#     username[0]]
#                ^
# SyntaxError: unmatched ']'
# >>> username[0] 
# 'k'
# >>> username[1]
# 'i'
# >>> for c in username
#   File "<stdin>", line 1
#     for c in username
#                      ^
# SyntaxError: expected ':'
# >>> username[-1]
# 'g'
# >>> dir(username)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# >>> mylist=[123,'chai',3.14]
# >>> mylist
# [123, 'chai', 3.14]
# >>> myDictionary={'one':'kiran','two':'bharath'}
# >>> myDictionary
# {'one': 'kiran', 'two': 'bharath'}
# >>> myDictionary['two']
# 'bharath'
# >>> myDictionary['onet']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'onet'
# >>> mytupples=(1,2,3) 
# >>> len(mytupples)     
# 3
# >>> mytupples[0]  
# 1