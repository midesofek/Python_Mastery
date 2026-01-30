empty_dict = {}
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

person = {
    'first_name': 'Mide',
    'last_name': 'Sofek',
    'age': 250,
    'country': 'Nigeia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Nicon Estate',
        'zipcode': '10011'
    }
}

print(type(person))
print(len(dct))
print(len(person))

print(person['is_married'])
print(dct['key2'])

## Another method to get items in a dict
print(person.get('address'))
print(person.get('balance')) ## intentionally trying item that doesn't exist
# print(dct['name']) ## creating the error

## Adding new items to a dictionary
dct['key5'] = 'value5'
print(dct)

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

dct['key1'] = 'value-one'
print(dct)

print('key1' in dct)
print('key6' in dct)

dct.pop('key5') # removes the specified item
dct.popitem() # removes the last item
del dct['key3'] # removes t
print(dct)

# converting dictionary to a list of items
print(dct.items())

# print(dct.clear())

# del dct
# print(dct)

dct_copy = dct.copy()
keys = dct.keys()
print(keys)

values = dct.values()
print(values)

dog = {
    'name': 'leo', 'color': 'red', 'breed': 'rotwhiler', 'legs': '4', 'age': 7
}
student = {
    'first_name': 'Glory',
    'last-name': 'Diamond',
    'gender': 'Female',
    'age': 26,
    'marital_status': 'single',
    'skills': ["model", "singing", "media", "art"], 
    'country': 'Nigeria',
    'city': 'Lagos',
    'address': ''
}
print(len(student))
print(student.values())
print(student.keys())
print(student.items())
del student['address']
print(student)
del student
# print(student)