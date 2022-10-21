#Write a Python program get alerts issued by US-CERT in the current year and write output to CSV and Excel file.
#Source: https://www.us-cert.gov/ncas/alerts

from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.us-cert.gov/ncas/alerts'

def getAllertToFile(url):
	listsAllert = []
	resp = requests.get(url)
	soup = BeautifulSoup(resp.content, "html.parser") #xem sourcecode cua url
	allert = soup.select('.view-content .item-list .views-field .field-content a') 
		
	# Select name and id allert
	for ele in allert:
		list = []
		urlAllert = 'https://cisa.gov/uscert' + ele['href']
		newResp = requests.get(urlAllert)
		newSoup = BeautifulSoup(newResp.content, 'html.parser')

		# Collect id of allert
		idAllert = newSoup.find(id='page-title').text 
		list.append(idAllert[7:16]) 

		# Collect name of id
		nameAllert = newSoup.find(id='page-sub-title').text
		list.append(nameAllert) 
		
		# Collect release date and last revised day.
		date = newSoup.find('div', class_='submitted meta-text').text.strip() 
		releaseDate = date.replace("Original release date: ", "").strip()
		if 'Last revised:' in releaseDate:
			listsdate = releaseDate.split("|")
			releaseDate = listsdate[0]
			lastRevised = str(listsdate[1]).replace("Last revised: ", '').strip()
			list.append(releaseDate)
			list.append(lastRevised)
		else:
			lastRevised = None
			list.append(releaseDate)
			list.append(lastRevised)
			
		# Add link to list.
		list.append(urlAllert)
		listsAllert.append(list)

	# Write file	
	with open("allert.csv", mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Alert ID', 'Alert Name', 'Release Date', 'Last revised', 'Alert Link'])
		writer.writerows(listsAllert)

if __name__ == '__main__':
	getAllertToFile(url)
	print("Successfully.")
