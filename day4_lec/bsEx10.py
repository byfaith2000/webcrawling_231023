import re
import string

def clearSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation + string.whitespace) for word in sentence]
    sentence = [word for word in sentence if len(word) > 1]
    return sentence

def clearInput(content):
    content = content.upper()
    content = re.sub(r'\n|\[\d+\]', ' ', content)
    content = bytes(content, 'utf-8')
    content = content.decode('ascii', 'ignore')
    content = content.split('. ')
    return [clearSentence(sentence) for sentence in content]

def getNgramsFromSenentence(content, n):
    output = []
    for i in range(len(content) - n + 1):
        output.append(content[i:i+n])
    return output

from collections import Counter

def getNgrams(content, n):
    content = clearInput(content)
    ngrams_list = []
    ngrams = Counter()

    for sentence in content:
        newNgrams = [' '.join(ngrams) for ngrams in getNgramsFromSenentence(sentence, n)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)
    return ngrams_list, ngrams

#print(getNgrams('it is a good day!!! python[3]. @have a good day', 2))

from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'html.parser')
content = bsObj.find('div', {'id':'mw-content-text'}).getText()
nlist, ngrams = getNgrams(content, 2)
#print(nlist)
print(ngrams)