import requests
from bs4 import BeautifulSoup
import json

with open('person_list.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    dict_data = []
    count = 0
    for line in lines:
        q = requests.get(line)
        result = q.content
        soup = BeautifulSoup(result, 'lxml')

        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        social_urls = soup.find_all(class_='bt-link-extern')

        social_networks_url = []

        for item in social_urls:
            social_networks_url.append(item.get('href'))

        data = {'person_name': person_name,
                'person_company': person_company,
                'social_networks': social_networks_url}

        dict_data.append(data)
        count += 1
        print(f'{count}: {line} is done!')
    with open('data.json', 'w') as file_json:
        json.dump(dict_data, file_json, indent=4)
