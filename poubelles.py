from bs4.builder import HTMLTreeBuilder
import requests
from bs4 import BeautifulSoup
from datetime import timedelta, datetime

# Change the tour number depending on your address

soup = BeautifulSoup(requests.get('https://administration.esch.lu/dechets/?street=73&tour=1').content,'html.parser')

scrape = []
result = []

# This part can certainly be shortened WIP

scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)').text.strip().replace(",","")))
scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(3)').text.strip().replace(",","")))
scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(3)').text.strip().replace(",","")))
scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(3)').text.strip().replace(",","")))
scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(3)').text.strip().replace(",","")))
scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(3)').text.strip().replace(",","")))
scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(3)').text.strip().replace(",","")))
scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(3)').text.strip().replace(",","")))
scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(9) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(9) > td:nth-child(3)').text.strip().replace(",","")))
scrape.append(str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(10) > td:nth-child(2)').text.strip())+ " : " + str(soup.select_one('#garbage-table > tbody:nth-child(2) > tr:nth-child(10) > td:nth-child(3)').text.strip().replace(",","")))

def validate(arg):
    if arg.find("Container") >= 0 or arg.find("Cartons en vrac") >= 0 :
            pass
    else:
            result.append(arg)

for i in range(len(scrape)):
    validate(scrape[i])

# print (*result, sep='\n')

# This part of the function is used if you to trigger a notification if there is a collect the next day.
 
today = datetime.today().strftime("%d")
tomorrow = datetime.today() + timedelta(1)

next=[]
for i in range(len(result)):
    if tomorrow == result[i].split(":")[1].split()[1]:
        next.append(result[i].split(":")[0])
        print("tomorrow collect")
    else:
        print(result[i].split(":")[1].split()[1] + " is not tomorrow" )
        pass

print (*next, sep='\n')