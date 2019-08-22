#
# l = [1, 2, 3]
# val = 10
# idx = 0
#
# while idx < len(l):
#     if l[idx] == val:
#         break
#     idx += 1
# else:
#     l.append(val)
#
# print(l)

# a = 10
# b = 0
#
# try:
#     a / b
# except ZeroDivisionError:
#     print('division by 0')
# finally:
#     print('this always executes')


# a = 0
# b = 10
#
#
# while a < 4:
#     print('------------------------')
#     a += 1
#     b -= 1
#
#     try:
#         a / b
#     except ZeroDivisionError:
#         print("{0}, {1} - division by 0".format(a, b))
#         break
#     finally:
#         print("{0}, {1} - always executes".format(a, b))
#
#     print("{0}, {1} - main loop".format(a, b))
#
# else:
#     print('Code executed without a zero division error')



## Garbage Collection
"""

import ctypes
import gc


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return 'Object exists'
    return 'Not Found'


class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))


gc.disable()


my_var = A()

# print(hex(id(my_var)))
#
#
# print(hex(id(my_var.b)))
# print(hex(id(my_var.b.a)))

a_id = id(my_var)
b_id = id(my_var.b)

print(hex(a_id))
print(hex(b_id))

print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))
my_var = None
print(my_var)
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))

gc.collect()

print(object_by_id(a_id))
print(object_by_id(b_id))
print(ref_count(a_id))
print(ref_count(a_id))
print(ref_count(a_id))
print(ref_count(b_id))


# import ctypes
a = "python"
id_a = id(a)
print(id(a), a)
retrieved = ctypes.cast(id_a, ctypes.py_object).value
print(id(retrieved), retrieved, type(retrieved))
"""
from functools import partial

"""
a = [1, 2]
b = [3, 4]
t = (a, b)
print("Address t: {}, value t: {}".format(hex(id(t)), t))
print("Address a: {}, value a: {}".format(hex(id(a)), a))
print("Address b: {}, value b: {}".format(hex(id(b)), b))

a.append(3)
b.append(5)
print("After appending the lists: ")
print("Address t: {}, value t: {}".format(hex(id(t)), t))
print("Address a: {}, value a: {}".format(hex(id(a)), a))
print("Address b: {}, value b: {}".format(hex(id(b)), b))

#  If i use shortened version "+=" address stays the same!
a += [4]
print("I always thought a=a+b is same as a+=b:")
print("Address t: {}, value t: {}".format(hex(id(t)), t))
print("Address a: {}, value a: {}".format(hex(id(a)), a))

#  Address changes if use concatenate on mutable object
a = a + [5]
print("After concat of a list: ")
print("Address t: {}, value t: {}".format(hex(id(t)), t))
print("Address a: {}, value a: {}".format(hex(id(a)), a))

"""

"""
# function arguments and mutability


def process(s):
    print('Initial s # = {0}'.format(id(s)))
    s = s + ' world'
    print('Initial s # = {0}'.format(id(s)))


my_var = 'hello'
print('my_var # = {0}'.format(id(my_var)))

process(my_var)

print(id(my_var))
print(my_var)
print('#################################')


def modify_list(lst):
    print('Initial lst # = {0}'.format(id(lst)))
    lst.append(100)
    print('Initial lst # = {0}'.format(id(lst)))


my_list = [1, 2, 3]
print(id(my_list))
modify_list(my_list)
print(id(my_list))
print(my_list)


print('#################################')


def modify_tuple(t):
    print('Initial t # = {0}'.format(id(t)))
    t[0].append(100)
    print('Initial t # = {0}'.format(id(t)))


my_tuple = ([1, 2], 'a')
print(id(my_tuple))
modify_tuple(my_tuple)
print(my_tuple)

print('#################################')
t1 = (1, 6, 5)
t2 = (1, 6, 5)
print(t1 is t2)

print('#################################')
a = 100
b = 100
c = a - 1
new_b = c + 1
print('a', id(a), a)
print('b', id(b), b)
print('new_b', id(new_b), new_b)
print('-----------------------')
a = 1000000000000000000
b = 1000000000000000000
c = a - 1
new_b = c + 1
print('a', id(a), a)
print('b', id(b), b)
print('new_b', id(new_b), new_b)

print('#################################')

from timeit import timeit
print(timeit('list(range(0,256))', globals=globals(), number=5_000_000))
print(timeit('list(range(258,514))', globals=globals(), number=5_000_000))
"""

# 26. python optimizations: string interning
"""
import sys
import time


def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass


start = time.perf_counter()
compare_using_equals(10_000_000)
end = time.perf_counter()
print('equality', end - start)

start = time.perf_counter()
compare_using_interning(10_000_000)
end = time.perf_counter()
print('equality', end - start)
"""


# 27. python optimizations: peephole

"""
def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3


print(my_func.__code__.co_consts)


def my_func(e):
    if e in [1, 2, 3]:
        pass


print(my_func.__code__.co_consts)


def my_func(e):
    if e in {1, 2, 3}:
        pass


print(my_func.__code__.co_consts)

import string
import time

print(string.ascii_letters)

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

print(char_list)
print(char_tuple)
print(char_set)


def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass


start = time.perf_counter()
membership_test(10_000_000, char_list)
end = time.perf_counter()
print('list', end - start)


start = time.perf_counter()
membership_test(10_000_000, char_tuple)
end = time.perf_counter()
print('tuple', end - start)

start = time.perf_counter()
membership_test(10_000_000, char_set)
end = time.perf_counter()
print('set', end - start)
"""

# 62. Positional and Keyword Arguments

"""

def my_func(a, b, c):
    print('a={0}, b={1}, c={2}'.format(a, b, c))


my_func(1, 2, 3)

# my_func(1, 2)


def my_func(a=1, b=2, c=3):
    print('a={0}, b={1}, c={2}'.format(a, b, c))


my_func(10, 20, 30)
my_func(10, 20)
my_func(10)
my_func()


def my_func(a, b=2, c=3):
    print('a={0}, b={1}, c={2}'.format(a, b, c))


my_func(c=30, b=20, a=10)
my_func(10, c=30, b=20)
my_func(10, c=30)
"""

# 65. Unpacking Iterables - Coding

"""

v = [x, y] = (1, 2)
# https://docs.python.org/3.6/reference/simple_stmts.html#assignment-statements
# "An assignment statement evaluates the expression list (remember that this can be a single expression or
# a comma-separated list, the latter yielding a tuple) and assigns the single resulting object to each of the
# target lists, from left to right."
# [x,y] = (1, 2)
# v = (1, 2)

print(type(v))
print(v)

a = (1, 2, 3)
print(type(a))
a = 1, 2, 3
print(type(a))
print(a)

a = (1)
print(type(a))

a = ('a')
print(type(a))

a = (1,)
print(type(a))

a = 100,
print(type(a))
print(a)

a = ()
print(type(a))

# dont work
#a = ,
# a(,)


a, b, c = [1, 'a', 3.14]
print(a, b, c)
(a, b, c) = [1, 2, 3]
print(a, b, c)

a, b = (1, 2)
print(a, b)

a, b = 10, 20
print(a, b)
a, b, c = 10, 20, 30
print(a, b, c)

a, b, c = 10, 'a', 3.14
print(a, b, c)
a, b, c = 10, {1, 2}, ['a', 'b']
print(a, b, c)

a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)


for e in 'XYZ':
    print(e)

a, b, c = 'XYZ'
print(a, b, c)

s = 'XYZ'
print(s[0], s[1])
s = {1, 2, 3}

try:
    print(s[0])
except TypeError:
    pass

s = {'p', 'y', 't', 'h', 'o', 'n'}
print(s)

for e in s:
    print(e)

a, b, c, d, e, f = s
print(a, b, c, d, e, f)

d = {'a': 1, 'b': 2, 'c': 3}
for e in d:
    print(e)

a, b, c = d
print(a, b, c, d)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a, b, c, d = d
print(a, b, c, d)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d, a, b, c = d
print(d, a, b, c)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for e in d:
    print(e)

for e in d.values():
    print(e)

a, b, c, d = d.values()
print(a, b, c, d)


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for a, b in dict1.items():
    print('key={0}, value={1}'.format(a, b))
"""


# 67. Extended Unpacking - Coding
"""

l = [1, 2, 3, 4, 5, 6]
a = l[0]
b = l[1:]
print(a)
print(b)

a, b = l[0], l[1:]
print(a)
print(b)

a, *b = l
print(a, b)

try:
    s = {1, 2, 3}
    a = s[0]
    b = s[1:]
except TypeError:
    pass


s = 'python'
a, *b = s
print(a, b)

t = ('a', 'b', 'c')
a, *b = t
print(a, b)

[a, b, c] = 'XYZ'
print(a, b, c)
a, b, *c = 'python'
print(a, b, c)

s = 'python'
a, b, *c, d = s
print(a, b, d, c)

a, b, c, d = s[0], s[1], s[2:-1], s[-1]
*c, = c
print(a, b, c, d)
print(a, b, str(c), d)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]

print(l)

l1 = [1, 2, 3]
s1 = 'abc'
print([*l1, *s1])


l1 = [1, 2, 3]
s1 = {'x', 'y', 'z'}
print([*l1, *s1])

s1 = 'abc'
s2 = 'cde'
print([*s1, *s2])
print({*s1, *s2})

s = {10, -99, 3, 'd'}
for c in s:
    print(c)

a, b, c, d = s
print(a, b, c, d)

a, b, *c = s
print(a, b, c)

print(list(s))
*c, = s
print(c)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
try:
    print(s1 + s2)
except TypeError:
    pass

c = {*s1, *s2}
print(c)

print(s1.union(s2))

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
print(s1.union(s2).union(s3).union(s4))
print(s.union(s2, s3, s4))
print({*s1, *s2, *s3, *s4})
print([*s1, *s2, *s3, *s4])


d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key4': 4}
print({*d1, *d2})
print({**d1, **d2})
print({**d2, **d1})


print({'a': 1, 'b': 2, **d1, 'c': 3})

a, b, e = [1, 2, 'XY']
print(a, b, e)
c, d = e
print(c, d)

a, b, (c, d) = [1, 2, 'XY']
print(a, b, c, d)

a, *b, (c, d, *e) = [1, 2, 3, 'python']
print(a, b, c, d, e)

l = [1, 2, 3, 4, 'python']
a, *b, (c, d, *e) = l
print(a, b, c, d, e)

print(l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:]))
a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)

l = (1, 2, 3, 4, ['a', 'b', 'c', 'd'])
a, *b, (c, d, *e) = l
print(a, b, c, d, e)
a, b, c, d, e = l[0], list(l[1:-1]), l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)
"""

# 69. *args - Coding
"""

a, b, *c = 10, 20, 'a', 'b'
print(a, b, c)


def func1(a, b, *c):
    print(a)
    print(b)
    print(c)


func1(10, 20)
func1(10, 20, 1, 2, 3)


def avg(*args):
    count = len(args)
    total = sum(args)
    return total/count


print(avg(10, 20))
print(avg(2, 2, 4, 4))


def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    return total/count


print(avg())
print(avg(2, 2, 4, 4))


def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count


print(avg())
print(avg(2, 2, 4, 4))
"""

# 71. Keyword Arguments - Lecture
"""

def func1(a, b, c):
    print(a, b, c)


func1(1, 2, 3)
func1(1, c=3, b=2)
func1(c=3, b=2, a=1)


def func1(a, b, *args):
    print(a, b, args)


func1(1, 2, 3, 4)


def func1(a, b, *args, d):
    print(a, b, args, d)

try:
    func1(1, 2, 3, 4, 5)
except TypeError:
    func1(1, 2, 3, 4, d=5)


def func1(*args, d):
    print(args, d)


func1(1, 2, 3, d='a')
func1(d='a')


def func(*, d):
    print(d)


func(d=100)
try:
    func(1, 2, 3, d=100)
except TypeError:
    func(d=100)


def func(a, b, *, d):
    print(a, b, d)


try:
    func(1, 2, 3, d=4)
except TypeError:
    func(1, 2, d=4)


def func(a, b=2, *args, d):
    print(a, b, args, d)


func(1, 5, 3, 4, d='a')
func(1, d='a')


def func(a, b=20, *args, d=0, e):
    print(a, b, args, d, e)

try:
    func(5, 4, 3, 2, 1)
except TypeError:
    func(5, 4, 3, 2, 1, e='all engines running')

func(0, 600, d='goood morning', e='python!')
func(11, 'm/s', 24, 'mph', d='unladen', e='swallow')

"""

# 72. **kwargs
"""

def func(**others):
    print(others)


func(a=1, b=2, c=3)


def func(*args, **kwargs):
    print(args)
    print(kwargs)


try:
    # func(1, 2, x=100, y=200, 12)
    x = 0
except Exception:
    func(1, 2, x=100, y=200)


def func(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)


func(1, 2, x=100, y=200, d=0)


def func(a, b, **kwargs):
    print(a)
    print(b)
    print(kwargs)


func(1, 2, x=100, y=200)
"""

# 74. Putting it all Together - coding
"""

def func(a, b, *args):
    print(a, b, args)


func(1, 2, 'x', 'y', 'z')
# func(a=1, b=2, 'x', 'y', 'z')  SyntaxError: positional argument follows keyword argument


def func(a, b=2, c=3, *args):
    print(a, b, c, args)

func(1, 4, 3, 'x', 'y', 'z')


func(1, c=5)


def func(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)


func(10, 20, 'x', 'y', 'z', c=4, d=1)
func(10, 20, 'x', 'y', 'z', d=10)

try:
    func(1, 'x', 'y', 'z', b=5, d=10)
except TypeError:
    func(1, 'x', 'y', 'z', d=10)


def func(a, b, *args, c=10, d=20, **kwargs):
    print(a, b, args, c, d, kwargs)


func(1, 2, 'x', 'y', 'z', c=100, d=200, x=0.1, y=0.2)


with open('log.txt', 'w') as fd:
    fprint = partial(print, file=fd)
    fprint(1, 2)
    fprint('python')
    a, b = 10, 3.14
    fprint(f'a: {a}, pi: {b}')
"""


# 75

"""
import time


def time_it(fn, *args, **kwargs):
    print(args, kwargs)


time_it(print, 1, 2, 3, sep=' - ', end=' ***')


def time_it(fn, *args, rep=1, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)


time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep


def time_it(fn, *args, rep=1, **kwargs):
    print(args, rep, kwargs)


print('-----------------------------------')
time_it(print, n=1, start=0, end=20000, rep=5)
print('-----------------------------------')

a = time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)
print(a)


def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results


print(compute_powers_1(2, end=5))


def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]


print(compute_powers_2(2, end=5))


def compute_powers_3(n, *, start=1, end):
    # using a list comprehension
    return (n**i for i in range(start, end))


print(list(compute_powers_3(2, end=5)))


print(time_it(compute_powers_1, 2, start=0, rep=5, end=20000))
print(time_it(compute_powers_2, n=2, start=0, rep=5, end=20000))
"""

# 77. Parameter Defaults - Beware Again!!
"""

def add_item(name, quantity, unit, grocery_list):
    grocery_list.append('{0} ({1} {2})'.format(name, quantity, unit))
    return grocery_list


store1 = []
store2 = []

add_item('banana', 2, 'units', store1)
add_item('milk', 1, 'liter', store1)

print(store1)
add_item('python', 1, 'medium-rare', store2)
print(store2)


def add_item(name, quantity, unit, grocery_list=[]):
    grocery_list.append('{0} ({1} {2})'.format(name, quantity, unit))
    return grocery_list

del store1
del store2

store1 = add_item('banana', 2, 'units')
add_item('milk', 1, 'liter')

print('---------------------')
print(store1)

store2 = add_item('python', 1, 'medium-rare')

print(store2)
print(store1)

print(store1 is store2)


def add_item(name, quantity, unit, grocery_list=None):
    if grocery_list is None:
        grocery_list = []
    grocery_list.append('{0} ({1} {2})'.format(name, quantity, unit))
    return grocery_list


store1 = add_item('banana', 2, 'units')
add_item('milk', 1, 'liter', store1)

print('------------ second test --------------')
print(store1)

store2 = add_item('python', 1, 'medium-rare')
print(store2)

print(store1 is store2)


def factorail(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorail(n-1)


print(factorail(3))
print(factorail(3))


def factorail(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorail(n-1, cache=cache)
        cache[n] = result
        return result


print('--------------- thierd -----------------')
cache = {}
print(factorail(3, cache=cache))
print(cache)

print(factorail(3, cache=cache))
print(cache)


print(factorail(4, cache=cache))
print(cache)


def factorail(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorail(n-1)
        cache[n] = result
        return result

print('--------------- fourh -----------------')
print(factorail(3))
print(factorail(4))
"""

# 80 Docstrings and Annotations - Coding


# def my_func(a, b=1):
#     # some comment here
#     # i = 10
#     """:returns a * b
#         some addional docs here
#
#         Inputs:
#
#         Outputs:
#     """
#     return a * b
#
#
# # help(my_func)
#
# print(my_func.__doc__)
#
#
# def my_func(a: 'annotation for a',
#             b: 'annotation for b' = 1) -> 'something with a long annotation':
#     """document for my_func"""
#     return a * b
#
#
# # print(help(my_func))
#
# print(my_func.__doc__)
# print(my_func.__annotations__)
#
#
# x = 3
# y = 5
#
#
# def my_func(a: 'some character', b = max(x, y)) -> 'character a repeated ' + str(max(x, y)) + ' times':
#     print(b)
#     return a * max(x, y)
#
#
# print(my_func('a'))
# print(my_func.__annotations__)
#
# x = 10
# print(my_func('a'))
# print(my_func.__annotations__)
#
#
# def my_func(a: str,
#             b: 'int > 0' = 1,
#             *args: 'some extra positional args',
#             k1: 'keyword-only arg 1',
#             k2: 'keyword-only arg 2' = 100,
#             **kwargs: 'some extra keyword-only args') -> 'something':
#     print(a, b, args, k1, k2, kwargs)
#
# # help(my_func)
#
#
# print(my_func.__annotations__)
#
# my_func(1, 2, 3, 4, 5, k1=10, k3=300, k4=400)


# 82. Lambda Expressions - Coding
"""

def sq(x):
    return x ** 2


print(type(sq))
print(sq)

l = lambda x: x ** 2
print(l)

l = lambda x, y: x+y
print(l)

f = sq

print(id(f), id(sq))

print(f(3))
print(sq(3))
print(f)

f = lambda x: x**2

print(f)
print(f(3))


g = lambda x, y=10: x+y
print(g)
print(g(1, 2))
print(g(1))


f = lambda x, *args, y, **kwargs: (x, *args, y, kwargs)
print(f(1, 'a', 'b', y=100, a=10, b=20))


def apply_func(x, fn):
    return fn(x)


print(apply_func(5, sq))
print(apply_func(5, lambda x: x ** 2))
print(apply_func(5, lambda x: x ** 3))


def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)


print(apply_func(sq, 3))
print(apply_func(lambda x: x ** 2, 3))
print(apply_func(lambda x, y: x + y, 1, 2))
print(apply_func(lambda x, *, y: x + y, 1, y=20))


print(apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5))
print(apply_func(sum, (1, 2, 3, 4, 5)))
print(sum((1, 2, 3, 4, 5)))
"""

# 83. Lambdas and Sorting
"""


l = [1, 5, 4, 10, 9, 6]
print(sorted(l))
print(l)

l = ['c', 'B', 'D', 'a']
print(sorted(l))

print(sorted(l, key=lambda s: s.upper()))


d = {'def': 300, 'abc': 200, 'ghi': 100}
print(d)

for e in d:
    print(e)

print(sorted(d))

print(sorted(d, key=lambda e: d[e]))


def dist_sq(x):
    return (x.real)**2 + (x.imag)**2


print(dist_sq(1+1j))

l = [3+3j, 1-1j, 0, 3+0j]

try:
    sorted(l)
except TypeError:
    pass

print(sorted(l, key=dist_sq))

print(sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2))

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']

print(sorted(l))
print(sorted(l, key=lambda s: s[-1]))

l = ['Idle', 'Cleese', 'Palin', 'Chapman', 'Gilliam', 'Jones']
print(sorted(l, key=lambda s: s[-1]))

"""

# 86 Function Introspection - Coding


# dummy code
# i = 100
#
#
# # TODO: Fix this function
# # currently does nothing, but should do ....\n
# def my_func(a: 'mandatory positional',
#             b: 'optional positional' = 1,
#             c=2,
#             *args: 'add extra positional here',
#             kw1,
#             kw2=100,
#             kw3=200,
#             **kwargs: 'provide extra kw-only here') -> 'does nothing':
#     """
#         This function does nothing but does have various parameters
#         and annotations.
#     """
#     i = 10
#     j = 20
#     a = i + j
#     return a
#
#
# print(my_func.__doc__)
# print(my_func.__annotations__)
#
# my_func.short_description = 'this is a function that does nothing much'
#
# print(dir(my_func))
# print(my_func.__name__)
#
# print(id(my_func))
#
#
# def func_call(f):
#     print(id(f))
#     print(f.__name__)
#
#
# func_call(my_func)
#
# print(my_func.__defaults__)
# print(my_func.__kwdefaults__)
#
# print(my_func.__code__)
# print(dir(my_func.__code__))
#
# print(my_func.__code__.co_name)
# print(my_func.__code__.co_varnames)
# print(my_func.__code__.co_argcount)
#
#
# import inspect
#
# from inspect import isfunction, ismethod, isroutine
#
# a = 10
#
# print(isfunction(a))
# print(isfunction(my_func))
# print(ismethod(my_func))
#
#
# class MyClass:
#     def f(self):
#         pass
#
#
# print(isfunction(MyClass.f))
#
# my_obj = MyClass()
#
# print(isfunction(my_obj.f))
# print(ismethod(my_obj.f))
# print(isroutine(my_obj.f))
# print(isroutine(MyClass.f))
#
#
# f = my_func
# print(inspect.getsource(f))
#
# print(inspect.getmodule(my_func))
# print(inspect.getmodule(print))
# import math
# print(inspect.getmodule(math.sin))
#
#
# print(inspect.getcomments(my_func))
#
#
# print(inspect.signature(my_func))
# print(dir(inspect.signature(my_func)))
#
# print(my_func.__annotations__)
# print(inspect.signature(my_func).return_annotation)
#
# sig = inspect.signature(my_func)
# print(type(sig))
# print(sig)
#
# print(sig.parameters)
#
#
# for param in sig.parameters.values():
#     # print('Key:', k)
#     print('Name: ', param.name)
#     print('Default:', param.default)
#     print('Annotation:', param.annotation)
#     print('Kind:', param.kind)
#     print('---------------------------')
    # print(dir(v))
    # print(k, type(v))


# 89. Map, Filter, Zip and List Comprehensions - Coding
"""

def fact(n):
    return 1 if n < 2 else n * fact(n-1)


print(fact(3))
print(fact(4))

results = map(fact, range(6))
print(results)


for x in results:
    print(x)

print('###  check again filter for map')

for x in results:
    print(x)


results = map(fact, range(6))
print(results)


l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = 100, 200, 300, 400  # tuple


results = list(map(lambda x, y, z: x+y+z, l1, l2, l3))
print(results)

results = map(lambda x, y: x+y, l1, l2, l3)
print(results)

try:
    for x in results:
        print(x)
except TypeError:
    pass


x = range(25)

print(x)

for i in x:
    print(i)


print(list(filter(lambda x: x % 3 == 0, range(25))))
print(list(filter(None, [1, 0, 4, 'a', '', None, True, False])))

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = 'python'
results = zip(l1, l2, l3)


for x in results:
    print(x)


print('###  check again filter for zip')

for x in results:
    print(x)


print(list(zip(range(10000), 'python')))

l = range(10)

print(list(l))

print(list(map(fact, l)))
print([fact(n) for n in range(10)])

results = (fact(n) for n in range(10))
print(results)

for x in results:
    print(x)

results = [fact(n) for n in range(10)]
print(results)


l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40]

print(list(map(lambda x, y: x+y, l1, l2)))
print([x+y for x, y in zip(l1, l2)])


print(list(filter(lambda x: x % 2 == 0, map(lambda x, y: x+y, l1, l2))))
print([x+y for x, y in zip(l1, l2) if (x+y) % 2 == 0])
"""

# 91. reducing functions - Lecture
"""

l = [5, 8, 6, 10, 9]


_max = lambda x, y: x if x > y else y


def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result


print(max_sequence(l))


_min = lambda a, b: a if a < b else b


def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result


print(min_sequence(l))


_add = lambda a, b: a + b


def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result


print(add_sequence(l))


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result


print(_reduce(_max, l))
print(_reduce(_min, l))
print(_reduce(_add, l))

try:
    print(_reduce(_max, {1, 3, 4, 5}))
except TypeError:
    pass

from  functools import reduce

print(reduce(_max, l))
print(reduce(_add, l))
print(reduce(_max, {1, 3, 4, 5}))

print(min(l))
print(min({1, 2, 3}))
print(max(l))
print(sum(l))
print(sum({1, 2, 3}))


s = {True, 1, 0, None}
print(all(s))

s2 = {True, 1, 's'}
print(all(s2))


print(bool(True) and bool(1) and bool('s'))
print(bool(True) and bool(1) and bool(0) and bool(None))

print(any(s))
print(any(s2))

s3 = {False, 0, '', None}
print(any(s3))


print(reduce(lambda a, b: bool(a) and bool(b), s))
print(reduce(lambda a, b: bool(a) or bool(b), s3))

l = [5, 8, 6, 10, 9]

print(reduce(lambda a, b: a * b, l))

l = [1, 2, 3, 4]

print(reduce(lambda a, b: a * b, l))

print(list(range(1, 5+1)))


print(reduce(lambda a, b: a * b, range(1, 5+1)))


def fact(n):
    return 1 if n < 2 else n * fact(n-1)


print(fact(5))


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n+1))


print(fact(2))


def _reduce(fn, sequence, initial):
    result = initial
    for x in sequence:
        result = fn(result, x)
    return result


print(_reduce(lambda a, b: a+b, l, 0))
print(_reduce(lambda a, b: a+b, l, 100))
print(_reduce(lambda a, b: a+b, {1, 2, 3, 4}, 0))
print(_reduce(lambda a, b: a+b, {1, 2, 3, 4}, 100))
print(reduce(lambda a, b: a+b, l, 0))
print(reduce(lambda a, b: a+b, l, 100))
"""

# 93. Partial Functions - Coding
"""

from functools import partial


def my_func(a, b, c):
    print(a, b, c)


my_func(10, 20, 30)


def f(x, y):
    return my_func(10, x, y)


f(20, 30)
f(100, 200)

f = lambda x, y: my_func(10, x, y)

f(100, 200)

f = partial(my_func, 10)

f(20, 30)


f = partial(my_func, 10, 20)

f(30)


def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)


my_func(10, 20, 100, 200, k1='a', k2='b', k3=1000, k4=2000)


def f(x, *vars, kw, **kwargs):
    return my_func(10, x, *vars, k1='a', k2=kw, **kwargs)


f(20, 100, 200, kw='b', k3=1000, k4=2000)
f = partial(my_func, 10, k1='a')

f(20, 100, 200, k2='b', k3=1000, k4=2000)


def pow(base, exponent):
    return base ** exponent

sq = partial(pow, 2)
print(sq(10))
sq = partial(pow, exponent=2)
print(sq(5))

cu = partial(pow, exponent=3)
print(cu(5))
print(cu(base=5))
print(cu(5, exponent=2))

a = 2
sq = partial(pow, exponent=a)
print(sq(5))
a = 3
print(sq(5))


def my_func(a, b):
    print(a, b)


a = [1, 2]
f = partial(my_func, a)

f(100)
a.append(3)
f(100)

origin = (0, 0)
l = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]

dist2 = lambda a, b: (a[0] -b[0])**2 + (a[1] - b[1])**2
print(dist2((1, 1), origin))
print(sorted(l))

f = partial(dist2, origin)
f((1, 1))
print(sorted(l, key=f))
f = lambda x: dist2(origin, x)
print(sorted(l, key=f))
print(sorted(l, key=partial(dist2, origin)))
print(sorted(l, key=lambda x: dist2(origin, x)))
"""

# 95. The operator Module - Coding
"""

import operator

print(operator)
print(operator.add(1, 2))
print(operator.mul(2, 3))
print(operator.truediv(3, 2))
print(operator.floordiv(13, 2))
print(13 // 2)

from functools import reduce

print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))
print(reduce(operator.mul, [1, 2, 3, 4]))

print(operator.lt(10, 3))

from operator import is_

print(is_('abc', 'def'))
print(is_('abc', 'abc'))
print(operator.truth([]))
print(operator.truth([1]))

my_list = [1, 2, 3, 4]
print(my_list[1])

print(operator.getitem(my_list, 1))

my_list[1] = 100
print(my_list)
del my_list[3]
print(my_list)

my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)
print(my_list)
operator.delitem(my_list, 3)
print(my_list)

f = operator.itemgetter(2)
print(f)
print(type(f))

my_list = [1, 2, 3, 4]
print(f(my_list))
s = 'python'
print(f(s))

f = operator.itemgetter(2, 3)
print(type(f))
my_list = [1, 2, 3, 4]
print(f(my_list))
print(f('python'))


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')


obj = MyClass()
print(obj)
print(obj.a, obj.b, obj.test)
obj.test()

prop_a = operator.attrgetter('a')
print(prop_a(obj))

my_var = 'b'
print(operator.attrgetter(my_var)(obj))

prob_b = operator.attrgetter(my_var)
print(prob_b(obj))
my_var = 'c'
print(prob_b(obj))


a, b, test = operator.attrgetter('a', 'b', 'test')(obj)
print(a, b, test)
test()

f = lambda x: x.a
print(f(obj))

f = lambda x: x[2]
x = [1, 2, 3, 4]
print(f(x))

f = lambda x: (x[2], x[3])
x = [1, 2, 3, 4]
print(f(x))

a = 5 + 10j
print(a)
print(a.real)
l = [5-10j, 3+3j, 2-100j]
print(sorted(l, key=lambda x: x.real))
print(sorted(l, key=operator.attrgetter('real')))

l = [(2, 3, 4), (1, 3, 5), (6,), (4, 100)]
print(sorted(l, key=lambda x: x[0]))
print(sorted(l, key=operator.itemgetter(0)))


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')


obj = MyClass()
f = operator.attrgetter('test')
print(f(obj))
f(obj)()
f = operator.methodcaller('test')
f(obj)


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def test(self, c, d, *, e):
        print(self.a, self.b, c, d, e)


obj = MyClass()
print(obj.a, obj.b)
obj.test(100, 200, e=300)
operator.methodcaller('test', 100, 200, e=300)(obj)
f = operator.attrgetter('test')
f(obj)(10, 20, e=100)
"""

# 98. Global and Local Scopes - Coding
"""

a = 10


def my_func(n):
    c = n ** 2
    return c


def my_func(n):
    print('global a:', a)
    c = a ** n
    return c


print(my_func(2))


def my_func(n):
    a = 20
    c = a ** n
    return c


print(a)
print(my_func(2))
print(a)


def my_func(n):
    global a
    a = 20
    c = a ** n
    return c


print(a)
print(my_func(2))
print(a)


def my_func():
    global var
    var = 'hello world'
    return


try:
    print(var)
except NameError:
    pass

my_func()
print(var)


a = 10


def my_func():
    global a
    a = 'hello'
    print('global a:', a)


my_func()
print(a)

a = 10


def my_func():
    print('global a:', a)
    a = 'hello world'
    print(a)


try:
    my_func()
except UnboundLocalError:
    pass


f = lambda n: print(a ** n)
f(2)
print(True)


def print(x):
    return 'hello {0}'.format(x)


print('world')

try:
    print('world', '!')
except TypeError:
    pass

del print


print('world')

for i in range(10):
    x = 2 * i


print(x)
print(i)
"""

# 100. Nonlocal Scopes - Coding
"""

def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()


outer_func()


def outer_func():
    x = 'hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()


outer_func()


def outer_func():
    x = 'hello'
    def inner():
        x = 'python'
        print('inner:', x)
    inner()
    print('outer:', x)

outer_func()


def outer_func():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
        print('inner:', x)
    print('outer(before): ', x)
    inner()
    print('outer(after):', x)


outer_func()


def outer():
    x = 'hello'
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)


outer()


def outer():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        inner2()
    i = inner1
    print('print inner1 func inside')
    print(i.__code__.co_freevars)
    print(i.__closure__)
    inner1()
    print(x)


k = outer
print(k.__code__.co_freevars)
print(k.__closure__)
k()

x = 5
print(x)

def dd():
    global dd_v
    dd_v = 'work'

dd()
print(dd_v)

# When you attempted to execute the code

# def outer():
#     global x
#     x = 'monty'
#     def inner():
#         nonlocal x
#         x = 'hello'
#     inner()
#     print(x)


# You got an error.  No functions were called, so this is a compile time error,
# Also, when using global you mentioned that if a given variable didn't exist in the global name space
# it would be created Seems when using nonlocal, there's no such creation of variables if they don't already
# exist in at least one of the enclosing local scopes.
"""


"""
def counter():
    count = 0
    print(hex(id(count)))

    def inc():
        nonlocal count
        print('--------begin inc')
        print(hex(id(count)))
        count += 1
        print(hex(id(count)))
        print('--------end inc')
        return count

    return inc

print('------------')
fn = counter()
print(fn.__code__.co_freevars)
print(fn.__closure__)

print(fn())
print(fn())
print(fn())


def outer(x):
    def inner():
        y = x

    print('print outer')
    print('create inner: ', inner.__closure__)
    return inner


f = outer(10)
print(f.__closure__)
print(id(f.__code__.co_freevars[0]))

f = outer(20)
print(f.__closure__)
print(id(f.__code__.co_freevars[0]))
"""

# 102. Closures - Coding
"""

def outer():
    x = 'python'
    def inner():
        print(x)
    return inner


fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)


def outer():
    x = [1, 2, 3]
    print(hex(id(x)))
    def inner():
        x = [1, 2, 3]
        print(hex(id(x)))
    return inner

fn = outer()
fn()


def outer():
    x = 'python'
    print(hex(id(x)))
    def inner():
        x = 'python'
        print(hex(id(x)))
    return inner


fn = outer()
fn()


def outer():
    x = [1, 2, 3]
    print(hex(id(x)))
    def inner():
        y = x
        print(hex(id(y)))
    return inner


fn = outer()
print(fn.__closure__)
fn()


def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc


fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(0)))

print(fn())

print(fn.__closure__)
print(hex(id(1)))


def outer():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2

fn1, fn2 = outer()

print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)
print(fn1.__closure__, fn2.__closure__)

print(fn1())
print(fn1.__closure__, fn2.__closure__)
print(fn2())
print(fn1.__closure__, fn2.__closure__)


def pow(n):
    def inner(x):
        return x ** n
    return inner

square = pow(2)
print(square.__closure__)
print(hex(id(2)))
print(square)
print(square(5))

cude = pow(3)
print(cude.__closure__)
print(hex(id(3)))
print(cude(5))


def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1.__closure__, add_2.__closure__, add_3.__closure__)
print(add_1(10), add_2(10), add_3(10))


addres = []
for n in range(1, 4):
    addres.append(lambda x: x + n)

print(addres)
print(n)
print(addres[0].__closure__)
print(addres[0](10))


def create_adders():
    addres = []
    for i in range(1, 4):
        addres.append(lambda x: x + i)
    return addres

adders = create_adders()

print(adders)
print(adders[0].__closure__)
print(adders[0].__code__.co_freevars)
print(adders[1].__closure__)
print(adders[2].__closure__)


print(adders[0](10))


def create_adders():
    addres = []
    for i in range(1, 4):
        addres.append(lambda x, y=i: x + y)
    return addres

adders = create_adders()

print(adders)
print(adders[0].__closure__)
print(adders[0].__code__.co_freevars)
print(adders[0](10))
"""

# 103. Closure Applications - Part 1
"""

class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

    def __str__(self):
        return str(self.numbers)


a = Averager()
print(a.add(10))
print(a)
print(a.add(20))
print(a)
print(a.add(30))
print(a)

b = Averager()
print(b.add(10))
print(b)


def average():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add


a = average()
print(a(10))
print(a(20))
print(a(30))

b = average()
print(b(10))


print(a.__closure__)
print(b.__closure__)


def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total / count
    return add

a = average()
print(a.__closure__)
print(a.__code__.co_freevars)
print(a(10))
print(a(20))
print(a(30))


class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count


from time import perf_counter

print(perf_counter())
print(perf_counter())


class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start


t1 = Timer()
print(t1())
print(t1())


def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll


t2 = timer()
print(t2())
print(t2())

"""

# 104. Closure Applications - Part 1
"""

def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter1 = counter()
print(counter1())
print(counter1())


def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


counter_add = counter(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)

result = counter_add(10, 20)
print(result)


counter_mult = counter(mult)
print(counter_mult(2, 5))


counters = dict()


def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner


counter_add = counter(add)
counter_mult = counter(mult)

print(counter_add(10, 20))
print(counter_add(20, 30))
print(counters)
print(counter_mult(2, 5))
print(counters)


def counter(fn, counter):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counter[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner


c= dict()
counter_add = counter(add, c)
counter_mult = counter(mult, c)

print(counters)


print(counter_add(10, 20))
print(counter_mult(2, 5))
print(counter_mult(3, 6))
print('----------', c)


def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product


print(fact(3))
print(fact(5))


counted_fact = counter(fact, c)
# print(counted_fact(5))
# print(c)

fact = counter(fact, c)
print(c)
print(fact.__closure__)
fact(3)
fact(5)
fact(10)
print(c)
"""


# 106. Decorators (Part 1) - Coding


# def counter(fn):
#     count = 0
#
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print('Function {0} (id={1}) was called {1} times'.format(fn.__name__, id(fn), count))
#         return fn(*args, **kwargs)
#     return inner
#
#
# def add(a: int, b: int = 0):
#     """
#     adds two values
#     """
#     return a + b
#
#
# # help(add)
#
# print(id(add))
# add = counter(add)
# print(id(add))
# # help(add)
#
#
# print(add(10, 20))
# print(add(20, 40))
# print(add(10))
#
#
# def mult(a: int, b: int, c: int = 1, *, d):
#     """
#     multiplies four values
#     """
#     return a * b * c * d
#
#
# print(mult(1, 2, 3, d=4))
# print(mult(1, 2, d=3))
# mult = counter(mult)
#
# # help(mult)
#
#
# print(mult(1, 2, 3, d=4))
# print(mult(1, 2, d=3))
#
#
# @counter
# def my_func(s: str, i: int) -> str:
#     return s * i
#
# # my_func = counter(my_func)
#
# # help(my_func)
#
# print(my_func('a', 10))
#
#
# print(mult.__name__)
# print(mult.__doc__)
#
#
# from functools import wraps
#
#
# def counter(fn):
#     count = 0
#
#     # @wraps(fn)
#     def inner(*args, **kwargs):
#         """
#         this is the inner closure
#         """
#         nonlocal count
#         count += 1
#         print('Function {0} (id={1}) was called {1} times'.format(fn.__name__, id(fn), count))
#         return fn(*args, **kwargs)
#     inner = wraps(fn)(inner)
#     return inner
#
#
# def mult(a: int, b: int, c: int = 1, *, d):
#     """
#     multiplies four values
#     """
#     return a * b * c * d
#
# help(mult)
# mult = counter(mult)
# help(mult)


# 107. Decorator Application(Timer)
"""

def timed(fn):
    from time import perf_counter
    from functools import wraps


    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, args_str, elapsed))

        return result
    return inner


def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)


# calc_recursive_fib(6)

@timed
def fib_recursive_fib(n):
    return calc_recursive_fib(n)


# print(fib_recursive_fib(6))
# print(fib_recursive_fib(20))
# print(fib_recursive_fib(25))
# print(fib_recursive_fib(30))
# print(fib_recursive_fib(36))


@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


print(fib_loop(6))
print(fib_loop(36))


from functools import reduce

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)
    return fib_n[0]


print(fib_reduce(35))
print(fib_loop(35))

"""


# 108. Decorator Application (Logger, Stacked Decorators)

"""

def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone


    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_dt, fn.__name__))
        return result
    return inner

@logged
def func_1():
    pass

@logged
def func_2():
    pass


# func_1()
# func_2()


def timed(fn):
    from functools import wraps
    from time import perf_counter


    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end-start))
        return result
    return inner


@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))


print(fact(3))
print(fact(5))


def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))


fact = logged(timed(fact))
fact(3)


def dec_1(fn):
    def inner():
        print('Running dec_1')
        return fn()
    return inner


def dec_2(fn):
    def inner():
        print('Running dec_2')
        return fn()
    return inner


@dec_1
@dec_2
def my_func():
    print('Running my_func')


# my_func = dec_1(dec_2(my_func))

my_func()


def dec_1(fn):
    def inner():
        result = fn()
        print('Running dec_1')
        return result
    return inner


def dec_2(fn):
    def inner():
        result = fn()
        print('Running dec_2')
        return result
    return inner


@dec_1
@dec_2
def my_func():
    print('Running my_func')


# my_func = dec_1(dec_2(my_func))

my_func()


def logged(fn):
    print('logged decorator running...')

    @timed
    def inner():
        print('logged inner running...')
        fn()

    return inner


def timed(fn):
    print('timer decorator running...')

    def inner():
        print('timer inner running...')
        fn()

    return inner


@logged
def fact():
    print('fact running...')


print('----------- ask ---------')
fact()
print('----------- ask ---------')
fact()

"""

# 109. Decorator Application (Memoization)
"""

def fib(n):
    print('Calculating fib ({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

# fib(10)

class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print('Calculating fib({0})'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]


# f = Fib()
# f.fib(10)


def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = calc_fib(n - 1) + calc_fib(n - 2)
        return cache[n]
    return calc_fib


# f = fib()
# print(f(10))
#
#
# g = Fib()
# print(g.fib(10))
#
#
# g = fib()
# print(g(10))


def memoize_fib(fib):
    cache = {1: 1, 2: 1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]
    return inner


@memoize_fib
def fib(n):
    print('Calculating fib ({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


# fib(10)


def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner


@memoize
def fib(n):
    print('Calculating fib ({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


# print(fib(10))
# print(fib(10))
# print(fib(11))


def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)


# print(fact(6))


@memoize
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)


# print(fact(6))
# print(fact(6))
# print(fact(7))


@memoize
def fib(n):
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


from time import perf_counter

start = perf_counter()
print(fib(200))
end = perf_counter()
print(end - start)

from functools import lru_cache


@lru_cache()
def fib(n):
    print('Calculating fib{0}!'.format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


# print(fib(10))
# print(fib(10))
# print(fib(11))


@lru_cache(maxsize=8)
def fib(n):
    print('Calculating fib{0}!'.format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


print(fib(8))
print(fib(8))
print(fib(16))
print(fib(8))
print(fib(9))
"""


# 111. Decorators (Part 2) - Coding
"""


def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print('Run time: {0:.6f}s'.format(elapsed))
        return result
    return inner


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)


# one way
#@timed
def fib(n):
    return calc_fib_recurse(n)


#second way
fib = timed(fib)


print(fib(30))



def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end - start)

        avg_run_time = total_elapsed / 10
        print('Avg Run time: {0:.6f}s'.format(avg_run_time))
        return result
    return inner


def fib(n):
    return calc_fib_recurse(n)


fib = timed(fib)
print(fib(28))


def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end - start)

        avg_run_time = total_elapsed / reps
        print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
        return result
    return inner


def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib, 5)

print(fib(28))


def dec(fn):
    print('running dec')

    def inner(*args, **kwargs):
        print('running inner')
        return fn(*args, **kwargs)

    return inner

@dec
def my_func():
    print('running my_func')


def my_func():
    print('running my_func')


my_func = dec(my_func)


my_func()


def dec_factory():
    print('running dec_factory')


    def dec(fn):
        print('running dec')

        def inner(*args, **kwargs):
            print('running inner')
            return fn(*args, **kwargs)

        return inner
    return dec


dec = dec_factory()


def my_func():
    print('running my_func')

my_func = dec(my_func)
my_func()

@dec
def my_func():
    print('running my_func')


my_func()


@dec_factory()
def my_func():
    print('running my_func')


def my_func():
    print('running my_func')


my_func = dec_factory()(my_func)


def dec_factory(a, b):
    print('running dec_factory')

    def dec(fn):
        print('running dec')

        def inner(*args, **kwargs):
            print('running inner')
            print('a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)

        return inner
    return dec


dec = dec_factory(10, 20)

@dec
def my_func():
    print('running my_func')

my_func()


@dec_factory(100, 200)
def my_func():
    print('running my_func')

my_func()


def my_func():
    print('running my_func')

my_func = dec_factory(150, 250)(my_func)

my_func()


def dec_factory(reps):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)

            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return timed


@dec_factory(5)
def fib(n):
    return calc_fib_recurse(n)


print(fib(28))


@dec_factory(15)
def fib(n):
    return calc_fib_recurse(n)


print(fib(28))


def timed(reps):
    def dec(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)

            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return dec


@timed(16)
def fib(n):
    return calc_fib_recurse(n)


fib(28)
"""

# 112. Decorator Application (Decorator Class)
"""

def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('decorated function called: a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec


@my_dec(10, 20)
def my_func(s):
    print('Hello {0}'.format(s))


my_func('World')


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c):
        print('called a={0}, b={1}, c={2}'.format(self.a, self.b, c))


obj = MyClass(10, 20)
print(obj)
obj.__call__(100)
obj(100)


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('decorated function called: a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner


@MyClass(10, 20)
def my_func(s):
    print('Hello {0}'.format(s))


my_func('World')


obj = MyClass(10, 20)


def my_func(s):
    print('Hello {0}'.format(s))


my_func = obj(my_func)
my_func('World')

"""

# 113. Decorator Application (Decorating Classes)
"""

from fractions import Fraction


f = Fraction(2, 3)


print(f.denominator)
print(f.numerator)

try:
    f.speak()
except AttributeError:
    pass


Fraction.speak = 100
print(f.speak)

Fraction.speak = lambda self, message: 'Fraction says: {0}'.format(message)


print(f.speak('This is a late parrot'))


f2 = Fraction(10, 5)


print(f2.speak('This parrot is no more.'))


Fraction.is_integral = lambda self: self.denominator == 1


f1 = Fraction(2, 3)
f2 = Fraction(64, 8)


print(f1)
print(f2)


print(f1.is_integral())
print(f2.is_integral())


def dec_speak(cls):
    cls.speak = lambda self, message: '{0} says: {1}'.format(self.__class__.__name__, message)
    return cls


Fraction = dec_speak(Fraction)
f1 = Fraction(2, 3)
print(f1.speak('hello'))


class Person:
    pass


Person = dec_speak(Person)
p = Person()

print(p.speak('this works!'))


from datetime import datetime, timezone


def info(self):
    results = []
    results.append('time: {0}'.format(datetime.now(timezone.utc)))
    results.append('Class: {0}'.format(self.__class__.__name__))
    results.append('id: {0}'.format(hex(id(self))))
    for k, v in vars(self).items():
        results.append('{0}: {1}'.format(k, v))
    return results


def debug_info(cls):
    cls.debug = info
    return cls


# there other way
@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi():
        return 'Hello there!'


# this one way
# Person = debug_info(Person)

p = Person('John', 1939)
print(p.debug())


@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0


    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('Speed cannot exceed top_speed.')
        else:
            self._speed = new_speed


favorite = Automobile('Ford', 'Model T', 1908, 45)
print(favorite.debug())

favorite.speed = 40

print(favorite.debug())

from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

print(abs(p1))

print(p1)
print(p1 is p2)
print(p2 is p3)
print(p1 == p2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __ne__(self, other):
        pass


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

print(abs(p1))

print(p1)
print(p1 is p2)
print(p2 is p3)
print(p1 == p2)
print(p3 == p1)

p4 = Point(100, 100)

print(p4 < p1)
print(p4 > p1)
print(p1 < p4)


def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not (self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)
    return cls


@complete_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented


p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 200)
print(p1 <= p4)
print(p3 >= p2)
print(p1 != p2)


from functools import total_ordering


@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented


p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 200)

print('---------------')
print(p1 <= p2)
print(p1 >= p4)
print(p1 != p2)




@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Point):
            return abs(self) > abs(other)
        else:
            return NotImplemented


p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 200)

print('---------------///---------------')
print(p4 > p1)
print(p2 <= p3)
print(p1 != p2)
"""


