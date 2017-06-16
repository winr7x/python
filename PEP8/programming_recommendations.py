# Implementations of Python: PyPy, Jython, IronPython, Cython, Psyco


def print_a_and_b(a, b):
    print("a ==", a, "\tb ==", b)


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

# Comparisons to singletons
# Todo == and is not None

c = ()
print('c = () is',
      'true' if c else 'false',
      'in boolean context')

# my_var true in context of "is my_var initialized"
print('c = () is',
      'true' if c is not None else 'false',
      'in context "is initialized"')
