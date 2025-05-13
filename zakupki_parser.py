import requests
from bs4 import BeautifulSoup

def get_contracts_by_inn(inn):
    url = f'https://zakupki.gov.ru/epz/contract/search/results.html?searchString={inn}&contractStage=EXECUTION&sortBy=UPDATE_DATE&pageNumber=1'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    contracts = []
    for item in soup.select('.search-registry-entry-block'):
        number_tag = item.select_one('.registry-entry__header-mid__number')
        if not number_tag:
            continue
        title = number_tag.text.strip()
        link = 'https://zakupki.gov.ru' + number_tag['href']
        contracts.append({'title': title, 'link': link})
    return contracts
