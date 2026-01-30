import os
import json
import csv

f = open('./day19_sample.txt')
print(f)


## READING FILE
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()

## Python
# first_10_char = f.read(10)
# print(type(first_10_char))
# print(first_10_char)

## readlines(): read all the text line by line and returns a list of lines
# lines = f.readlines()
# print(type(lines))
# print(lines)
# f.close()

with open('./day19_sample.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

with open('./day19_sample.txt', 'a') as f:
    f.write('This text has to be appended at the end')

with open('./day19_sample_writing.txt', 'w') as f:
    f.write('This text will be written in a newly created file')

## DELETING A FILE
if os.path.exists('./day19_sample_writing.txt'):
    os.remove('./day19_sample_writing.txt')
else:
    print('Path does not exist')

# Changing JSON to Dictionary
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

## Changing Dictionary to JSON
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
person2_json = json.dumps(person, indent=4)
print(type(person2_json))
print(person2_json)

with open('./day19_personexample.json', 'w' , encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


## Saving CSV in PY
with open('./day19_sample_csv.csv',) as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')