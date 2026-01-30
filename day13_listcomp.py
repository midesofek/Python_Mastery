## List comprehension
language = 'Python'
lst = [i for i in language]
print(type(lst))
print(lst)

numbers = [i for i in range(11)]
print(numbers)

# handle math operations during iterations
squares = [i * i for i in range(11)]
print(squares)

## LAMBDA FUNCTIONS in PYTHON
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(1,2,7))

## Self invoking
print((lambda x: x**2)(3))