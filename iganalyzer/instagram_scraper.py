import requests
from bs4 import BeautifulSoup

def get_name(username: str):
    URL = 'https://www.instagram.com/' + username + '/'
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('meta', attrs = {'property':'og:title'}) 

    name = 'FILLER'

    if (table):
        name = table.attrs['content'].split(' (')[0]

    return name if name != None else 'FILLER'