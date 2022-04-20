#!/usr/bin/my_env python
from bs4 import BeautifulSoup
import requests

url = 'https://25livepub.collegenet.com/s.aspx?calendar=mc-all_advertised_events&widget=main&spudformat=xhr'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')


# print(soup.prettify()) #prints the html content 

# links = soup.find_all('a')
# for link in links:
#     print(link.text) #gets all event names, can be used


table = soup.find("table", class_="twSimpleTableTable") #GETS THE WHOLE TABLE

print('*' * 80)
print('*' * 80)

event_names = table.find_all('span', class_='twDescription')
for event_name in event_names:
    print(event_name.text) # gets all event names

print('*' * 80) 
print('*' * 80)

all_start_times = table.find_all('span', class_='twStartTime')
for event in all_start_times:
    print(event.text) # gets all start times

print('*' * 80) 
print('*' * 80)

all_locations = table.find_all('span', class_='twLocation')
for location in all_locations:
    print(location.text) # gets all locations