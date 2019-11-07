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
