import re
import requests
from bs4 import BeautifulSoup
import json
URL='https://manganelo.com/manga/Hakaijuu'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
page_=soup.findAll('a',{'class':'chapter-name text-nowrap'})

for i in page_:
    print()

# for i in re.findall(' href="(.*?)" rel=',str(page_)):
#     print(i)
