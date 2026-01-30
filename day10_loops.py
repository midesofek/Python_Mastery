count = 0
# while count < 5:
#     # print(count)
#     count += 1
# else:
#     print('Print sth else')

## BREAK AND CONTINUE
# Break
while count < 5:
    print(count)
    count +=1
    if count == 2:
        break

counter = 0
while counter < 5:
    if counter == 3:
        counter += 1
        continue
    print(counter)
    counter +=1

numbers = [0,1,2,3,4,5] 
for num in numbers:
    print(f'No. {num}')

language = 'Python'
for let in language:
    print(let)

for i in range(len(language)):
    print(language[i])

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

