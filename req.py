import re
import requests
from bs4 import BeautifulSoup
import json
def ChapterLinkFounder(a):
    URL = 'https://mangasee123.com/rss/{}.xml'.format(a)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return re.findall('<link/>(.*?)<pubdate>', str(soup))

def get_manga_list(name):
    URL = ChapterLinkFounder(name)[0]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    page_script = soup.find_all('script')
    page_ = str(page_script[-1])
    first_index = page_.find('vm.CHAPTERS') + 16
    last_index = page_.find('vm.IndexName') - 8
    return page_[first_index:last_index].split('},{')
def download_with_prograss(url):
    r=requests.get(url)
    lis=('Byte','KB','MB','GB')
    lenth = float(r.headers['Content-Length'])
    i=-1
    while int(lenth) > 0 :
     url1 = lenth
     lenth=lenth/1024
     # print(url)
     i=i+1
     # print(i)
    print('{} --> {}'.format(url1,lis[i]))


def download_image(url):
    fullname = str(url).split('/')[-1]
    r = requests.get(url)
    with open(fullname, 'wb') as outfile:
        outfile.write(r.content)

def main():
    for i in get_manga_list('Hakaijuu'):
        json_ = json.loads('{' + i + '}')
        print(i)

if __name__=='__main__':
    main()
    # download_with_prograss(url='https://s1.mangabeast01.com/manga/Hakaijuu/0001-001.png')
    # download_image('https://s1.mangabeast01.com/manga/Hakaijuu/0001-001.png')