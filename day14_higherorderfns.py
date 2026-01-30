## Fn as a param
from functools import reduce
def sum_numbers(nums): 
    return sum(nums)    

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

def square(x):       
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
    
def higher_order_fn(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
result = higher_order_fn('square')
print(result(3))
result = higher_order_fn('cube')
print(result(3))
result = higher_order_fn('absolute')
print(absolute(3))

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

### Python also has map(), filter() and reduce()
## map() function

numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2

nums_squared = map(square, numbers)
print(list(nums_squared))
print(list(map(lambda x: x**2, numbers)))

num_str = ['1', '2', '3', '4', '5']
print(list(map(int, num_str)))

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print(list(map(lambda x: x.upper(), names)))
         

# Filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

even_nums = filter(is_even, numbers)
odd_nums = filter(is_odd, numbers)
print(list(even_nums))
print(list(odd_nums))

### Reduce function
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)