# Write a program to get and download all the image in https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales.

from bs4 import BeautifulSoup
import requests
import os

url = 'https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')
images = soup.find_all('img')

os.mkdir('photo')

for i, image in enumerate(images):
    link = image['src']
    with open ('photo' + '/' + str(i+1) + '.png', 'wb') as f:
        try:
            data = requests.get('https:' + link)
        except:
            pass
            
        f.write(data.content)
        print('downloading ' + str(i))
print('Done.')