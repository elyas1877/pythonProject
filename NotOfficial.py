baseURL = 'https://mangasee123.com/'
coverURL = 'https://cover.nep.li/cover/'

'''def ChapterLinkFounder(a):
    URL = '{}/rss/{}.xml'.format(baseURL, a)
    page = req.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return re.findall('<link/>(.*?)<pubdate>', str(soup))'''

def GetChapterURL(manga, chapter):
  chapter_url = baseURL + 'read-online/{}-chapter-{}-page-1.html'.format(manga['i'], chapter)
  manga['ChapterURL'] = chapter_url
  return manga

def ResolveChapterNumber(chapter_id):
  id = chapter_id[1:]
  result = ''
  if int(id[-1]) > 0:
    result = id[:-1] + '.' + id[-1]
  else:
    result = id[:-1]
  return result

def ReplaceWithChapterNumber(chapters):
  for c in chapters:
    c['Chapter'] = ResolveChapterNumber(c['Chapter'])
  return chapters

def DeleteUnusedKeys(li):
  for n in li:
    del n['Type']
    del n['Directory']

def GetChapter(chapters, number):
  for c in chapters:
    if float(c['Chapter']) == float(number):
      return c

# https://s4-1.mangabeast.com/manga/Parallel-Paradise/0113-003.png

def GetChapterPages(manga):
  page_limit = int(manga['ChapterList']['Page'])
  page_url = manga['ChapterList']['cdn'] + '/manga/'+ manga['i'] +'/'+ manga['ChapterList']['Chapter'] + '-'
  pages = {}
  for i in range(1, page_limit + 1):
    page_no = ''
    if i < 10:
      page_no = '00' + str(i)
    elif i < 100:
      page_no = '0' + str(i)
    else:
      page_no = i
    pages[str(page_no)] = page_url + str(page_no) + '.png'
  manga['ChapterList']['PageList'] = pages
  return manga
 
def GetChapterDetails(manga):
  url = manga['ChapterURL']
  response = req.get(url)
  chapter_number = url[url.find('-chapter-')+len('-chapter-'):url.find('-page-')]
  page_source = BeautifulSoup(response.content, 'html.parser')
  page_script = page_source.find_all('script')
  script_source = str(page_script[-1])
  current_path_index = script_source.find('vm.CurPathName')
  chapters_index = script_source.find('vm.CHAPTERS')
  index_index = script_source.find('vm.Index')
  chapter_list_script = str(script_source[chapters_index:index_index])
  path = str(script_source[current_path_index:chapters_index])
  chapters = chapter_list_script[chapter_list_script.find('['):chapter_list_script.find(';')]
  server_path = 'https://' + path[path.find('"')+1:path.find('";')]
  chapters = json.loads(chapters)
  DeleteUnusedKeys(chapters)
  chapters = ReplaceWithChapterNumber(chapters)
  selected_chapter = GetChapter(chapters, chapter_number)
  if selected_chapter is not None:
    selected_chapter['cdn'] = server_path
  del manga['ChapterURL']
  manga['ChapterNo'] = len(chapters)
  manga['ChapterList'] = selected_chapter
  manga = GetChapterPages(manga)
  return manga

def GetChaptersURL(chaptersId):
  pass

def GetAllMangaList():
  response = req.post('{}/_search.php'.format(baseURL), data={})
  return req.models.Response.json(response)

def FindManga(name):
  a_list = GetAllMangaList()
  result = []
  for parameter in a_list:
    name = name.lower()
    if name in parameter['i'].lower() or name in parameter['s'].lower():
      parameter['c'] = '{}{}.jpg'.format(coverURL, parameter['i'])
      result.append(parameter)
    else:
      for x in parameter['a']:
        if name in x.lower():
          parameter['c'] = '{}{}.jpg'.format(coverURL, parameter['i'])
          result.append(parameter)
  return result

#print(FindManga('one piece'))


print(GetChapterDetails(GetChapterURL(FindManga('Ao-Ashi')[0], 203)))
