from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def extract_href_from_detail_btn(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    store_urls = []
    for td_tag in soup.find_all('td', class_='detail-btn'):
        a_tag = td_tag.find('a')
        if a_tag and 'href' in a_tag.attrs:
            href = a_tag['href']
            store_urls.append(urljoin(url, href))
    return store_urls

def extract_fax_number_from_store_url(store_url):
    response = requests.get(store_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    fax_number_tag = soup.find('div', class_='jp-store-information-0001-inner__tel fax clearfix')
    if fax_number_tag:
        fax_number = fax_number_tag.find('div', class_='jp-store-information-0001__text-area-pc').get_text(strip=True)
        print("FAX番号:", fax_number)
    else:
        print("FAX番号は見つかりませんでした。")

# 与えられたURLからhrefを抽出する
url = 'https://toyota.jp/service/dealer/spt/search?CN=P2&OFFICE_CD=05301&padid=dealer_spt_store_list_company_05301'
store_urls = extract_href_from_detail_btn(url)
print(store_urls)

# store_urlsからFAX番号を抽出する
fax_numbers = []
for store_url in store_urls:
    fax_number = extract_fax_number_from_store_url(store_url)
    # fax_numbers.append(fax_number)

# 取得したFAX番号を出力する
# for idx, fax_number in enumerate(fax_numbers, start=1):
#     print(f"店舗{idx}のFAX番号: {fax_number}")

