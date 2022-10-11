# Write a Python program get the number of security alerts issued by US-CERT in the current year.
# Source: https://www.us-cert.gov/ncas/alerts

import requests
from bs4 import BeautifulSoup

listAllert = []
url = 'https://www.us-cert.gov/ncas/alerts'

for i in range(10): # co 10 trang tren web url
    resp = requests.get(url + "?page=" + str(i))
    soup = BeautifulSoup(resp.content, "html.parser") #xem sourcecode cua url
    allert = soup.select('.view-content .item-list .views-field .field-content ') # lay ma so va ten allert

    for ele in allert:
        listAllert.append(ele.text.replace('\n','')) #ma so va ten allert tren url dang o dang text
        
print("The number of security alerts issued by US-CERT in the current year: " + str(len(listAllert)))
