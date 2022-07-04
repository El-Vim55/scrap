import requests
from bs4 import BeautifulSoup


headers = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/103.0.5060.53 Safari/537.36',
                            'Accept-language': 'en-AU, en;q=0.5'})


url = 'https://core-electronics.com.au/raspberry-pi-compute-module-4-lite-1gb-ram.html'
r = requests.get(url, headers=headers)
print('[Response Code]', r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')


#* TITLE
try:
    for title in soup.find_all('h1', attrs=
                                        {'class': 'page-title'}):

        for i in title:
            for j in i:
                title = j
        print("[Title]", title)

except AttributeError:
    print('NA')


#* IN_STOCK
try:
    for stock in soup.find_all('div', attrs=
                                        {'class': 'product alert stock'}):
        x = ''.join(stock.find('p'))
        print('[Stock]', x)
    

except AttributeError:
    print('NA')


#* Price
try:
    for data in soup.find_all('span', attrs=
                                        {'class': 'price'}):
        for price in data:
            print('[Price]', price)

except AttributeError:
    print('NA')
    