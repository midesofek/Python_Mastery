st= set()
st = {'item1', 'item2', 'item3', 'item4'}   
print(st)
print(len(st))

# Checking items in a set
print('item3' in st)

# adding items to a set
st.add('item5')
print(st)

# add multiple items using update()
st.update(['item6', 'item7', 'item8'])
print(st)

# removing with remove()
st.remove('item7')
print(st)

# pop() methods remove a random item from a list and it returns the removed item.
removed_item = st.pop()
print(st)
print('removed item:',removed_item)

# # clear with clear()
# st.clear()
# print(st)

# # deleting a set with del
# del st
# print(st)

# converting set to list
st = list(st)
list_arr=["Stuff1", 'Stuff2', 'Stuff3']
print(st)

# joining sets with union()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3= st1.union(st2)
print(st3)

# joining sets with update()
st1.update(st2)
print(st1)

# finding intersection items
st4 = {'item1', 'item2', 'item3', 'item4'}
st5 = {'item3', 'item2'}
print(st4.intersection(st5))

# checking subset
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

# checking difference
print(st2.difference(st1))