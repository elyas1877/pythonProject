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

        for xx,x in enumerate(re.findall('<a class="chapter-name text-nowrap" (.*?)>', str(soup))):
            chap = {'link': '', 'title': '','index':''}
            chap['link']=re.findall('href="(.*?)"',x)[0]
            chap['title']=re.findall(' title="(.*?)"',x)[0]
            chap['index']=xx
            self.Chapters.append(chap)

        self.Chapters = self.Chapters[::-1]


    def showchapters(self):
        return self.Chapters


    def __str__(self):
        return f'Name:{self.Name} '



    # return index1
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
    print(j.Name + ' / ' + j.Id_encode + ' / ' + j.Id+ ' / ' + j.Lastchapter)

print(list[0].showchapters())

list[0].addChapters()
# print(list[0].showchapters())


# print(list[0].download('https://manganelo.com/chapter/pn918005/chapter_8','https://manganelo.com/chapter/pn918005/chapter_6'))
for k in list[0].showchapters():
    print(k)

# for p in list[0].download('https://manganelo.com/chapter/pn918005/chapter_20','https://manganelo.com/chapter/pn918005/chapter_32'):
#     print(p)