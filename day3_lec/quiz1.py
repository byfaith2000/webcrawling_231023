import re
from urllib.request import urlopen

f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

encoding = f.info().get_content_charset(failobj='utf-8')
html = f.read().decode(encoding)

#print(html)

for partial_html in re.findall(r'<td class="left"><a.+?</td>', html):
    #print(partial_html)
    url = re.search(r'<a href="(.+?)">', partial_html).group(1)
    url = 'http://www.hanbit.co.kr' + url
    title = re.sub('r<.+?>', '', partial_html)
    print('url : ',url)
    print('title : ',title)
    print('-'*100)
