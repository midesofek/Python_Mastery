## PIP = Preferred installer program
## Pip is Python's Package Manager

import numpy
import webbrowser
import requests

print(numpy.version.version)

lst = [1, 2, 3,4, 5]
num_arr = numpy.array(lst)
print(len(num_arr))
print(num_arr * 2)
print(num_arr + 2)


## Open any web browser
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/sofekun-ayomide/',
    'https://github.com/midesofek',
    'https://twitter.com/midesofek',
]

# opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)

url = 'https://www.w3.org/standards/'
res = requests.get(url)
print(res)
print(res.status_code) # status code, success:200
# print(res.headers)
# print(res.text)

## READING FROM AN API
url = 'https://slooth.onrender.com/api/v1/label/0x224b239b8bb896f125bd77eb334e302a318d9e33'
response = requests.get(url)
print(response)
print(response.status_code) 
wallet = response.json()
print(wallet)