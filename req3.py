import re
import requests
from bs4 import BeautifulSoup
from typing import Union
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
        # self.Chapters = []
        # self.Pages = []

    @staticmethod
    def getChapters(id_encoded) -> list:
        global chap
        url = f'https://manganelo.com/manga/{id_encoded}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        list1 = []
        for x in re.findall('<a class="chapter-name text-nowrap" (.*?)>', str(soup)):
            chap = {'link': re.findall('href="(.*?)"',x)[0], 'title': re.findall(' title="(.*?)"',x)[0]}
            list1.append(chap)
        list1=list1[::-1]
        for i,x in enumerate(list1):
            x['index'] = i

        # print(list1)
        return list1
    @staticmethod
    def getPages(link) -> list:
        page = requests.get(link)
        list1=[]
        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        for x in re.findall("m\" src=\"(.*?)\" title=", str(soup)):
          list1.append(x)
        return list1


    def showchapters(self):
        return self.Chapters


    def __str__(self):
        return f'Name:{self.Name} '



    # return index1
def search(tex : str) -> Union[list,None]:
    URL = 'https://manganelo.com/getstorysearchjson'
    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'PostmanRuntime/7.26.5'}
    if tex !='':
        try:
            response1 = requests.post(URL, data={'searchword': tex}, headers=header)
            Json_ = response1.json()
            print(Json_)
            if Json_ != []:
                list = []
                for i in Json_:
                    list.append(
                        Manga(i['name'], i['id'],
                              i['id_encode'],
                              i['nameunsigned'],
                              i['lastchapter'],
                              i['image'],
                              i['author']))


                # print(list[0].Author)
                return list
            else:
                return None
        except Exception as e:
            print(e)

# for j in list:
#     print(j.Name + ' / ' + j.Id_encode + ' / ' + j.Id+ ' / ' + j.Lastchapter)
#
# print(list[1].showchapters())
#
# list[1].getChapters()
# # print(list[0].showchapters())
#
#
# # print(list[0].download('https://manganelo.com/chapter/pn918005/chapter_8','https://manganelo.com/chapter/pn918005/chapter_6'))
#
# list[1].getPages(0)
# print(len(list[1].Pages))
# for h in list[1].Pages:
#     print(h)
# for k in list[0].showchapters():
#     print(k)

# for p in list[0].download('https://manganelo.com/chapter/pn918005/chapter_20','https://manganelo.com/chapter/pn918005/chapter_32'):
#     print(p)