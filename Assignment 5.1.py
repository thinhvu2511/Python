#Write a Python program get alerts issued by US-CERT in the current year and write output to CSV and Excel file.
#Source: https://www.us-cert.gov/ncas/alerts
from bs4 import BeautifulSoup
import requests
import csv

listAllert = []

url = 'https://www.us-cert.gov/ncas/alerts'

for i in range(10): # co 10 trang tren web url
	resp = requests.get(url + "?page=" + str(i))
	soup = BeautifulSoup(resp.content, "html.parser") #xem sourcecode cua url
	allert = soup.select('.view-content .item-list .views-field .field-content ') # lay ma so va ten allert

	for ele in allert:
		listAllert.append(ele.text.replace('\n','')) #ma so va ten allert tren url dang o dang text

newLst = []
for i in range(len(listAllert)):
	ele = listAllert[i].split(":", 1) # tach chuoi 1 lan vi trong allert co nhieu noi dung ton tai dau :
	newLst.append(ele)
	
with open("allert.csv", mode='w') as file:
	writer = csv.writer(file)
	writer.writerow(['CODE','ALLERT'])
	writer.writerows(newLst)
