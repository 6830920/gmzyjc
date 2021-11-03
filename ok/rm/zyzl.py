import requests
from bs4 import BeautifulSoup
import time
baseurl = 'https://www.haoz.net/'
url = 'https://www.haoz.net/jingdian/zhongyi/161998/'
web_html = requests.get(url) 
bs4 = BeautifulSoup(web_html.content, 'lxml')   #声明bs对象和解析器，返回解析后的网页信息
# print(bs4)                              #看起来会比较混乱一点

def getContent(url):
    web_html = requests.get(url) 
    mybs = BeautifulSoup(web_html.content, 'lxml')   #声明bs对象和解析器，返回解析后的网页信息
    ptext = mybs.find('div',id = 'htmlContent').find_all('p')
    text = ''

    for pt in ptext:
        ptext = pt.get_text()
        text = text + '\r\n' + ptext


    # text = mybs.find('div',id = 'htmlContent').get_text()
    title = mybs.find('h1').get_text()

    print(title)
    print(text)
    filedir = title+'.md'
    with open(filedir, 'w', encoding='utf-8') as f:
                # with open(bookdir+'temp.md', 'w', encoding='utf-8') as f:
                    f.write(text)




zzr=bs4.find_all('a')
hrefA = []
for mya in zzr: 
    myhref = mya.get('href')
    if 'haoshu-50' in myhref:
        print(myhref)
        hrefA.append(myhref)

for h1 in hrefA:
    time.sleep(2)
    getContent(baseurl+h1,)
# print(bs4.get_text()) 
# target = bs4.select('div.title.media-heading a')
