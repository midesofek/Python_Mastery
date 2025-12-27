letter='millions' # single line strings
print('millions')

multiline_string = '''This is how to write

A multi line string in python

With 3 single quotes or double quotes
'''
# print(multiline_string)

## String concatenation
first_letter = 'Mide'
second_letter = 'Sofek'
print(first_letter + ' ' + second_letter)

## Escape Sequences in Strings
# \n \t (tab 8 spaces) \\ (back slash) \' (single) \"" (double quote)
print('Python has new lines also\nLike this\n')
print('Lets\tNow\tUse\tTabs')
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is how we use backslash symbol(\\)')
print('We use single quote within single quote like this(\') and double quotes(\")')

## String Formatting
# OLD METHOD USING --> % Operator:
'''
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
'''
first_name = 'Mide'
second_name = 'Sofek'
language='Python'
formatted_output='I am %s %s. I\'m learning %s' %(first_name, second_name, language)
print(formatted_output)

# Strings & Numbers Formatting
r = 10
pi = 3.14
area=pi* r ** 2
print('The area of a circle with a radius %d is %.2f'%(r, area)) 

python_libraries = ['Django', 'Flask', 'NumPy', 'MatplotLib', 'Pandas']
formated_string = 'The following are Python libraries: %s'%(python_libraries)
print(formated_string)

## NEW FORMATTING STYLE introduced by python v3
newformatted_output = 'I am {} {}. I am learning {}'.format(first_name, second_name, language)
print(newformatted_output)

# a=3
# b=2
# print('{} + {} = {}'.format(a,b, a+b))

# ## NEW FORMATTING USING fStrings - Python v3.6+
# print(f'{a} + {b} = {a+b}')

# Unpacking Characters (Destructuring)
lang = 'Python'
a,b,c,d,e,f = lang
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# ## Accessing chars in strings by index
# print(lang[0])
# print(lang[1])
# print(lang[2])
# print(lang[3])
# print(lang[4])
# print(lang[5])
# print(lang[-1])
# print(lang[-2])

## Slicing Python Strings
print(lang[0:3]) #pyt
print(lang[3:6]) #hon
# Another way
print(lang[-3:]) #hon
print(lang[3:]) #hon
print(lang[0:]) #python

## Reversing a string
print(lang[::-1])

## Skipping characters while slicing
print(lang[0:5:2])

## String Methods
# capitalize()  count()     endswith()      expandtabs()  
# find()        rfind()     format()        index()     
# rindex()      isalnum()   isalpha()       isdecimal
# isdigit()     isnumeric() isidentifier()  islower()
# isupper()     join()      strip()         replace()
# split()       title()     swapcase()      startswith()

# capitalize()
greeting = "hello world!"
print(greeting.capitalize()) # this converts ONLY the first character of the string (Hello world!)

# count(substring, start=.., end=..)
print(greeting.count('l')) #3
print(greeting.count('l', 6, 12)) #1

#  endswith()
print(greeting.endswith("world!")) #true

# expandtabs()
greeting2="hello\tworld\tthis\tis\tpython"
print(greeting2.expandtabs()) # 8 spaces by default
print(greeting2.expandtabs(10)) # 10 spaces

# find(): returns the index of the first occurrence of a substring, if not found returns -1
print(greeting.find('hello')) #0
print(greeting.find('hellor')) #-1

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
print(greeting.rfind('l'))

# format() -- as used above

# index(): Returns the lowest index of a substring, additional arguments indicate starting 
# and ending index (default 0 and string length - 1). 
# If the substring is not found it raises a valueError.
print(greeting.index('l'))

# rindex()
print(greeting.index('l')) # 2

# isalnum(): Checks alphanumeric character
print(greeting.isalnum()) # false
print("Hello100World".isalnum()) # true - n.b: space is not an alnum char

#isalpha
print(greeting.isalpha()) # false cos space is not alphanumeric
print("Hello100World".isalpha()) # false
print("HelloWorld".isalpha()) # true

#isdecimal
print('123'.isdecimal()) #true
print('12 3'.isdecimal()) #false

#isdigit
print('123'.isdigit()) #true

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

# join()
print(' '.join(python_libraries))

# strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('not')) # 'irty days of py'

# split()
print(greeting.split(', '))

# title(
print(greeting.title())

# swapcase()
print(greeting.swapcase())
print("PRIDE COMES".swapcase())

# startswith
print(greeting.startswith('hel'))
print(greeting.startswith('hello'))

## EXERCISE
print(f'{'Thirty'} {'Days'} {'Of'} {'Python'}')
print(f'{'Coding'} {'For'} {'All'}')
company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.swapcase())
print(company[0:1])
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
pytcompany='Python For Everyone'
print(pytcompany.replace('Everyone', 'All'))
print(company.split(' '))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print(company[0])
print(company[-1])
print(company[10])
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

bcos='You cannot end a sentence with because because because is a conjunction'
print(bcos.find('because'))
print(bcos.rfind('because'))
print(bcos[31:55])
print(company.startswith('Coding'))
print(company.endswith('Coding'))
print('   Coding For All      '.strip()  )
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
r=10
area = int(3.14 * r ** 2)
print(f'The area of a circle with radius {r} is {area} meters square.')
a, b=8,6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {"{:.2f}".format(a/b)}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')