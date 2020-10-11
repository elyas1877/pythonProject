import re
import requests
from bs4 import BeautifulSoup
import json

def ChapterLinkFounder(a):
    URL = 'https://mangasee123.com/rss/{}.xml'.format(a)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return re.findall('<link/>(.*?)<pubdate>', str(soup))





URL = ChapterLinkFounder('Hakaijuu')[0]
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
page_script=soup.find_all('script')
page_=str(page_script[-1])
first_index=page_.find('vm.CHAPTERS')+16
last_index=page_.find('vm.IndexName')-8
chapter_list=page_[first_index:last_index].split('},{')
json_=json.loads('{'+chapter_list[0]+'}')
# print(chapter_list.split(','))
print(json_)
# for i in json_:
#     print(i)






