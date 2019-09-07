
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
"""

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
"""


# 133. Import Variants and Misconceptions - Coding
"""

import sys

for key in sorted(sys.modules.keys()):
    print(key)


print('cmath' in sys.modules)
print('cmath' in globals())

from cmath import exp

print('cmath' in globals())
print('exp' in globals())


print(exp)

print(id(exp))


print('cmath' in sys.modules)


print(exp(2+2j))


cmath = sys.modules['cmath']
print('cmath' in globals())
print(cmath.exp(2+2j))
print(cmath.sin(2+2j))
print(cmath.pi)
print(cmath.cos(2+2j))


from cmath import *

print(globals())

print(sin(2+2j))

from math import *

print(globals())



try:
    print(sin(2+2j))
except TypeError:
    pass

from cmath import sin

print(sin)

from math import sin

print(sin)


from cmath import sin as c_sin

print(c_sin)

from math import sin as r_sin

print(r_sin)


### Efficiency

def my_func(a):
    import math
    return math.sqrt(a)


from time import perf_counter
from collections import namedtuple


Timings = namedtuple('Timings', 'timing_1m timing_2 abs_diff rel_diff_perc')


def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1) / timing1 * 100

    timings = Timings(round(timing1, 1),
                      round(timing2, 1),
                      round(timing2 - timing1, 1),
                      round(rel_diff, 2))
    return timings


print(compare_timings(1, 2))


test_repeats = 10_000_000


### Timing using fully qualified module.symbol

#
import math

start = perf_counter()

for _ in range(test_repeats):
    math.sqrt(2)

end = perf_counter()
elapsed_fully_qualified = end - start
print(f'Elapsed: {elapsed_fully_qualified}')


#### Timing using a directly import symbol name


from math import sqrt

start = perf_counter()

for _ in range(test_repeats):
    sqrt(2)

end = perf_counter()
elapsed_direct_symbol = end - start
print(f'Elapsed: {elapsed_direct_symbol}')


print(compare_timings(elapsed_fully_qualified, elapsed_direct_symbol))


#### Timing using a function wrapper (fully qualified symbol)

import math


def func():
    math.sqrt(2)


start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()
elapsed_func_qualified = end - start
print(f'Elapsed: {elapsed_func_qualified}')


#### Timing using a function wrapper  import sqrt

from math import sqrt


def func():
    sqrt(2)


start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()
elapsed_func_direct_symbol = end - start
print(f'Elapsed: {elapsed_func_direct_symbol}')


print(compare_timings(elapsed_func_qualified, elapsed_func_direct_symbol))


### Nested imports


def func():
    import math
    math.sqrt(2)


start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()
elapsed_nested_fully_qualified = end - start
print(f'Elapsed: {elapsed_nested_fully_qualified}')


compare_timings(elapsed_func_qualified, elapsed_nested_fully_qualified)


def func():
    from math import sqrt
    sqrt(2)


start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_direct_symbol = end - start
print(f'Elapsed: {elapsed_nested_direct_symbol}')


compare_timings(elapsed_nested_fully_qualified, elapsed_nested_direct_symbol)


def a():
    import math
    math.sqrt(25)


def b():
    from math import sqrt
    sqrt(25)


from time import perf_counter

iterations = 100_00000
start = perf_counter()

for i in range(iterations):
    a()

end = perf_counter()
elapsed = end - start

print(elapsed)

from time import perf_counter

iterations = 100_00000
start = perf_counter()

for i in range(iterations):
    b()

end = perf_counter()
elapsed = end - start

print(elapsed)

"""


# 134. Reloading Modules
"""

import os


def create_module_file(module_name, **kwargs):
    '''Create a module file named <module_name>.py
    Module has a single function (print_vlaues) that will print
    out the suppliked (stringified) kwargs.
    '''

    module_file_name = f'{module_name}.py'
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}.py\n\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', '{str(value)}')\n")


create_module_file('test', k1=10, k2='python')

import test

print(test)
print(test.print_values())


create_module_file('test', k1=10, k2='python', k3='cheese')


import test
print(test.print_values())
print(id(test))

import sys

print('test' in sys.modules)
del sys.modules['test']
print('test' in sys.modules)

import test
print(id(sys.modules['test']))
print(test.print_values())
print('test' in globals())
print(id(test))
print(test.print_values())


print(id(test), id(sys.modules['test']))


create_module_file('test', k1=10, k2='python', k3='cheese', k4='parrots')

import importlib

importlib.reload(test)

print(id(test))
print(id(sys.modules['test']))
print(test.print_values())


create_module_file('test2', k1='python')

from test2 import print_values

print('test2' in globals())
print('test2' in sys.modules)
print(print_values)
print_values()

create_module_file('test2', k1='python', k2='cheese')
importlib.reload(sys.modules['test2'])
print_values()

print_values = sys.modules['test2'].print_values
print_values()
"""







