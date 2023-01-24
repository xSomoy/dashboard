import requests
from bs4 import BeautifulSoup
import time
import os
start_time = time.time()

index = 1
page_limit = 30
links = []
foo = 1
bar = 1 
while index <= page_limit:
    print("downloading page " + str(index))
    url = "https://flossmoor.portal.iworq.net/FLOSSMOOR/requests/700?search=0&searchField=reqnum_id&page=" + str(index)
    response = requests.get(url)

    print('parsing page ' + str(index))
    soup = BeautifulSoup(response.text, "html.parser")

    print('Adding links to list frome page ' + str(index))
    for link in soup.find_all("a"):
        if foo > 8 and foo < 39:
            if (bar%2) == 0:
              links.append(link.get("href"))
        foo += 1
        bar += 1
    foo = 1
    bar = 1
    index += 1
# os.system('cls')

for i in links:
    print(i)

print(len(links))


end_time = time.time()
print("Program runtime: ", end_time - start_time)



