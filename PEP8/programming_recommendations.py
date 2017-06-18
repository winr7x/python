import math
from functools import total_ordering


def item_1():
    def print_a_and_b(a, b):
        print("a ==", a, "\tb ==", b)

    # Implementations of Python: PyPy, Jython, IronPython, Cython, Psyco

    def inplace_concatenation():
        # In-place string concatenation
        a = "aaa"
        b = "bbb"
        print_a_and_b(a, b)
        a += b
        print_a_and_b(a, b)
        a = a + b
        print_a_and_b(a, b)
        print('\n')

    def join_concatenation():
        # ''.join() concatenation
        a = ["display", "battery", "keyboard"]
        b = " <--> ".join(a)
        print('" <--> ".join(["display", "battery", "keyboard"]) == "' + b + '"')
        print('\n')

        c = "xyz"
        d = "+".join(c)
        print('"+".join("xyz") == "' + d + '"')
        print('\n')

    inplace_concatenation()
    join_concatenation()


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

    print('\n')


def item_3():
    # is not Vs. not .. is
    class Cat:
        pass

    cat1 = Cat()
    cat2 = Cat()

    if cat1 is not cat2:
        print('cat1 is not cat2')

    # if not cat1 is cat2:              Bad
        # print('cat1 not is cat2')     Bad

    print('\n')


def item_4():
    # ordering operation
    @total_ordering         # try comment this line and check the result
    class FiveCentricPoint:
        def __init__(self, name, x, y):
            self.x = x
            self.y = y
            self.name = name

        def __repr__(self):
            return '{}({},{})'.format(self.name, self.x, self.y)

        def weight(self):
            x_part = (5 - self.x)**2
            y_part = (5 - self.y)**2
            return math.sqrt(x_part + y_part)

        def __eq__(self, other):
            # try comment this method and check the result
            # try comment this method and @total_ordering and check the result
            return self.weight == other.weight()

        def __gt__(self, other):
            # try comment this method and check the result
            # try comment this method and @total_ordering and check the result
            return self.weight() > other.weight()

    list = [FiveCentricPoint('a', 1, 1),
            FiveCentricPoint('b', 6, 5),
            FiveCentricPoint('c', 5, 3)]

    print(sorted(list))
    print(list[0].__ne__(list[1]))
    print(list[0].__gt__(list[1]))
    print(list[0].__lt__(list[1]))
    print(list[0].__ge__(list[1]))
    print(list[0].__le__(list[1]))
    print('\n')


def item_5():
    # def vs. lambda
    def f_def(x):
        return 2*x

    # f_lam = lambda x: 2*x                                 # Bad lambda use

    print('f_def(3) ==', f_def(3))

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __repr__(self):
            return '[{}-{}]'.format(self.name, self.price)

    list = [Product('car', 92),
            Product('kettle', 1),
            Product('trampoline', 40)]

    print("unsorted list", list)
    print("sorted list",
          sorted(list, key=lambda product: product.price))  # Good lambda use
    print('\n')


item_1()
item_2()
item_3()
item_4()
item_5()
