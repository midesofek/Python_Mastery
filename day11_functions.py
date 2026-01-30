def generate_full_name ():
    first_name ='Mide'
    last_name = 'Sofek'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add():
    num_one = 2
    num_two = 4
    return (num_one+num_two)
print(add())

def greetings(name):
    return name + ', welcome to Python Course!'
print(greetings('Mide Sofek'))

def add_200k(num):
    return int(num) + 200_000
print(add_200k(15_000))

def square_num(num):
    return num * num
print(square_num(100))

def calc_area_of_circle(r):
    return 3.14 * int(r) ** 2
print(calc_area_of_circle(5))

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print(sum_of_numbers(5))

def generate_full_name(first_name, last_name):
    return first_name + ' ' + last_name
print(generate_full_name('Mide', 'Sofek'))

def sum_two_numbers(num_one, num_two):
    return f'${num_one + num_two}'
print(sum_two_numbers(100_000, 100_000))

def calc_age(current_year, birth_year):
    return current_year - birth_year
print(calc_age(2026, 1979))

def weight_of_object(mass, gravity):
    return str(mass * gravity)+ ' N'
print('The weight of the object is ', weight_of_object(50, 7.8))

## Passing args with key & value: order does not matter
print(sum_two_numbers(num_two=150_000, num_one=50_000))

def greet_dev(name='Banks'):
    return name + ', welcome back to work!'
print(greet_dev)

## Arbitrary number of params
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2,4,6,8,10))

## Default and arbitrary number of params in functions
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
    return len(args)
print(generate_groups('Team-Rich', 'Mide', 'Muyiwa', 'Joshua'))

## Dictionary unpacking
# calling a function with a dict with matching key names
def greet(name, location):
    print("Hi ", name, ", how is the weather in", location, "?")
name_dct = {'name': 'Mide', 'location': 'Doha'}
greet(**name_dct) # the magic happens here

## function as a param in another function
def square_number(n):
    return n ** n
def do_sth(f, k):
    return f(k)
print(do_sth(square_num, 4))

def calc_area_of_circle(r):
    π =  3.14
    return π * r * r
print(calc_area_of_circle(50))

def add_all_nums(*args):
    total = 0
    for num in args:
        if type(num) is int:
            total += num
        else:
            print('Arg must be number:',num )
            break
    return total
print(add_all_nums(2,3,4,5,6,7))

def convert_celsius_to_fahrenheit(c):
    # (°C x 9/5) + 32
    f = (c * 9/5) + 32
    return f
print('°F is:', convert_celsius_to_fahrenheit(30))