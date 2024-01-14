import re
from urllib.request import urlopen

uf = urlopen('https://www.hanbit.co.kr/store/books/full_book_list.html')
byte_content = uf.read()
#print(byte_content)
scanned_text = byte_content[0:1024].decode('ascii', errors='replace')
#print(scanned_text)

mobj = re.search(r'charset=\"([\w-]+)\"', scanned_text)
print(mobj)
print(mobj.group())
print(mobj.group(1))

if mobj:
    encoding = mobj.group(1)
else:
    encoding = 'ms949'

text = byte_content.decode(encoding)
print(text)