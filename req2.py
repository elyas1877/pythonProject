import re
import requests
from bs4 import BeautifulSoup

URL='https://s51.mkklcdnv51.com/mangakakalot/h1/hakaijuu/vol1_chapter_1_future_is/1.jpg'

#soup = BeautifulSoup(page.content, 'html.parser')
#page_=re.findall('<img alt=(.*?)/>', str(soup))
# for i in page_:
#      print(i)
# with requests.Session() as session:
#     resp_2 = session.get("https://bu3.mkklcdnbuv1.com/mangakakalot/m2/mother_im_sorry/chapter_5_chapter_5/2.jpg", headers={"referer":"https://mangakakalot.com/chapter/ro920198/chapter_5"})
#     with open("xx.jpg","wb") as f:
#         f.write(resp_2.content)
def download_image(url):
    fullname = str(url).split('/')[-1]
    r = requests.get(url,headers={"referer":"https://manganelo.com/chapter/hakaijuu/chapter_1"})
    with open(fullname, 'wb') as outfile:
        outfile.write(r.content)

if __name__ == '__main__':
    download_image('https://s51.mkklcdnv51.com/mangakakalot/h1/hakaijuu/vol1_chapter_1_future_is/5.jpg')
    print('y')

