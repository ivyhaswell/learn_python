# Fibonacci series:
def fiboonacci(n):
    """ print a fibonacci series up to n """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


f100 = fiboonacci(100)
f100


def default_params(a, l=[]):
    l.append(a)
    print(l)


default_params(1)
default_params(2)
default_params(3)


def default_params2(a, l=None):
    if l is None:
        l = []
    l.append(a)
    print(l)


default_params2(1)
default_params2(2)
default_params2(3)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print('args' + "-" * 40)

    for arg in arguments:
        print(arg)

    print('keywords' + "-" * 40)

    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def my_function():
    """Do nothing, but document it.
    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)

# 元组不可变，但是能包含可变对象，可变对象改变了，元组也会对应改变
l1 = [1,2,3]
l2 = [4,5,6]

t1 = (l1,l2)
l1[0] = 10
print(t1)

tk1 = (1,2)
tk2 = (1,2)
dict1 = {tk1: 'tk1'}
print(dict1.get(tk1))
print(dict1.get(tk2))

import builtins
dir(builtins)


class A:
    a='a'

class B:
    a = 'b'

class C(B,A):
    pass

ci = C()
print(ci.a)

import os
help(os)

import datetime
today = datetime.date.today()
bd = datetime.date(1993,5,25)
today - bd

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
unittest.main()  # Calling from the command line invokes all tests
