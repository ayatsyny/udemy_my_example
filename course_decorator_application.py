
# 114. Decorator Application (Dispatching) Part - 1


from html import escape


def html_escape(arg):
	return escape(str(arg))


def html_int(a):
	return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


def html_real(a):
	return '{0:.2f}'.format(round(a, 2))


def html_str(s):
	return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
	items = ('<li>{0}</li>'.format(html_escape(item)) for item in l)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
	items = ('<li>{0}={1}</li>'.format(k, v) for k, v in d.items())
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'



print(html_str("""this is
	a muli line string
	with special characters: 10 < 100"""))

print(html_int(255))



print(html_escape(3+10j))


from decimal import Decimal


def htmlize(arg):
	if isinstance(arg, int):
		return html_int(arg)
	elif isinstance(arg, float) or isinstance(arg, Decimal):
		return html_real(arg)
	elif isinstance(arg, str):
		return html_str(arg)
	elif isinstance(arg, list) or isinstance(arg, tuple):
		return html_list(arg)
	elif isinstance(arg, dict):
		return html_dict(arg)
	else:
		return html_escape(arg)


print(htmlize(100))
print(htmlize("""Python
	rocks!"""))


print(htmlize([1, 2, 3]))

print(htmlize(["""Python rocks! 0 < 1""", (10, 20, 30), 100]))


def func1():
	func2()


def func2():
	print('func2')


func1()


from decimal import Decimal
from html import escape


def htmlize(arg):
	if isinstance(arg, int):
		return html_int(arg)
	elif isinstance(arg, float) or isinstance(arg, Decimal):
		return html_real(arg)
	elif isinstance(arg, str):
		return html_str(arg)
	elif isinstance(arg, list) or isinstance(arg, tuple):
		return html_list(arg)
	elif isinstance(arg, dict):
		return html_dict(arg)
	elif isinstance(arg, set):
		return html_set(arg)
	else:
		return html_escape(arg)


def html_escape(arg):
	return escape(str(arg))


def html_int(a):
	return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


def html_real(a):
	return '{0:.2f}'.format(round(a, 2))


def html_str(s):
	return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
	items = ('<li>{0}</li>'.format(htmlize(item))
		for item in l
		)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
	items = ('<li>{0}={1}</li>'.format(html_escape(k), htmlize(v))
		for k, v in d.items()
		)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_set(arg):
	return html_list(arg)


print(htmlize(100))


print(htmlize(["""Python
	rocks! 0 < 1""", (10, 20, 30), 100]))


print('-------------')
print(htmlize({1, 2, 3}))


def htmlize(arg):
	registry = {
		object: html_escape,
		int: html_int,
		float: html_real,
		Decimal: html_str,
		str: html_str,
		list: html_list,
		tuple: html_list,
		set: html_dict
	}

	fn = registry.get(type(arg), registry[object])
	return fn(arg)


print('--------58264-----')
print(htmlize(100))
print(htmlize([1, 2, 3]))


def singledispatch(fn):
	registry = {}

	registry[object] = fn

	def inner(arg):
		return registry[object](arg)

	return inner


@singledispatch
def htmlize(a):
	return escape(str(a))


print(htmlize('1 < 100'))



def singledispatch(fn):
	registry = {}

	registry[object] = fn
	registry[int] = lambda a: '{0}(<i>{1}</i>)'.format(a, str(hex(a)))
	registry[str] = lambda s: escape(s).replace('\n', '<br/>\n')


	def inner(arg):
		return registry.get(type(arg), registry[object])(arg)

	return inner


@singledispatch
def htmlize(a):
	return escape(str(a))


print(htmlize('1 < 100'))
print(htmlize(100))


def singledispatch(fn):
	registry = {}

	registry[object] = fn

	def decorated(arg):
		return registry.get(type(arg), registry[object])(arg)

	def register(type_):
		def inner(fn):
			registry[type_] = fn
			return fn
		return inner

	def dispatch(type_):
		return registry.get(type_, registry[object])


	decorated.register = register
	decorated.dispatch = dispatch
	# decorated.registry = registry

	return decorated

 
@singledispatch
def htmlize(a):
	return escape(str(a))


print(htmlize('1 < 100'))
print(htmlize.register)


@htmlize.register(int)
def html_int(a):
	return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

print(html_int)
print(htmlize(100))
print('--------- dispatch ---------')
print(htmlize.dispatch(int))
# print(htmlize.registry)

# one way
# other way after declate this function 
# html_list = htmlize.register(list)(html_list)
@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
	items = ('<li>{0}</li>'.format(htmlize(item))
		for item in l
		)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


# print(htmlize.registry)
print(htmlize([1, 2, 3]))
print(htmlize((1, 2, 3)))


from numbers import Integral

@singledispatch
def htmlize(a):
	return escape(str(a))


@htmlize.register(Integral)
def html_integral_number(a):
	return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


print(isinstance(True, Integral))
print(htmlize(10))


@htmlize.register(int)
@htmlize.register(bool)
def html_integral_number(a):
	return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


print(htmlize(10))
print(htmlize(True))


from collections.abc import Sequence


print(isinstance([1, 2, 3], Sequence))
print(isinstance((1, 2, 3), Sequence))

print(type([1, 2, 3]) is Sequence)



from functools import singledispatch
from collections.abc import Sequence

@singledispatch
def htmlize(a):
	return escape(str(a))


print(htmlize.registry)
print(htmlize.dispatch(str))


@htmlize.register(Integral)
def htmlize_integral_number(a):
	return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


print(htmlize.registry)
print(htmlize.dispatch(int))
print(htmlize.dispatch(str))


@htmlize.register(Integral)
def htmlize_integral_number(a):
	return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

print(htmlize.registry)


print(type(10))
print(isinstance(10, int))
print(isinstance(10, Integral))
print(isinstance(True, Integral))


print(htmlize.dispatch(bool))
print(htmlize(10))
print(htmlize(True))


@htmlize.register(Sequence)
def html_sequence(l):
	items = ('<li>{0}</li>'.format(htmlize(item))
		for item in l
		)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(htmlize([1, 2, 3]))
print(htmlize((1, 2, 3)))


print(isinstance('python', Sequence))
for s in 'python':
	print(s)


# print(htmlize('python'))

@htmlize.register(str)
def html_str(s):
	return html_escape(s).replace('\n', '<br/>\n')


print(htmlize('python 1 < 100'))
print(htmlize([1, 2, 3]))
print(htmlize((1, 2, 3)))


@htmlize.register(tuple)
def html_tuple(t):
	items = (escape(str(item)) for item in t)
	return '({0})'.format(', '.join(items))



print(htmlize((1, 2, 3)))
print(htmlize([1, 2, 3]))


@singledispatch
def htmlize(a):
	return escape(str(a))


@htmlize.register(Integral)
def _(a):
	return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


@htmlize.register(Sequence)
def _(l):
	items = ('<li>{0}</li>'.format(htmlize(item))
		for item in l
		)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(str)
def _(s):
	return html_escape(s).replace('\n', '<br/>\n')


print(htmlize.registry)


print(htmlize(100))
print(htmlize([1, 2, 3]))


print(_)
print(htmlize.dispatch(Integral))
print(htmlize.dispatch(str))
print(id(htmlize.dispatch(Sequence)))
print(id(htmlize.dispatch(Integral)))
print(id(htmlize.dispatch(str)))
print(id(_))




