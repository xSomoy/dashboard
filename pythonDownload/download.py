import urllib.request
import os

url = 'https://raw.githubusercontent.com/xSomoy/GoogleDark_Extension/master/README.md'
urllib.request.urlretrieve(url, 'README.md')

file_path = 'README.md'

if os.path.isfile(file_path):
    os.remove(file_path)
    print(f'{file_path} has been removed.')
else:
    print(f'{file_path} does not exist.')

url = 'http://www.example.com'
response = urllib.request.urlopen(url)
webContent = response.read()

with open('example.html', 'wb') as f:
    f.write(webContent)