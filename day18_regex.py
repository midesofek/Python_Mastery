import re

## Methods in re module
# re.match() # searches ONLY IN THE BEGINNING of the first line of the string and returns matched objects if found, else returns None
# re.search() # Returns a match object if there is one ANYWHERE in the string, including multiline strings.
# re.findall() # Returns a list containing all matches
# re.split() # Takes a string, splits it at the match points, returns a list
# re.sub() ## Replaces one or many matches within a string

txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I) # re.I is case ignore
match2 = re.match('Ok I love to teach', txt, re.I) # re.I is case ignore
print(match)
print(match2)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language. Not my first tho'''
match = re.search('first', txt, re.I)
print(match)

span = match.span()
print(match.span())
start, end = span
print(start, end)
substr = txt[start:end]
print(substr)

## Searching using findall
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

## Replacing a Substring
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
matches = re.sub('%', '', txt)
print(matches)

## Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?''' 
print(re.split('\n', txt))

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

