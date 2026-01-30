a = 200_000
if a > 0:
    print('Mide is a millionaire in dollars!')

if a < 0:
    print('A is a negative number')
elif a> 0: 
    print("A is a positive number")
else:
    print('A is 0')

## shorthand
print('OG A is positive') if a > 0 else print('A is negative')

## Nested 
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even number')
    else:
        print('A is a positive number but not even')
elif a == 0:
    print('A is zero')
else: 
    print('A is a negative number')

## if condition and logical operators
if a > 0 and a % 2 == 0:
    print('A is a positive and even number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

## Exercises
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are old enough to drive')
# else:
#     print(f'You need to wait {18-age} more years to learn to drive')

## exercise 2
# my_age = 25
# your_age=int(input('Enter your age:'))

# if my_age > your_age:
#     if my_age - your_age > 1:
#         print(f'I am {my_age-your_age} years older than you')
#     else:
#         print(f'I am {my_age-your_age} year older than you')
# elif my_age < your_age:
#     if your_age - my_age > 1:
#         print(f'You are {your_age - my_age} years older than me')
#     else:
#         print(f'You are {your_age - my_age} year older than me')
# else: 
#     print('We are of the same age')

## exercise 3
# num1 = int(input('Enter number one:'))
# num2 = int(input('Enter number two:'))

# if num1 > num2:
#     print(f'{num1} is greater than {num2}')
# elif num2 > num1:
#     print(f'{num2} is greater than {num1}')
# else:
#     print('Both numbers are equal')

## exercise 4
# user_score = int(input('Enter your score:'))

# if user_score >= 90 and user_score <= 100:
#     print('Grade A')
# elif user_score >= 80 and user_score <= 89:
#     print('Grade B')
# elif user_score >= 70 and user_score <= 79:
#     print('Grade C')
# elif user_score >= 60 and user_score <= 69:
#     print('Grade D')
# elif user_score >= 0 and user_score <= 50:
#     print('Grade F')
# else:
#     print('Enter a valid score between 0-100')

##  exercise 5
# month = input('Enter month:')

# autumn = ['September', 'October', 'November']
# winter = ['December', 'January', 'February']
# spring = ['March', 'April', 'May']
# summer = ['June', 'July', 'August']

# if month in autumn:
#     print('The season is autumn')
# elif month in winter:
#     print('The season is winter')
# elif month in spring:
#     print('The season is spring')
# elif month in summer:
#     print('The season is summer')

## exercise 6
fruit = input('Enter fruit:')
fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else: 
    print('We have the fruit available')