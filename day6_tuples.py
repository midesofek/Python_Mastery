# A tuple is a collection of different data types which is ordered and unchangeable (immutable)
empty_tuple = tuple()
print(empty_tuple)
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)
print(len(fruits))

# positive indexing
print(fruits[0])
print(fruits[-1])

# negative indexing
print(fruits[-3])
print(fruits[-2])
print(fruits[-3:])

# range
print(fruits[-3:-1]) # orange, mango

# Changing tuples to list
changed_tpl_to_list = list(fruits)
print(changed_tpl_to_list)

# checking items
print('mango' in fruits)

# joining tuples
vegies = ('tomato', 'carrot')
print('Fruits & Vegies:', fruits + vegies)

# deleting tuples
# It is not possible to remove a single item in a tuple 
# but it is possible to delete the tuple itself using del.
# del vegies
# print(vegies) # would return 'not defined'

# EXERCISES
emp_tuple=tuple()
web_boys=('Jack', 'Jeff', 'Zuck', 'Elon')
web_sis=('Emily', 'Sophie', 'Billy')
web_family=web_boys+web_sis
print(len(web_boys))
print(web_family)

