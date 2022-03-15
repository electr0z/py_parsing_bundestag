from bs4 import BeautifulSoup
import requests


person_list = []
for i in range(0, 740, 20):
    url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'

    q = requests.get(url)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')

    person_block = soup.find_all(class_='bt-open-in-overlay')

    for person in person_block:
        url_person_card = person.get('href')
        person_list.append(url_person_card)
with open("person_list.txt", 'a') as file:
    for element in person_list:
        file.write(f'{element}\n')
