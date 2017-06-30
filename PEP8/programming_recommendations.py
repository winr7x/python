import math
from functools import total_ordering


def item_1():
    def print_a_and_b(a, b):
        print('a ==', a, '\tb ==', b)

    # Implementations of Python: PyPy, Jython, IronPython, Cython, Psyco

    def inplace_concatenation():
        # In-place string concatenation
        a = 'aaa'
        b = 'bbb'
        print_a_and_b(a, b)
        a += b
        print_a_and_b(a, b)
        a = a + b
        print_a_and_b(a, b)
        print('\n')

    def join_concatenation():
        # ''.join() concatenation
        a = ['display', 'battery', 'keyboard']
        b = ' <--> '.join(a)
        print('{} == "{}"'.format(
            "'' <--> '.join(['display', 'battery', 'keyboard'])",
            b
        ))
        print('\n')

        c = 'xyz'
        d = '+'.join(c)
        print('{} == "{}"'.format("'+'.join('xyz')", d))
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

    list = [
        FiveCentricPoint('a', 1, 1),
        FiveCentricPoint('b', 6, 5),
        FiveCentricPoint('c', 5, 3),
    ]

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

    list = [
        Product('car', 92),
        Product('kettle', 1),
        Product('trampoline', 40),
    ]

    print('unsorted list', list)
    print('sorted list',
          sorted(list, key=lambda product: product.price))  # Good lambda use
    print('\n')


def item_6():
    # Exception vs. BaseException
    class AaaError(Exception):         # Error exception
        pass

    class Bbb(Exception):              # Non-error exception
        pass

    # class B(BaseException):          # Bad
        # pass

    # Locations where the exceptions are raised:            Bad
    # OSError: [Errno 2] No such file or directory: 'fff'
    # IOError: [Errno 2] No such file or directory: 'fff'

    # Answer to the question "What went wrong?              Good
    # FileNotFoundError: ...


def item_7():
    # Exception chaining

    def do_exception():
        0 / 0

    def python3():
        try:
            try:
                do_exception()
            except ZeroDivisionError as e:
                raise ValueError('Error at the same abstraction level as the '
                                 'function item_7') from e
        except ValueError:
            pass

    def python2():
        class SomeError(Exception):
            def __init__(self, message, cause):
                # Ensure that relevant details are transferred to
                # the new exception
                super().__init__(message + ', caused by ' + str(cause))
                self.cause = cause

        try:
            try:
                do_exception()
            except ZeroDivisionError as e:
                raise SomeError('Error at the same abstraction level as the '
                                'function item_7', e)
        except SomeError:
            pass

    python3()
    python2()


def item_8():
    # Python 2 raising exception form

    # raise ValueError('message')   # Preferred form
    # raise ValueError, 'message'   # bad older form
    pass


def item_9():
    # Specific exception vs. bare except:

    # try:
    #     pass
    # except:     # Bare except: It is equivalent to except BaseExceptio
    #     pass

    # rule of a thumb:

    # 1)
    # try:
    #     some work...
    # except:
    #     printing out the traceback...
    #     or logging the traceback...

    # 2)
    # try:
    #     some work...
    # except:
    #     cleanup work...
    #     propagate upwards with raise...
    #     (but try...finally can be a better way)

    try:
        0/0
    except Exception as e:  # Good catching of all exceptions
        pass


def item_10():
    # Explicit exception name binding vs. comma-based

    try:
        0/0
    except (TypeError, ZeroDivisionError) as e:     # Good
        pass

    # try:
    #     0/0
    # except (TypeError, ZeroDivisionError), e:     # Bad
    #     pass


def item_11():
    # Explicit exception hierarchy vs. errno

    f = 'nonexistentfile'

    try:
        open(f)
    except FileNotFoundError as e:                              # Good
        print(str(e))

    try:
        open(f)
    except IOError as e:
        print('Open file "{}". errno = {}'.format(f, e.errno))  # Bad


def item_12():
    # Minimum code in try:

    # try:
    #     value = collection[key]           # Minimum code here
    # except KeyError:
    #     return key_not_found(key)
    # else:
    #     return handle_value(value)

    # try:
    #     # Too broad!
    #     return handle_value(collection[key])
    # except KeyError:
    #     # Will also catch KeyError raised by handle_value()
    #     return key_not_found(key)
    pass


def item_13():
    # Ensure local resource is cleaned up

    # with open('somefile.txt', 'r') as f:
        # print(f.read())                   # Will be closed anyway

    file = None
    try:
        file = open('somefile2.txt', 'r')
        print(file.read())
    except Exception as e:
        print("Exception occured:", str(e))
    finally:                                # Will be closed anyway
        if file is None:
            print('File was not opened')
        else:
            print('Closing file...')
            file.close()
    print('\n')


def item_14():
    # Context expression explicitly indicates what Context manager do

    # with conn.begin_transaction():          # Good
    #     do_stuff_in_transaction(conn)

    # 'conn.begin_transaction()' explicitly indicates that we want to wrap
    # transaction stuff in some context

    # ====================================================================

    # with conn:                              # Bad
    #     do_stuff_in_transaction(conn)

    # 'conn' doesn't indicate that we want wrap transaction stuff in some
    # context.

    # Establishing connection is one thing,
    # but the transaction is another.

    # with establish_connection() as conn     # Good
    #     do_stuff_in_connection
    pass


def item_15():
    # Be constistent in return statements

    def foo(x):                     # Good
        if x >= 0:
            return math.sqrt(x)
        else:
            return None

    def bar(x):                     # Good
        if x < 0:
            return None
        return math.sqrt(x)

    def baz(x):
        if x >= 0:
            return math.sqrt(x)
        # Bad: must be 'return None' here

    def qux(x):
        if x < 0:
            return                  # Bad: must be explicit 'return None'
        return math.sqrt(x)


def item_16():
    # String methods instead of thie string module

    # In Python 2:

    # string.lower('AAABBB')            # Bad
    # string.upper('aaabbb')
    # string.split('a b c')
    # string.join(['E', 'W'], '!')
    # string.replace('abc', 'b', 'Z')
    # string.find('abc', 'c')
    # string.count('abca', 'a')

    # In Python 3:

    print('AAABBB'.lower())             # Good
    print('aaabbb'.upper())
    print('a b c'.split())
    print('!'.join(['E', 'W']))
    print('abc'.replace('b', 'Z'))
    print('abca'.count('a'))

    # Unicode
    print('Fichier δ non trouvé'.upper())
    print('FICHIER Δ NON TROUVÉ'.lower())
    print('FICHIER Δ NON TROUVÉ'.split('Δ'))
    print('Fichier δ non trouvé'.replace('δ', 'Δ'))
    print('Δ Fic ƍ hier δ no ƍ n ⲇ tro ƍ uvé Ⲇ'.count('ƍ'))


item_1()
item_2()
item_3()
item_4()
item_5()
item_6()
item_7()
item_8()
item_9()
item_10()
item_11()
item_12()
item_13()
item_14()
item_15()
item_16()
