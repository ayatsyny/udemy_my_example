
# 119. Tuples as Data Structures - Coding
"""


print((10, 20, 30))
a = (10, 20, 30)
b = 10, 20, 30

print(type(a))
print(type(b))


def print_tuple(t):
    for e in t:
        print(e)


print_tuple((10, 20, 30))

a = 'a', 10, 200

print(a[0], a[1])

a = 1, 2, 3, 4, 5, 6
print(type(a))


print(a[2:5])


for e in a:
    print(e)


a = 'a', 10, 20
x, y, z = a
print(x, z)


a = 1, 2, 3, 4, 5
x, *other, y, z = a

print(x)
print(y)
print(z)
print(other)


x, *_, y, z = a
print(x, y, z)
print(_)

print(a[0])
try:
    a[0] = 100
except TypeError:
    pass


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'


pt = Point2D(10, 20)
print(pt, id(pt))
pt.x = 100
print(pt, id(pt))


a = Point2D(0, 0), Point2D(10, 20)
print(a)
print(id(a[0]))
a[0].x = 100
print(a)


s = 'python'
print(id(s))
s = 'python' + ' rocks!'
print(s, id(s))


a = 1, 2, 3
print(id(a))

a += (4, 5)
print(a)
print(id(a))


pt1 = (0, 0)
pt2 = (10, 20)

london = 'London', 'UK', 8_780_000
new_your = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000


print(london)
cities = [london, new_your, beijing]
total = 0
for city in cities:
    total += city[2]

print(total)


total = sum(city[2] for city in cities)

record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072
symbol, year, month, day, open_, high, low, close = record

print(symbol, close)

symbol, *_, close = record

print(symbol, close)
print(_)


for city, country, population in cities:
    print(city, country, population)


for index, city in enumerate(cities):
    print(index, city)


from random import uniform
from math import sqrt


def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False

    return random_x, random_y, is_in_circle


num_attempts = 1_000_000
count_inside = 0
for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1


print(f'Pi is approximately: {4 * count_inside / num_attempts}')
"""

# 121. Named Tuples - Coding
"""

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


from collections import namedtuple


Point2D = namedtuple('Point2D', ['x', 'y'])
pt1 = Point2D(10, 20)
print(pt1)
pt3d_1 = Point3D(10, 20, 30)
print(pt3d_1)


Point2D = namedtuple('Point2D', ('x', 'y'))
pt2 = Point2D(10, 20)
print(pt2)

Pt3D = Point3D
p = Pt3D(10, 20, 30)
print(p)

p = Point3D(x=10, y=20, z=30)
print(p.x, p.y)


p = Point2D(x=10, y=20)
print(p)
print(isinstance(p, tuple))
p = Point3D(x=10, y=20, z=30)
print(isinstance(p, tuple))


a = (10, 20)
b = (10, 20)
print(a is b)
print(a == b)


pt1 = Point2D(10, 20)
pt2 = Point2D(10, 20)

print(pt1 is pt2)
print(pt1 == pt2)


pt1 = Point3D(10, 20, 30)
pt2 = Point3D(10, 20, 30)

print(pt1 is pt2)
print(pt1 == pt2)


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.x}, z={self.z})'

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False


pt1 = Point3D(10, 20, 30)
pt2 = Point3D(10, 20, 30)

print(pt1)
print(pt1 == pt2)


pt1 = Point2D(10, 20)
pt2 = Point3D(10, 20, 30)

print(max(pt1))

try:
    print(max(pt2))
except TypeError:
    pass


def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


pt1 = Point3D(1, 2, 3)
pt2 = Point3D(1, 1, 1)


print(dot_product_3d(pt1, pt2))

a = (1, 2)
b = (1, 1)
print(list(zip(a, b)))
print(sum(e[0] * e[1] for e in zip(a, b)))


def dot_product(a, b):
    return sum(e[0] * e[1] for e in zip(a, b))


print(dot_product(a, b))
pt1 = Point2D(1, 2)
pt2 = Point2D(1, 1)

print(dot_product(pt1, pt2))

Vector3D = namedtuple('Vector3D', 'x y z')

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(1, 1, 1)
print(v1)
print(dot_product(v1, v2))

print(v1)
print(tuple(v1))


print(v1[0])
print(v1[0:2])
print(v1)
print(v1.x)
print(v1.y)


Circle = namedtuple('Circle', 'center_x center_y      radius')
c = Circle(0, 0, 10)
print(c)
print(c.radius)


Stock = namedtuple('Stock', '''symbol
                                    year
                                    month
                                    day
                                    open
                                    high
                                    low
                                    close''')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print(djia)

print(djia.close)

for item in djia:
    print(item)


p = Point2D(10, 20)
x, y = p
print(x, y)
print(djia)

symbol, year, month, day, *_, close = djia
print(symbol, year, month, day, close)
print(_)


Person = namedtuple('Person', 'name age _ssn', rename=True)
print(Person._fields)

print(Point2D._fields)
print(Stock._fields)


print(Stock._source)

print(Point2D._source)


print(djia)
print(djia._asdict())
d = djia._asdict()
print(dict(djia._asdict()))
"""

# 123. Named Tuples - Modifying and Extending - Coding
"""

from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')
pt = Point2D(10, 20)
print(pt)
print(pt[0])
print(pt.x)

try:
    pt.x = 100
except AttributeError:
    pass

try:
    pt[0] = 100
except TypeError:
    pass


print(id(pt))
pt = Point2D(100, pt.y)
print(pt)
print(id(pt))


s = 'python'
print(id(s))

s += ' rocks!'
print(s)
print(id(s))


Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

print(djia)


djia = Stock(djia.symbol, djia.year, djia.month, djia.day, djia.open, djia.high, djia.low, 1000)

print(djia)

*values, _ = djia
print(values)

values.append(26_393)
print(values)

djia = Stock(*values)
print(djia)

a = [1, 2, 3]
print(id(a))
a = a + [4, 5]
print(a)
print(id(a))

a = [1, 2, 3]
print(a)
print(id(a))
a.append(4)
print(a)
print(id(a))
a.extend([5, 6, 7])
print(a)
print(id(a))


print(djia)
values = djia[:7]
print(values)
print(type(values))

print(values + (100,))

djia = Stock(*(values + (100 ,)))
print(djia)


djia = Stock(*values, 1000)
print(djia)


print(id(djia))
djia = djia._replace(year=2019, open=10000)
print(djia)
print(id(djia))

djia = Stock._make(values + (100,))
print(djia)

djia = djia._replace(close=10000)
print(djia)


print(Point2D)
print(Point2D._fields)
print(Point2D._fields + ('z', ))


Point3D = namedtuple('Point3D', Point2D._fields + ('z', ))
print(Point3D._fields)

print(Stock._fields)
StockExt = namedtuple('StockExt', Stock._fields + ('previous_close', ))
print(StockExt._fields)


print(pt)

pt3d = Point3D(*pt, 100)
print(pt3d)


print(djia)
djia_ext = StockExt(*djia, 1_000_000)
print(djia_ext)

"""

# 125. Named Tuples - DocStrings and Default Values - Coding
"""

from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')
print(Point2D.__doc__)
print(Point2D.x.__doc__)
print(Point2D.y.__doc__)

Point2D.__doc__ = '2D Cartesian coordinate'
Point2D.x.__doc__ = 'x coordinate'
Point2D.y.__doc__ = 'y coordinate'


print(Point2D.__doc__)
print(Point2D.x.__doc__)
print(Point2D.y.__doc__)


# PROOTYPE

Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
print(Vector2D._fields)
v1 = Vector2D(0, 0, 10, 10, 0, 0)
print(v1)

vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
print(vector_zero)


v2 = vector_zero._replace(x1=10, y1=10, x2=20, y2=20)
print(v2)

vector_altorigin = Vector2D(0, 0, 0, 0, -10, -10)


def func(a, b=10, c=20):
    print(a, b, c)


func(1)
print(func.__defaults__)

func.__defaults__ = (100, 200, 300)
func()

print(Vector2D.__new__.__defaults__)
print(type(Vector2D.__new__.__defaults__))

Vector2D.__new__.__defaults__ = (0, 0)

v1 = Vector2D(10, 10, 20, 20)
print(v1)


Vector2D.__new__.__defaults__ = (-10, -10)
v1 = Vector2D(10, 10, 20, 20)
print(v1)
"""


# 126. Named Tuples - Application - Returning Multiple Values
"""

from random import randint, random
from collections import namedtuple


def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha


color = random_color()
print(color)
red, green, blue, alpha = color
print(red)
print(alpha)


Color = namedtuple('Color', 'red green blue alpha')


def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)


color = random_color()
print(color)
print(color.red)
print(color.alpha)

"""

# 127. Named Tuples - Application - Alternative to Dictionaries


data_dict = dict(key1=100, key2=200, key3=300)
print(data_dict['key1'])


from collections import namedtuple

print(data_dict.keys())
Data = namedtuple('Data', data_dict.keys())
print(Data._fields)
print(data_dict.values())
d1 = Data(*data_dict.values())
print(d1)


d2 = Data(key1=10, key3=30, key2=20)
print(d2)

Data = namedtuple('Data', 'key3 key2 key1')
print(Data._fields)


d2 = Data(*data_dict.values())
print(d2)

key_name = 'key2'
print(data_dict[key_name])

print(getattr(d2, key_name))
print(data_dict.get('key1', None))
print(data_dict.get('key10', None))
print(data_dict.get('key10', None))
print(data_dict['key1'])
print(d2.key1)


data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

keys = set()

for d in data_list:
    for key in d.keys():
        keys.add(key)


print(keys)


keys = {key for dict_ in data_list for key in dict_.keys()}
print(keys)


Struct = namedtuple('Struct', sorted(keys))
print(Struct._fields)

Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)

print(Struct(key3=10))


data_list = [
    {'key2': 2, 'key1': 1},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]


tuple_list = []
for dict_ in data_list:
    tuple_list.append(Struct(**dict_))

print(tuple_list)


def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', sorted(keys), rename=True)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]


tuple_list = tuplify_dicts(data_list)
print(tuple_list)



