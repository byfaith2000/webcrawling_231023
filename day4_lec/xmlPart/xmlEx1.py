from bs4 import BeautifulSoup

file = open('books.xml', encoding='utf-8')
book_xml = file.read()
#print(book_xml)

bsObj = BeautifulSoup(book_xml, 'lxml')

for book_info in bsObj.findAll('author'):
    print(book_info.text)
