from bs4 import BeautifulSoup

html_str = '''
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
'''

bsObj = BeautifulSoup(html_str, 'html.parser')
ul_tag = bsObj.find('ul')
#print(ul_tag)

litags = ul_tag.findAll('li')
#print(litags)

for li in litags:
    print(li.text)