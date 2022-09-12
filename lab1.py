import requests
print(requests.__version__)

import requests


out = requests.get('https://github.com/jackie174/lab1/blob/master/lab1.py')

with open('filename.txt', 'wb') as r:
    r.write(out.content)