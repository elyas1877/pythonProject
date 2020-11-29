import re
import requests
from bs4 import BeautifulSoup
import json
# class download:
#     def __init__(self):

class Manga:
    def __init__(self, Name, id, id_encode, nameunsigned, lastchapter, image, author):
        self.Name = Name.replace('<span style="color: #FF530D;font-weight: bold;">', '').replace('</span>', '')
        self.Id = id
        self.Id_encode = id_encode
        self.Nameunsigned = nameunsigned.replace('<span style="color: #FF530D;font-weight: bold;">', '').replace('</span>', '')
        self.Lastchapter = lastchapter.replace('<span style="color: #FF530D;font-weight: bold;">', '').replace('</span>', '')
        self.Image = image
        self.Author = author.replace('<span style="color: #FF530D;font-weight: bold;">', '').replace('</span>', '')
        self.Chapters = []

    def addChapters(self):
        url = f'https://manganelo.com/manga/{self.Id_encode}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        for x in re.findall('<a class="chapter-name text-nowrap" (.*?)>', str(soup)):
            chap = {'link': '', 'title': ''}
            chap['link']=re.findall('href="(.*?)"',x)[0]
            chap['title']=re.findall(' title="(.*?)"',x)[0]
            self.Chapters.append(chap)

    def AddTitels(self, name):
        self.Titels.append(name)

    def showchapters(self):
        return self.Chapters
    def __str__(self):
        return f'Name:{self.Name} '



URL = 'https://manganelo.com/getstorysearchjson'
header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'User-Agent': 'PostmanRuntime/7.26.5'}
response1 = requests.post(URL, data={'searchword': 'solo'}, headers=header)
Json_ = response1.json()

list = []
for i in Json_:
    list.append(
        Manga(i['name'], i['id'],
              i['id_encode'],
              i['nameunsigned'],
              i['lastchapter'],
              i['image'],
              i['author']))
for j in list:
    print(j.Name + ' / ' + j.Id_encode + ' / ' + j.Id)

print(list[0].showchapters())
list[0].addChapters()
# print(list[0].showchapters())
for k in list[0].showchapters()[::-1]:
    print(k['link'])