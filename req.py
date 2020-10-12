import re
import urllib
import requests
from bs4 import BeautifulSoup
import json
from clint.textui import progress
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
def download_with_prograss(url,path):
    r = requests.get(url, stream=True)
    path1=path+str(url).split('/')[-1]
    with open(path1, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

def download_image(url):
    fullname = str(url).split('/')[-1]
    urllib.request.urlretrieve(url,fullname)

def main():
    for i in get_manga_list('Hakaijuu'):
        json_ = json.loads('{' + i + '}')
        print(json_)

if __name__=='__main__':
    # download_with_prograss(url='https://download.ir/wp-content/uploads/2020/04/header-54.jpg')
    download_image(url='https://download.ir/wp-content/uploads/2020/04/header-54.jpg')