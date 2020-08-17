import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': 'en-US,en;q=0.9,ko;q=0.8',
}

data = {
    'pageNum': '1',
    'searchGbn': '',
    'searchTxt': '',
    'moreSearchTxt': '',
    'defaultSearchTxt': '',
    'defaultMoreSearchTxt': '',
    'reSearchYn': '',
    'ctlgId': '',
    'orderSort': 'dnldNtD',
    'orderSortScroll': '666',
    'pageSize': '150',
    'searchKeywordTxt': '',
    'typeFilterTxt': '',
    'providerFilterTxt': '',
    'dateFilterTxt': '',
    'priceFilterTxt': ''
}

response = requests.post(
    'https://www.bigdata-finance.kr/dataset/datasetList.do', data=data)

soup = BeautifulSoup(response.text, 'html.parser')

list_1 = soup.select(
    '#frm > div.cont > div > div.tabs-dataset > div > div.dset-lst-wp > div.dset-lst > a')

title = []
# frm > div.cont > div > div.tabs-dataset > div > div.dset-lst-wp > div.dset-lst > a:nth-child(1) > div > strong
for li in list_1:
    a = li.select('a > div.dset-item > strong')
    title.append(a)

title_list = list(map(lambda x: str(x).split(
    'tit">')[1].split('</')[0], title))


# frm > div.cont > div > div.tabs-dataset > div > div.dset-lst-wp > div.dset-lst > a:nth-child(35) > div > p:nth-child(3) > span:nth-child(1) > em
souce = []

for li in list_1:
    a = li.select_one(
        'a > div.dset-item > p:nth-child(3) > span:nth-child(1) > em')
    souce.append(a.text)


df = pd.DataFrame(title_list, souce)
df.to_csv('data_list.csv', encoding='cp949')
