import statistics
# DATA COLLECTION TYPES IN PYTHON
# List (mutable), Tuple (immutable) 
# Set (immutable), Dictionary (mutable)

lst_creation_method1 = list()
print(lst_creation_method1)
lst_creation_method2 = []
print(len(lst_creation_method2))
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
print('No of Countries',len(countries))

# Accessing list items using Positive indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
last_fruit = fruits[-1]
print('First fruit: ',first_fruit)
print('Last fruit: ', last_fruit)

# Accessing list items using Negative indexing
first_fruit = fruits[-4]
print(first_fruit)

# Unpacking list items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item, second_item, third_item, ' '.join(rest))
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

# Slicing items from a list (positive indexing)
print(lst[0:5]) 
print(lst[0:]) # unpacks all
print(lst[1:])
print(lst[::2])

# Slicing items from a list (negative indexing)
print(lst[-3:-1])
print(lst[-3:])
print(lst[::-1])

# Modifying lists
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Prev fruits:', fruits)
fruits[0] = 'watermelon'
print('Fruits after:', fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'apple'
print(fruits)

# Checking items in a list
print('apple' in fruits) # true
print('banana' in fruits) # false

# To add item to the end of an existing list we use the method append().
fruits.append('avocado')
print(fruits)

# Inserting items at a specified index in a list
fruits.insert(5, 'cashew')
fruits.insert(2, 'pear')
print(fruits)

# Removing items in a list with remove
# fruits.remove('cashew')
# print(fruits)

# Removing items in a list with pop() to remove at a specified index
# fruits.pop()
# print(fruits)
# fruits.pop(1)
# print(fruits)

# Removing items using del
# del fruits[-6]
# print(fruits)

# clearing items using clear()
# fruits.clear()
# print(fruits)

# copying a list
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining a list using + operator
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# print(fruits + vegetables)
fruits.extend(vegetables)
print(fruits)

# The count() method returns the number of times an item appears in a list
print(fruits.count('pear'))

# finding the index of an item
print(fruits.index('Potato'))

# reversing a list
# fruits.reverse()
# print(fruits)

# sorting a list using sort()
# fruits.sort() # ascending order
# print(fruits)
# fruits.sort(reverse=True) # descending order
# print(fruits)

# sorting a list using sort()
# sorted(): returns the ordered list without modifying the original list
print(sorted(fruits))
print(sorted(fruits, reverse=True))

### EXERCISE ###
exercise_list=[]
sports=['football', 'bball', 'volleyball', 'golf', 'pool']
print(len(sports))
print(sports[0], sports[2], sports[-1])

mixed_data_type=['Mide', 25, 6.5, 'Single', 'Lagos']
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])
it_companies.insert(-2, 'Samsung')
print(it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)
print('#'.join(it_companies))
print('Samsung' in it_companies)
it_companies.sort()
print(it_companies)
# it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
last_coy_index=len(it_companies)
print(it_companies[int(last_coy_index/2)])
# print(it_companies.pop(0))
# it_companies.pop(int(last_coy_index/2))
it_companies.pop(-1)
it_companies.clear()
print(it_companies)
del it_companies
# print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
tech_stack=front_end+back_end
print(tech_stack)
full_stack = tech_stack.copy()
full_stack.insert(-3, 'Python and SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age=min(ages)
max_age=max(ages)
print(ages)
print('Min:', min_age, 'Max:', max_age)
median_age=statistics.median(ages)
print('Median:', median_age)
rnge=max_age-min_age
print('Range:', rnge)