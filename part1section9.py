
# 129. What is a Module?

"""
def func():
    a = 10
    return a


print(func)
print(func())
print(id(func))
print(globals())


f = globals()['func']
print(f is func)
print(f())
print(globals()['func']())


print(locals())
print(locals() is globals())

a = 100
print(globals())


def func():
    a = 10
    b = 10
    print(locals())


func()



import math

print(math)


import fractions

print(fractions)


junk = math

print(junk.sqrt(2))
print(junk is math)

print(globals())
print(globals()['math'])
mod_math = globals()['math']
print(mod_math.sqrt(2))

print(type(globals()))

print(type(math))
print(type(fractions))

print(id(math))

import math
print(id(math))

import sys

# print(sys.modules)

print(type(sys.modules))
print(sys.modules['math'])
print(id(sys.modules['math']))

print(math.__name__)
print(math.__dict__)

f = math.__dict__['sqrt']

print(f)
print(f(2))


import fractions

print(sys.modules['fractions'])
print(dir(fractions))

# print(fractions.__dict__)


import calendar

print(calendar)


import types

print(isinstance(fractions, types.ModuleType))
print(isinstance(math, types.ModuleType))

mod = types.ModuleType('test', 'This is a test module.')


from types import ModuleType

print(isinstance(mod, ModuleType))

print(mod.__dict__)

mod.pi = 3.14
print(mod.__dict__)

mod.hello = lambda: 'Hello!'
print(mod.hello())

hello = mod.hello
print('hello' in globals())
print('mod' in globals())
print(hello())

from collections import namedtuple


mod.Point = namedtuple('Point', 'x y')
p1 = mod.Point(0, 0)
p2 = mod.Point(1, 1)
print(dir(mod))


PT = getattr(mod, 'Point')
print(PT(20, 20))

PT = mod.__dict__['Point']
print(PT(20, 20))

"""


# 130. How does Python Import Modules?
"""

import sys

sys.modules['test'] = lambda: 'Testing module caching'

import test

print(test)
print(test())

"""

# 131. Imports and importlib


import sys

print(sys)


import collections

print(collections)

mod_name = 'math'

import importlib
print(importlib)


m = importlib.import_module('math')
print(m)
print('math' in sys.modules)
print('fractions' in sys.modules)

try:
    print(math.sqrt(2))
except NameError:
    pass

print('math' in globals())


# import math as math2
# math2 = sys.modules['math']
math2 = importlib.import_module(mod_name)
print('math2' in globals())
print(id(math2))
print(id(sys.modules['math']))

print(math2.sqrt(2))

print(math2)

print(importlib)

fractions = importlib.import_module('fractions')
print(fractions)

print(fractions.__spec__)
print(sys.meta_path)

import math


print(math.__spec__)

# import module1


with open('module1.py', 'w') as code_file:
    code_file.write("print('running modul1.py...')\n")
    code_file.write('a=100\n')




