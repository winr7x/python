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


item_1()
item_2()
item_3()
