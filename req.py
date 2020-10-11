import re
import requests
from bs4 import BeautifulSoup
import json

def ChapterLinkFounder(a):
    URL = 'https://mangasee123.com/rss/{}.xml'.format(a)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return re.findall('<link/>(.*?)<pubdate>', str(soup))





URL = ChapterLinkFounder('We-Never-Learn')[-1]
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
page_script=soup.find_all('script')
page_=str(page_script[-1])
first_index=page_.find('vm.CurChapter')+15
last_index=page_.find('vm.CurPathName')-6
chapter_list=page_[first_index:last_index]
json_=json.loads(chapter_list)
print(json_['Type'])






