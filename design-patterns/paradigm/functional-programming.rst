Functional Programming
======================


Pure function
-------------
* Function which returns always the same results based on the same argument.
* ``random.randint()`` - Not pure
* ``pow()`` - Pure


Lambda - Anonymous functions
----------------------------
Example 1:

>>> DATA = [1, 2, 3, 4]
>>>
>>>
>>> def is_even(x):
...     if x % 2 == 0:
...         return True
...     else:
...         return False
>>>
>>>
>>> result = filter(is_even, DATA)
>>> print(list(result))
[2, 4]

>>> DATA = [1, 2, 3, 4]
>>>
>>> result = filter(lambda x: x % 2 == 0, DATA)
>>> print(list(result))
[2, 4]

Example 2:

>>> DATA = [{'user': 'twardowski', 'uid': 1000},
...         {'user': 'root', 'uid': 0}]
>>>
>>> def is_system_user(data):
...     if data['uid'] < 1000:
...         return True
...     else:
...         return False
>>>
>>> result = []
>>>
>>> for user in DATA:
...     if is_system_user(user):
...         result.append(user)
>>>
>>> print(result)
[{'user': 'root', 'uid': 0}]

>>> DATA = [{'user': 'twardowski', 'uid': 1000},
...         {'user': 'root', 'uid': 0}]
>>>
>>>
>>> result = filter(lambda x: x['uid'] < 1000, DATA)
>>>
>>> print(list(result))
[{'user': 'root', 'uid': 0}]

Monkey patching:

>>> class Astronaut:
...     pass
>>>
>>> jan = Astronaut()
>>> jan.say_hello = lambda: print('hello')
>>>
>>> jan.say_hello()
hello


Function Passing
----------------
.. code-block:: python

    print(
        tuple(
            filter(lambda x: x[1]<100,
                   enumerate(
                       filter(lambda x: x%2==0,
                              map(lambda x: pow(x, 2),
                                  map(float,
                                      (x for x in range(0, 34) if x % 3 == 0
    ))))))))


``functools``
-------------
Reduce:

>>> from functools import reduce
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5]
>>>
>>> def add(x, y):
...     return (x + y)
>>>
>>> result = reduce(add, DATA)
>>>
>>> print(result)
15

>>> from functools import reduce
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5]
>>>
>>> result = reduce(lambda x, y: x + y, DATA)
>>>
>>> print(result)
15

``lru_cache``:

>>> from functools import lru_cache
>>>
>>>
>>> @lru_cache(maxsize=None)
... def fib(num):
...     if num < 2:
...         return num
...     else:
...         return fib(num-1) + fib(num-2)
>>>
>>>
>>> fib(16)
987
>>>
>>> fib  # doctest: +SKIP
<functools._lru_cache_wrapper object at 0x...>
>>>
>>> fib.cache_info()
CacheInfo(hits=14, misses=17, maxsize=None, currsize=17)

memoize:

>>> def factorial(n):
...     if not hasattr(factorial, '__cache__'):
...         factorial.__cache__ = {1: 1}
...
...     if not n in factorial.__cache__:
...         factorial.__cache__[n] = n * factorial(n - 1)
...
...     return factorial.__cache__[n]
>>>
>>>
>>> factorial(5)
120
>>>
>>> factorial.__cache__
{1: 1, 2: 2, 3: 6, 4: 24, 5: 120}

>>> def memoize(function):
...     from functools import wraps
...
...     memo = {}
...
...     @wraps(function)
...     def wrapper(*args):
...         if args in memo:
...             return memo[args]
...         else:
...             rv = function(*args)
...             memo[args] = rv
...             return rv
...     return wrapper
>>>
>>>
>>> @memoize
... def fibonacci(n):
...     if n < 2: return n
...     return fibonacci(n - 1) + fibonacci(n - 2)
>>>
>>> fibonacci(25)
75025

partial:

* Create alias function and its arguments
* Useful when you need to pass function with arguments to for example ``map`` or ``filter``

>>> from functools import partial
>>>
>>>
>>> basetwo = partial(int, base=2)
>>> basetwo.__doc__ = 'Convert base 2 string to an int.'
>>> basetwo('10010')
18

partialmethod:

>>> from functools import partialmethod
>>>
>>>
>>> class Cell(object):
...     def __init__(self):
...         self._alive = False
...
...     @property
...     def alive(self):
...         return self._alive
...
...     def set_state(self, state):
...         self._alive = bool(state)
...
...     set_alive = partialmethod(set_state, True)
...     set_dead = partialmethod(set_state, False)
>>>
>>>
>>> c = Cell()
>>>
>>> c.alive
False
>>>
>>> c.set_alive()
>>> c.alive
True

reduce:

Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned.

Roughly equivalent to:

>>> def reduce(function, iterable, initializer=None):
...     it = iter(iterable)
...     if initializer is None:
...         value = next(it)
...     else:
...         value = initializer
...     for element in it:
...         value = function(value, element)
...     return value

singledispatch:

* Since Python 3.4
* Overload a method
* Python will choose function to run based on argument type

>>> from functools import singledispatch
>>>
>>>
>>> @singledispatch
... def celsius_to_kelvin(arg):
...     raise NotImplementedError('Argument must be int or list')
>>>
>>> @celsius_to_kelvin.register
... def _(degree: int):
...     return degree + 273.15
>>>
>>> @celsius_to_kelvin.register
... def _(degrees: list):
...     return [d+273.15 for d in degrees]
>>>
>>>
>>> celsius_to_kelvin(1)
274.15
>>>
>>> celsius_to_kelvin([1,2])
[274.15, 275.15]
>>>
>>> celsius_to_kelvin((1,2))
Traceback (most recent call last):
NotImplementedError: Argument must be int or list

singledispatchmethod:

* Since Python 3.8
* Overload a method
* Python will choose method to run based on argument type

>>> from functools import singledispatchmethod
>>>
>>>
>>> class Converter:
...
...     @singledispatchmethod
...     def celsius_to_kelvin(*args):
...         raise NotImplementedError('Argument must be int or list')
...
...     @celsius_to_kelvin.register
...     def _(self, degree: int):
...         return degree + 273.15
...
...     @celsius_to_kelvin.register
...     def _(self, degrees: list):
...         return [d+273.15 for d in degrees]
>>>
>>>
>>> conv = Converter()
>>>
>>> conv.celsius_to_kelvin(1)
274.15
>>>
>>> conv.celsius_to_kelvin([1,2])
[274.15, 275.15]
>>>
>>> conv.celsius_to_kelvin((1,2))
Traceback (most recent call last):
NotImplementedError: Argument must be int or list


Callback
--------
>>> import requests
>>> from http import HTTPStatus
>>>
>>>
>>> def http(obj):
...     response = requests.request(
...         method=obj.method,
...         data=obj.data,
...         path=obj.path)
...
...     if response == HTTPStatus.OK:
...         return obj.on_success(response)
...     else:
...         return obj.on_error(response)
>>>
>>>
>>> class Request:
...     method = 'GET'
...     path = '/index'
...     data = None
...
...     def on_success(self, response):
...         print('Success!')
...
...     def on_error(self, response):
...         print('Error')
>>>
>>> http(Request())  # doctest: +SKIP


Assignments
-----------
.. literalinclude:: assignments/paradigm_functional_a.py
    :caption: :download:`Solution <assignments/paradigm_functional_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/paradigm_functional_b.py
    :caption: :download:`Solution <assignments/paradigm_functional_b.py>`
    :end-before: # Solution
