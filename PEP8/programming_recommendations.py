def item_1():
	def print_a_and_b(a, b):
	    print("a ==", a, "\tb ==", b)

	# Implementations of Python: PyPy, Jython, IronPython, Cython, Psyco

	# In-place string concatenation
	a = "aaa"
	b = "bbb"
	print_a_and_b(a, b)
	a += b
	print_a_and_b(a, b)
	a = a + b
	print_a_and_b(a, b)
	print('\n')

	# ''.join() concatenation
	iterable1 = ["display", "battery", "keyboard"]
	joined1 = " <--> ".join(iterable1)
	print('" <--> ".join(["display", "battery", "keyboard"]) == "' + joined1 + '"')
	print('\n')

	iterable2 = "xyz"
	joined2 = "+".join(iterable2)
	print('"+".join("xyz") == "' + joined2 + '"')
	print('\n')


def item_2():
	# Comparisons to singletons
	a = 0
	if a is not None:
	    print('a is not None')

	# if a != None:             Bad
	    # print('a != None')    Bad

	b = ()
	print('b = () is',
	      'true' if b else 'false',
	      'in boolean context')

	# my_var true in context of "is my_var initialized"
	print('b = () is',
	      'true' if b is not None else 'false',
	      'in context "is initialized"')


item_1()
item_2()
