import re
import requests
from bs4 import BeautifulSoup
import json


class Manga:
    def __init__(self, Name, id, id_encode, nameunsigned, lastchapter, image, author):
        self.Name = Name
        self.Id = id
        self.Id_encode = id_encode
        self.Nameunsigned = nameunsigned
        self.Lastchapter = lastchapter
        self.Image = image
        self.Author = author
        self.Chapters = []

    def addChapters(self):
        url = f'https://manganelo.com/manga/{self.Id_encode}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for x in re.findall('<a class="chapter-name text-nowrap" (.*?)>', str(soup)):
            self.Chapters.append(x)

    def AddTitels(self, name):
        self.Titels.append(name)

    def showchapters(self):
        return self.Chapters


URL = 'https://manganelo.com/getstorysearchjson'
header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'User-Agent': 'PostmanRuntime/7.26.5'}
response1 = requests.post(URL, data={'searchword': 'solo'}, headers=header)
Json_ = response1.json()
# replace('<span style="color: #FF530D;font-weight: bold;">','').replace('</span>','')
list = []
for i in Json_:
    list.append(
        Manga(i['name'].replace('<span style="color: #FF530D;font-weight: bold;">', '').replace('</span>', ''), i['id'],
              i['id_encode'],
              i['nameunsigned'].replace('<span style="color: #FF530D;font-weight: bold;">', '').replace('</span>', ''),
              i['lastchapter'].replace('<span style="color: #FF530D;font-weight: bold;">', '').replace('</span>', ''),
              i['image'],
              i['author'].replace('<span style="color: #FF530D;font-weight: bold;">', '').replace('</span>', '')))
for j in list:
    print(j.Name + ' / ' + j.Id_encode + ' / ' + j.Id)

print(list[0].showchapters())
# print(Json_)

# page = requests.get(URL)
# a=Manga(URL.split('/')[-1])
# soup = BeautifulSoup(page.content, 'html.parser')
# for x in re.findall('<a class="chapter-name text-nowrap" (.*?)>',str(soup)):
# Json_=json.loads('{'+x.replace('href','"href"').replace('rel','"rel"').replace('title','"title"')+'}')
#      a.AddChapters(x)
# print(len(a.showChapters()))
# for i in a.showChapters():
#  print(a.Name)
#  print(i)
